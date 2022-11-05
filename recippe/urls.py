from django.urls import path, include

from .views import *

'''
221105 로그인 과정 위해 login/ 링크 추가, 
221105 이메일 과정 위해 emailcheck/ 링크 추가 (미완), 
221105 자동로그인 해제 위해 cancelAutoLogin/ 링크 추가,
'''

urlpatterns = [
    path("login/", LoginAPI.as_view()),
    path("cancelAutoLogin/", CancelAutoLoginAPI.as_view()),
    path("emailcheck/", EmailAPI.as_view()),
]