from rest_framework.generics import get_object_or_404

from django.core.mail import EmailMessage
from django.db.models import Q

from .models import *

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
221106 이메일인증 finishCheck 추가, 이메일전송코드 추가
221106 최종 회원가입 class 추가
'''

class ControlLogin_b():

    def checkLogin(self, id, pw):
        dbCheck = get_object_or_404(User, uid=id)

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
            result = self.sendResult(1)
        else: result = self.sendResult(0)
        return result

    def finishCheck(self, request):
        try:
            self.codeCheck = TempEmail.objects.get(email = request.data['email'])

            if self.codeCheck.code == request.data['code']:
                result = self.sendResult(4)
                return result
            else:
                result = self.sendResult(3)
                return result
        except:
            result = self.sendResult(2)
            return result
            
    def sendResult(self, result):
        if result == 1:
            print("이메일 전송 성공")
            return "이메일 전송 성공"
        elif result == 0:
            print("이메일 전송 실패")
            return "이메일 전송 실패"
        elif result == 2:
            print("존재하지 않는 이메일 입력")
            return "존재하지 않는 이메일 입력"
        elif result == 3:
            print("잘못된 코드")
            return "잘못된 코드"
        elif result == 4:
            print("이메일 인증 최종 완료")
            return "이메일 인증 최종 완료"

class ControlSignUp_b():
    def checkOverlap(self, id, nickname):
        idCheck = User.objects.filter(uid=id)
        nickCheck = User.objects.filter(nickname=nickname)

        if len(idCheck) > 0 and len(nickCheck) == 0:
            result = self.sendResult("중복된 아이디")
        elif len(idCheck) == 0 and len(nickCheck) > 0:
            result = self.sendResult("중복된 닉네임")
        elif len(idCheck) > 0 and len(nickCheck) > 0:
            result = self.sendResult("아이디, 닉네임 모두 중복")
        elif len(idCheck) == 0 and len(nickCheck) == 0:
            result = self.sendResult("중복되지 않은 아이디, 닉네임")

        return result

    def sendResult(self, result):
        if result == "중복된 아이디":
            return 0
        elif result == "중복된 닉네임":
            return 1
        elif result == "아이디, 닉네임 모두 중복":
            return 2
        elif result == "중복되지 않은 아이디, 닉네임":
            return 3
