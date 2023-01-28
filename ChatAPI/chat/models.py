import django

django.setup()
import datetime
from django.db import models
from users.models import User


class Conversation(models.Model):
    initiator = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="convo_starter"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="convo_participant"
    )
    start_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, related_name='message_sender')
    text = models.TextField(blank=True)
    attachment = models.FileField(blank=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)


class Notification(models.Model):
    to = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name='notification_to')
    message = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def since(self):
        now = datetime.now()
        diff = now - self.timestamp
        if diff.days >= 1:
            return f"{diff.days} h"
        elif diff.seconds >= 3600:
            return f"{diff.seconds // 3600} h"
        elif diff.seconds >= 60:
            return f"{diff.seconds // 60} m"
        else:
            return f"{diff.seconds} s"