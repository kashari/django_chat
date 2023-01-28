from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification
from users.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=User)
def created_or_updated_user_notification(sender, instance, created, **kwargs):
    if created:
        message = "Your account was created successfully."
    else:
        message = f"Hello {instance.username}. Your account was updated successfully."

        async_to_sync(get_channel_layer().group_send)(
            f"notification_{instance.id}", {
                "type": "user.notification",
                "message": message
            }
        )

    Notification.objects.create(to=instance, message=message)
