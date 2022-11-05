from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

from .models import User

from .serializers import UserInfoSerializer

from .authentication import *

# Create your views here.

'''
221105 로그인 view 추가
'''

class AuthAPI(APIView):
    def get(self, request):
        print(request.data['uid'])

        inputId = request.data['uid']
        inputPw = request.data['password']

        controlLogin = ControlLogin_b()
        serializer = controlLogin.checkLogin(inputId, inputPw)

        if serializer == "error":
            return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)