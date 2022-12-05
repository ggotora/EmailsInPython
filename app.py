import smtplib
from email.message import EmailMessage
import mimetypes
import json
import os 

f = open("secrets.json")
secrets = json.load(f)

# Setup email message 
message = EmailMessage()
sender = secrets["username"]
recipient = secrets["username"]
sender = "ispeakjavascript.gmail.com"
message['From'] = sender
message['To'] = recipient
message["Subject"] = "Hello world"
body = """Hey there!
...
... I'm learning to send emails using Python!"""
message.set_content(body)
print(message)

# Attachment 
attachment_path = "/tmp/processed.pdf"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

# Add attachment to message 
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                            maintype=mime_type,
                         subtype=mime_subtype,
                         filename=os.path.basename(attachment_path))

print(message)


server = smtplib.SMTP_SSL('smtp.gmail.com')
server.login(secrets["username"], secrets["password"])
server.send_message(message)
server.close()