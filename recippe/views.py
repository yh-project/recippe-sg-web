from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

from .models import User

from .serializers import UserInfoSerializer

# Create your views here.

'''
221105 로그인 view 추가
'''

class AuthAPI(APIView):
    def get(self, request):
        serializer = UserInfoSerializer(data=request.data)

        if serializer.is_valid():
            inputId = serializer.validated_data['uid']
            inputPw = serializer.validated_data['password']
            
            controlLogin = ControlLogin_b(serializer)
            controlLogin.checkLogin(inputId, inputPw)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)








class ControlLogin_b():
    def __init__(self, serializer):
        self.serializer = serializer

    def checkLogin(self, id, pw):
        dbCheck = get_object_or_404(User, uid=id)

        if dbCheck.password == pw:
            print("Login Success")
            self.sendResult(1, dbCheck)
        else:
            print("Login Fail")
            self.sendResult(0, self.serializer)

    def sendResult(self, result, userInfo=None):
        if result == 1:
            return Response(userInfo, status=status.HTTP_200_OK)
        elif result == 0:
            return Response(userInfo, status=status.HTTP_404_NOT_FOUND)