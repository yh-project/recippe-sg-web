from django.urls import path, include

from .views import AuthAPI

'''
221105 로그인 과정 위해 login/ 링크 추가
'''

urlpatterns = [
    path("login/", AuthAPI.as_view()),
]