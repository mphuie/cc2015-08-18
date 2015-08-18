from flask import request
from flask_restful import reqparse, Resource, abort
import datetime
from notifications import NOTIFICATIONS

INVENTORY = []

inventory_parser = reqparse.RequestParser()
inventory_parser.add_argument("label", type=str, help="Label (string)", required=True)
inventory_parser.add_argument("expirationDate", type=str, help="Expiration date (string in YYYY-MM-DD)", required=True)


class InventoryList(Resource):
  def get(self):
    return INVENTORY

  def post(self):
    global INVENTORY
    args = inventory_parser.parse_args()
    args["notifyUsers"] = []
    INVENTORY.append(args)
    return args


class InventoryItem(Resource):
  def get(self, label):
    item_query = [i for i in INVENTORY if i["label"] == label]
    if len(item_query) == 1:
      return item_query[0]
    else:
      abort(404, message="Not found")

  # Update inventory item notifications list
  def put(self, label):
    if "user" in request.form and "action" in request.args:

      action = request.args["action"]
      user = request.form["user"]

      item_query = [i for i in INVENTORY if i["label"] == label]
      if len(item_query) == 1:
        item = item_query[0]

        if action == "addNotify":
          item["notifyUsers"].append(user)
        if action == "removeNotify":
          item["notifyUsers"] = [i for i in item["notifyUsers"] if i != user ]

        return item

      else:
        abort(404, message="Not found")
    else:
      abort(400, message="User or action not specified!")

  def delete(self, label):
    global INVENTORY
    global NOTIFICATIONS
    item_query = [i for i in INVENTORY if i["label"] == label]
    if len(item_query) == 1:
      item = item_query[0]

      for user in item["notifyUsers"]:
        NOTIFICATIONS.append({ "user": user, "message": "%s was removed" % (item["label"])})

      INVENTORY = [i for i in INVENTORY if not (i["label"] == label)]
    else:
      abort(404, message="Not found")
    return INVENTORY