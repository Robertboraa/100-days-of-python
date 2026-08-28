import smtplib

from twilio.rest import Client
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_whatsapp(self, message):
        self.client.messages.create(
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
            body=message
        )

    def send_emails(self, email_list, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for user in email_list:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user["email"],
                    msg=f"Subject:Low Price Alert!\n\nDear {user['name']},\n\n{message}"
                )