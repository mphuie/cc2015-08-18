from flask import request
from flask_restful import Resource, reqparse
import datetime

NOTIFICATIONS = []


notification_parser = reqparse.RequestParser()
notification_parser.add_argument("user", type=str, help="User to notify (string)", required=True)
notification_parser.add_argument("message", type=str, help="Message (string)", required=True)


class NotificationList(Resource):
  def get(self):
    return NOTIFICATIONS

  def post(self):
    args = notification_parser.parse_args()
    NOTIFICATIONS.append(args)
    return args


class UserNotifications(Resource):
  def get(self, user):
    return [n for n in NOTIFICATIONS if n["user"] == user]

