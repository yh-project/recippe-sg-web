from django.urls import path, include

from .views import LoginAPI

'''
221105 로그인 과정 위해 login/ 링크 추가
'''

urlpatterns = [
    path("login/", LoginAPI.as_view()),
]