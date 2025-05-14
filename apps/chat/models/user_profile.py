# 사용자 프로필, 스터디 그룹 정보 관리

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    studies = models.ManyToManyField('chat.StudyGroup', related_name='members')     #사용자가 참여중인 스터디 그룹 목록

    def __str__(self):
        return self.user.username
