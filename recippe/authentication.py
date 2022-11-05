from rest_framework.generics import get_object_or_404

from .models import User

from .serializers import UserInfoSerializer

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
    def startCheck(email):
        pass