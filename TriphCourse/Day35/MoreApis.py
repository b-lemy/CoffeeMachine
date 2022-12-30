from twilio.rest import Client
import os

# TWILIO_ACCOUNT_SID = "AC7de9eea9d7014a3c88a8022ea5bc3811"
# TWILIO_AUTH_TOKEN = "72d115a50e43f5f0b30bbad589dafd6f"

# account_sid = os.environ[TWILIO_ACCOUNT_SID]
# auth_token = os.environ[TWILIO_AUTH_TOKEN]

account_sid = "AC7de9eea9d7014a3c88a8022ea5bc3811"
# Real Token
# auth_token = "d44a7eb0883b0d65b011dd7cf351bb30"
auth_token = "..............."

client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                     body="Dont forget your charge pllllllzzzzzzzzzz"
                          "never ever brother",
                     from_='+17208026293',
                     to='+255 757 983 352'
                 )

print(message.status)
