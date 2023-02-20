from inspect import getmembers

from utils.serializers.fields import BaseField


class OutputSerializer:

    def __init__(self, validated_data: dict):
        self.fields = {field[0]: field[1] for field in getmembers(self) if isinstance(field[1], BaseField)}
        self.validated_data = validated_data

    def prepare_output(self) -> dict | list:
        if isinstance(self.validated_data, dict):
            return self._prepare_item_output(self.validated_data)

        return self._prepare_list_output()

    def _prepare_list_output(self) -> list[dict]:
        return [self._prepare_item_output(data) for data in self.validated_data]

    def _prepare_item_output(self, validated_data: dict) -> dict:
        output_data = dict()

        field_class: BaseField
        for field_name, field_class in self.fields.items():
            output_data[field_name] = field_class.cast(validated_data[field_name], output=True)

        return output_data
