from twilio import rest

# Your Account SID from twilio.com/console
account_sid = "AC0e321a9f5a5d0ed762e3b79a2571d9cf"
# Your Auth Token from twilio.com/console
auth_token  = "3a126dff7088fb447c1fcd18e6696d01"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+919092495510", 
    from_="+12564877144",
    body="Hello from Python!")

print(message.sid)