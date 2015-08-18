import app
import json
from nose.tools import *

test_app = app.app.test_client()

test_user = "mphuie"
test_item = dict(expirationDate="2015-12-01", label="test2")

def test_inventory_list():
	rv = test_app.get("/inventory")
	resp = json.loads(rv.data)
	eq_(rv.status_code, 200)
	eq_(len(resp), 0)

def test_inventory_add():
  rv = test_app.post("/inventory", data={})
  eq_(rv.status_code, 400)

  rv = test_app.post("/inventory", data=test_item)
  eq_(rv.status_code, 200)
  
  rv = test_app.get("/inventory")
  resp = json.loads(rv.data)
  eq_(rv.status_code, 200)
  eq_(len(resp), 1)

def test_add_notification_user():
  rv = test_app.put("/inventory/%s?action=addNotify" % test_item["label"], data=dict(user=test_user))
  eq_(rv.status_code, 200)

def test_delete_and_notification():
  rv = test_app.get("/notifications/%s" % test_user)
  resp = json.loads(rv.data)
  eq_(rv.status_code, 200)
  eq_(len(resp), 0)

  rv = test_app.post("/notifications", data=dict(user=test_user, message="test notification"))
  resp = json.loads(rv.data)
  eq_(rv.status_code, 200)
  
  rv = test_app.get("/notifications")
  resp = json.loads(rv.data)
  eq_(rv.status_code, 200)
  eq_(len(resp), 1)

  # this should trigger a notification
  rv = test_app.delete("/inventory/%s" % test_item["label"])
  eq_(rv.status_code, 200)

  rv = test_app.get("/notifications/%s" % test_user)
  resp = json.loads(rv.data)
  eq_(rv.status_code, 200)
  eq_(len(resp), 2)

  rv = test_app.delete("/inventory/doesnotexist")
  eq_(rv.status_code, 404)




