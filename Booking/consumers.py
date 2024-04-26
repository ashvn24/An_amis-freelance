import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class AdminConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("admin_notifications", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard("admin_notifications", self.channel_name)

    def appointment_created(self, event):
        message = event["message"]
        booking_details = event["booking_details"]
        self.send(text_data=json.dumps({"message": message, "booking_details": booking_details}))