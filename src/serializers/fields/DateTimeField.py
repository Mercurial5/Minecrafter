from datetime import datetime

from serializers.fields import BaseField
from serializers.fields.exceptions import FailedCast


class DateTimeField(BaseField):

    def __init__(self, date_format: str, read_only: bool = False):
        super().__init__(read_only)
        self.date_format = date_format

    def perform_cast(self, value: str) -> datetime:
        x = datetime.strptime(value, self.date_format)
        if x is None:
            raise FailedCast()

        return x
