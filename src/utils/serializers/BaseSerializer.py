from inspect import getmembers

from utils.serializers.exceptions import NotValidated
from utils.serializers.fields import BaseField


class BaseSerializer:

    def __init__(self, data: dict):
        self.fields = {field[0]: field[1] for field in getmembers(self) if isinstance(field[1], BaseField)}
        self.is_valid = False
        self._validated_data = None

        self.data = data

    def validate(self) -> dict:
        validated_data = dict()

        field_serializer: BaseField
        for field_name, field_serializer in self.fields.items():
            if field_serializer.read_only:
                continue

            if field_name not in self.data:
                return dict(status=False, description=f'`{field_name}` is not given')

            casted = field_serializer.cast(self.data[field_name])
            if not casted:
                return dict(status=False,
                            description=f'`{field_name}` could not be casted to {field_serializer.__class__.__name__}')

            validated_data[field_name] = casted

        self.is_valid = True
        self._validated_data = validated_data

        return dict(status=True)

    @property
    def validated_data(self) -> dict:
        if self.is_valid is None:
            raise NotValidated('Data is not valid. Maybe `validate` was not called')
        return self._validated_data
