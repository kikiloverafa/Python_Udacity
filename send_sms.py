#from twilio.rest import Client
from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC48697829c2d37c558044bffc802df216"
# Your Auth Token from twilio.com/console
auth_token  = "5517142823d2ad37e39482fb9dcd4ac7"

#client = Client(account_sid, auth_token)
client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+15095921206", 
    from_="+15095530591 ",
    body="My name is Kiki. Hello from Python!")

print(message.sid)
