from twilio.rest import Client
import smtplib

MY_EMAIL = "robotjonas123@gmail.com"
MY_PASSWORD = "apfzogtsuajirtkn"

TWILIO_SID = "AC308754fc305f4072cbad3761aea6f1c1"
TWILIO_AUTH_TOKEN = "b04906c4f8c51a8b1031cdb838c61bf0"
TWILIO_VIRTUAL_NUMBER = "+12516511990"
TWILIO_VERIFIED_NUMBER = "+5583991624250"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
