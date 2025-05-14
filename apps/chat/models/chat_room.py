# 채팅방 정보, 멤버 관리

from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    study_group = models.OneToOneField('chat.StudyGroup', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, through='ChatRoomMembers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ChatRoomMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'chatroom')