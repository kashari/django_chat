from django.apps import apps
from django.db import models
from datetime import datetime, timezone
from users.models import User


class Notification(models.Model):
    to = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, related_name='notification_to')
    message = models.TextField(blank=False)
    opened = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

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


apps.get_app_config('notifications').ready()
