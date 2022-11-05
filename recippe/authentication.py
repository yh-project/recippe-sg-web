from rest_framework.generics import get_object_or_404

from django.core.mail import EmailMessage

from .models import User

from .serializers import *

import random

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient import errors
from email.message import EmailMessage
import base64

def gmail_authenticate():
    SCOPES = ['https://mail.google.com/']
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('./token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, message_text):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = to.split(",")
    message["Subject"] = subject
    message.set_content(message_text)
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf8')}
    
def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)

'''
221105 로그인 class 추가
221105 이메일인증 class 추가
221105 로그아웃 class 추가
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


class ControlLogout_b():
    def cancelAutoLogin(self, nickname):
        # 앞의 nickname은 db의 nickname 뒤의 nickname은 매개변수 
        dbCheck = get_object_or_404(User, nickname = nickname)
        print(f"ControlLogout_b's dbCheck success")
        dbCheck.auto_login = 0
        dbCheck.save()

        dbCheck = get_object_or_404(User, nickname = nickname)
        print(f"ControlLogout_b's second dbCheck success")
        if dbCheck.auto_login == 0:
            return self.sendResult(True)
        else:
            return self.sendResult(False)
        
    def sendResult(self, result):
        if result == True:
            print("자동 로그인이 성공적으로 해제되었습니다.")
            return "자동 로그인이 성공적으로 해제되었습니다."
        else:
            print("자동 로그인 해제에 실패했습니다.")
            return "자동 로그인 해제에 실패했습니다."


class ControlEmailVerification_b():
    def startCheck(self, request):
        code = random.randrange(100000, 1000000)
        request.POST._mutable = True
        request.data['code'] = code
        serializer = EmailVerificationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return "이메일 등록 성공"
        else:
            return "이메일 등록 실패"
        
    def sendCode(self, email, code):
        service = gmail_authenticate()
        message = create_message("레쉽피", email, "테스트", str(code))
        result =  send_message(service, "recippesg@gmail.com", message)
        if result is not None:
            result = "이메일 전송 성공"
        else: result = "이메일 전송 실패"
        return result

    def sendResult(self, result):
        if result == 1:
            print("이메일 전송 성공")
            return "이메일 전송 성공"
        elif result == 0:
            print("이메일 전송 실패")
            return "이메일 전송 실패"
