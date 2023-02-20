from typing import Any

from utils.serializers.fields import BaseField
from utils.serializers.fields.exceptions import FailedCast


class IntegerField(BaseField):

    def perform_cast(self, value: str) -> Any:
        try:
            return int(value)
        except ValueError:
            raise FailedCast()

    def perform_output_cast(self, value: int) -> str:
        return str(value)
