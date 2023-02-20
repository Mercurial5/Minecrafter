from datetime import datetime

from utils.serializers.fields import BaseField
from utils.serializers.fields.exceptions import FailedCast


class DateTimeField(BaseField):

    def __init__(self, date_format: str, date_output_format: str = None):
        super().__init__()
        self.date_format = date_format
        self.date_output_format = date_format if not date_output_format else date_output_format

    def perform_cast(self, value: str) -> datetime:
        x = datetime.strptime(value, self.date_format)
        if x is None:
            raise FailedCast()

        return x

    def perform_output_cast(self, value: datetime) -> str:
        return value.strftime(self.date_output_format)
