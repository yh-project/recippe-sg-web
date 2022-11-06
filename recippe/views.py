from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404

from .models import User

from .serializers import *

from .authentication import *

# Create your views here.

'''
221105 로그인 view 추가
221105 이메일 view 추가
221105 자동로그인 해제 view 추가
221106 이메일 인증 get 함수 추가
221106 최종 회원가입 view 추가
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
            
class EmailAPI(APIView):
    def post(self, request):
        print(request.data['email'])

        emailVerification = ControlEmailVerification_b()
        uploadRes = emailVerification.startCheck(request)

        if uploadRes == "이메일 등록 성공":
            sendRes = emailVerification.sendCode(request.data['email'], request.data['code'])
            if sendRes == "이메일 전송 성공":
                return Response("이메일 전송 완료", status=status.HTTP_200_OK)
            elif sendRes == "이메일 전송 실패":
                return Response("이메일 전송 실패", status=status.HTTP_400_BAD_REQUEST)
        elif uploadRes == "이메일 등록 실패":
            return Response("에러", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        print(f"email = {request.data['email']}, code = {request.data['code']}")

        emailVerification = ControlEmailVerification_b()
        checkRes = emailVerification.finishCheck(request)

        if checkRes == "존재하지 않는 이메일 입력":
            return Response("존재하지 않는 이메일 입력", status=status.HTTP_400_BAD_REQUEST)
        elif checkRes == "잘못된 코드":
            return Response("잘못된 코드", status=status.HTTP_400_BAD_REQUEST)
        elif checkRes == "이메일 인증 최종 완료":
            return Response("이메일 인증 최종 완료", status=status.HTTP_200_OK)

class SignUpAPI(APIView):
    def post(self, request):
        print(request.data)

        signUp = ControlSignUp_b()
        overlapRes = signUp.checkOverlap(request.data['uid'], request.data['nickname'])

        if overlapRes == 0:
            return Response(0, status=status.HTTP_400_BAD_REQUEST)
        elif overlapRes == 1:
            return Response(1, status=status.HTTP_400_BAD_REQUEST)
        elif overlapRes == 2:
            return Response(2, status=status.HTTP_400_BAD_REQUEST)
        elif overlapRes == 3:
            serializer = UserInfoSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(4, status=status.HTTP_200_OK)
            else:
                return Response(3, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

