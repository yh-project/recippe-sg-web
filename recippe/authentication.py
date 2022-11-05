from rest_framework.generics import get_object_or_404

from .models import User

from .serializers import UserInfoSerializer

'''
221105 로그인 class 추가
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

'''
221105 로그아웃 class 추가
'''

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
