from abc import ABC, abstractmethod
from typing import Any

from utils.serializers.fields.exceptions import FailedCast


class BaseField(ABC):

    def cast(self, value: Any, output: bool = False) -> Any | None:
        try:
            if output:
                return self.perform_output_cast(value)

            return self.perform_cast(value)
        except FailedCast:
            return None

    @abstractmethod
    def perform_cast(self, value: str) -> Any:
        pass

    @abstractmethod
    def perform_output_cast(self, value: Any) -> str:
        pass
