import smtplib
import json
f = open("secrets.json")
secrets = json.load(f)
print(secrets)

email = """This is a new email saka so"""

server = smtplib.SMTP_SSL('smtp.gmail.com')
server.login(secrets["username"], secrets["password"])
server.sendmail(secrets["username"], secrets["password"], email)