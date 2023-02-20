from datetime import datetime

import mongoengine
from bson.objectid import ObjectId


class User(mongoengine.Document):
    id = mongoengine.ObjectIdField(primary_key=True, default=ObjectId)
    telegram_id = mongoengine.IntField(unique=True, min_value=0, required=True)
    username = mongoengine.StringField(unique=True, min_length=4, required=True)
    created = mongoengine.DateTimeField(default=datetime.now)
