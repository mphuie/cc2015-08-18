import requests
import json
import datetime

r = requests.get('http://localhost:5000/inventory')
inventory = r.json()

now = datetime.datetime.today()
for item in inventory:


  expirationDateObject = datetime.datetime.strptime(item["expirationDate"], "%Y-%m-%d")

  if now > expirationDateObject:
    print "this item is expired!!"

    for user in item["notifyUsers"]:
      r = requests.post("http://localhost:5000/notifications", data=dict(user=user, message="%s is expired!" % item["label"]))
      print r.status_code
