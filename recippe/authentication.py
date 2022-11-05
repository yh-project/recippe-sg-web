from rest_framework.generics import get_object_or_404

from django.core.mail import EmailMessage

from .models import User

from .serializers import *

import random

import smtplib
from email.mime.text import MIMEText

'''
221105 로그인 class 추가
221105 이메일인증 class 추가
'''

class ControlLogin_b():

    def checkLogin(self, id, pw):
        dbCheck = get_object_or_404(User, uid=id)
        print("hello", dbCheck.nickname)

        if dbCheck.password == pw:
            print("Login Success")
            serializer = self.sendResult(1, dbCheck)
            return serializer
        else:
            print("Login Fail")
            self.sendResult(0, self.serializer)

    def sendResult(self, result, userInfo=None):
        if result == 1:
            serializer = UserInfoSerializer(userInfo)
            return serializer
        elif result == 0:
            return "error"

class ControlEmailVerification_b():
    def startCheck(self, request):
        code = random.randrange(100000, 1000000)
        request.POST._mutable = True
        request.data['code'] = code
        serializer = EmailVerificationSerializer(data=request.data)
        
        if serializer.is_valid():
            print("hello")
            return "이메일 등록 성공"
        else:
            return "이메일 등록 실패"
        
    def sendCode(self, email, code):
        print(email)
        email_contents = EmailMessage(
            '인증 코드 전송',
            f"인증 코드는 {code}",
            to=[email],
        )
        print(email_contents)
        res = email_contents.send()
        #smtp = smtplib.SMTP('smtp.gmail.com', 587)


        result = self.sendResult(res)
        return result

    def sendResult(self, result):
        if result == 1:
            print("이메일 전송 성공")
            return "이메일 전송 성공"
        elif result == 0:
            print("이메일 전송 실패")
            return "이메일 전송 실패"