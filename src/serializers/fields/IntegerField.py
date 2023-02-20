from typing import Any

from serializers.fields import BaseField
from serializers.fields.exceptions import FailedCast


class IntegerField(BaseField):

    def perform_cast(self, value: str) -> Any:
        try:
            return int(value)
        except ValueError:
            raise FailedCast()
