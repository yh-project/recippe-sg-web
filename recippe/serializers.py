from dataclasses import field
from re import search
from rest_framework import serializers
from .models import Ingredients, Units, User,  PhotoPost, RecipePost, Mail, LikeInfo, Comment, Refrigerator, Recipe_Ingredients, Report, TempEmail

'''
221105 유저 serializer 추가
221105 이메일인증 serializer 추가
'''

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname', 'uid', 'password', 'email', 'auto_login')

class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempEmail
        fields = ('email', 'code')