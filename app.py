import json
f = open("secrets.json")
secrets = json.load(f)
print(secrets)