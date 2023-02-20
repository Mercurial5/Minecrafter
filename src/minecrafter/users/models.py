from datetime import datetime

import mongoengine


class User(mongoengine.Document):
    id = mongoengine.ObjectIdField()
    telegram_id = mongoengine.IntField(min_value=0, required=True)
    username = mongoengine.StringField(min_length=4, required=True)
    created = mongoengine.DateTimeField(default=datetime.now)
