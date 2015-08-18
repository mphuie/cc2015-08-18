from flask import Flask, request
from flask_restful import Api


app = Flask(__name__)
api = Api(app)

from resources.notifications import NotificationList, UserNotifications
from resources.inventory import InventoryList, InventoryItem

api.add_resource(InventoryList, '/inventory')
api.add_resource(InventoryItem, '/inventory/<label>')
api.add_resource(NotificationList, '/notifications')
api.add_resource(UserNotifications, '/notifications/<user>')

if __name__ == '__main__':
  app.run()