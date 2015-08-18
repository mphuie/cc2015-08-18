import urllib2
import json
import datetime

response = urllib2.urlopen('http://localhost:5000/inventory').read()
inventory = json.loads(response)

now = datetime.datetime.today()
for item in inventory:


  expirationDateObject = datetime.datetime.strptime(item["expirationDate"], "%Y-%m-%d")

  if now > expirationDateObject:
    print "this item is expired!!"
