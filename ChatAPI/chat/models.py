import django

django.setup()
from datetime import datetime, timezone
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

    @property
    def since(self):
        now = datetime.now(tz=timezone.utc)
        diff = now - self.timestamp
        if diff.days >= 365:
            return f"{diff.strftime('%d %b %y')}"
        elif diff.days >= 28:
            return f"{diff.strftime('%d %b')}"
        elif diff.days >= 7:
            return f"{diff.days // 7}w ago"
        elif diff.days >= 1:
            return f"{diff.days}d ago"
        elif diff.seconds >= 3600:
            return f"{diff.seconds // 3600}h ago"
        elif diff.seconds >= 60:
            return f"{diff.seconds // 60}m ago"
        else:
            return f"{diff.seconds}s ago"
