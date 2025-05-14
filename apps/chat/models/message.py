# 메시지 내용, 타입, 첨부파일, 읽음 여부관리

from django.db import models
from django.contrib.auth.models import User

from apps.chat.models.chat_room import ChatRoom


class Message(models.Model):
    TEXT = 'text'
    IMAGE = 'image'
    FILE = 'file'
    CONTENT_TYPE_CHOICES = [
        (TEXT, 'text'),
        (IMAGE, 'image'),
        (FILE, 'file'),
    ]

    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    chat_room = models.ForeignKey('chat.ChatRoom', on_delete=models.CASCADE)
    content = models.TextField()
    contentType = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, default=TEXT)
    file_attachment = models.FileField(upload_to='chat_files/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read_by = models.ManyToManyField(User, related_name='read_messages', blank=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f'{self.sender}: {self.content[:20]}'