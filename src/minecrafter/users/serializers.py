from utils.serializers import BaseSerializer
from utils.serializers import fields


class UserCreateSerializer(BaseSerializer):
    id = fields.StringField(read_only=True)
    telegram_id = fields.IntegerField()
    username = fields.StringField()
    created = fields.DateTimeField(date_format='%Y-%m-%d %H:%M')

    def __init__(self, data: dict):
        super().__init__(data)
