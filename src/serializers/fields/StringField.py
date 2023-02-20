from typing import Any

from serializers.fields import BaseField
from serializers.fields.exceptions import FailedCast


class StringField(BaseField):

    def perform_cast(self, value: str) -> Any:
        try:
            return str(value)
        except ValueError:
            raise FailedCast()
