from typing import Any

from utils.serializers.fields import BaseField
from utils.serializers.fields.exceptions import FailedCast


class StringField(BaseField):

    def perform_cast(self, value: str) -> Any:
        try:
            return str(value)
        except ValueError:
            raise FailedCast()

    def perform_output_cast(self, value: str) -> str:
        return str(value)
