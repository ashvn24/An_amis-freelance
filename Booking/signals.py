from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book
import channels.layers
from asgiref.sync import async_to_sync
import json


@receiver(post_save, sender=Book)
def appointment_created(sender, instance, created, **kwargs):
    if created:
        # Notify admin about the new appointment along with details
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "admin_notifications",
            {
                "type": "appointment_created",
                "message": "New appointment created.",
                "booking_details": {
                    "customer_name": instance.user.email,
                    "Name": instance.Name,
                    "Phone": instance.Phone,
                    "time": instance.time,
                    "date": instance.date.strftime("%Y-%m-%d"),
                },
            },
        )