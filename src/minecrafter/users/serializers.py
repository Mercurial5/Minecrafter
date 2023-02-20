from utils.serializers import InputSerializer, OutputSerializer
from utils.serializers import fields


class UserOutputSerializer(OutputSerializer):
    id = fields.StringField()
    telegram_id = fields.StringField()
    username = fields.StringField()
    created = fields.DateTimeField(date_format='%Y-%m-%d %H:%M:%S')


class UserCreateSerializer(InputSerializer):
    telegram_id = fields.IntegerField()
    username = fields.StringField()

    def __init__(self, data: dict):
        super().__init__(data)
