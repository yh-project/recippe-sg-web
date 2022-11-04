from django.contrib import admin

from .models import User

'''
221105 User 관련 데이터 관리 admin 추가
'''

# Register your models here.
admin.site.register(User)