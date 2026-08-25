from twilio.rest import Client

TWILIO_SID = ""
TWILIO_TOKEN = ""
TWILIO_NUMBER = ":"  # twilio sandbox number
MY_NUMBER = ":"     # your number

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_whatsapp(self, message):
        self.client.messages.create(
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
            body=message
        )