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

class LoginAPI(APIView):
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

'''
221105 자동로그인 해제 view 추가
'''

class CancelAutoLoginAPI(APIView):
    def post(self, request):
        print(f"CancleAutoLogin Class start")

        inputNickname = request.data['nickname']

        controlLogout = ControlLogout_b()
        result = controlLogout.cancelAutoLogin(inputNickname)

        if result == "자동 로그인이 성공적으로 해제되었습니다.":
            return Response(result, status=status.HTTP_200_OK)
        elif result == "자동 로그인 해제에 실패했습니다.":
            return Response(result,status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            
        