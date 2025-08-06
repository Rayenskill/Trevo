from django.contrib.auth import get_user_model
from django.db import models

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    chat_name = models.CharField(null=True, blank=True, max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}-{self.chat_name}" if self.sender else f"{self.message}-{self.chat_name}"
    
    