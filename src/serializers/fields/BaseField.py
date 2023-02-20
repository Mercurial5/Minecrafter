from abc import ABC, abstractmethod
from typing import Any

from serializers.fields.exceptions import FailedCast


class BaseField(ABC):

    def __init__(self, read_only: bool = False):
        self.read_only = read_only

    def cast(self, value: Any) -> Any | None:
        try:
            return self.perform_cast(value)
        except FailedCast:
            return None

    @abstractmethod
    def perform_cast(self, value: str) -> Any:
        pass
