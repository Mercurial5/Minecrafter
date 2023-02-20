from http import HTTPStatus
from typing import Callable, Type

from flask import Request

from utils.serializers import InputSerializer, OutputSerializer


def jsonable(request: Request) -> Callable:
    def jsonable_inner(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if request.is_json:
                return func(*args, **kwargs)

            return dict(description='To access this endpoint, you need to pass json.'), HTTPStatus.BAD_REQUEST

        return wrapper

    return jsonable_inner


def serializable(request: Request, input_serializer_class: Type[InputSerializer] = None,
                 output_serializer_class: Type[OutputSerializer] = None) -> Callable:
    def serializable_inner(func: Callable) -> Callable:
        @jsonable(request)
        def wrapper(*args, **kwargs):
            if input_serializer_class is not None:
                serializer = input_serializer_class(data=request.json)
                validation = serializer.validate()
                status = validation.pop('status')

                if not status:
                    return validation, HTTPStatus.BAD_REQUEST
                validated_data = serializer.validated_data
                result, status = func(validated_data, *args, **kwargs)
            else:
                result, status = func(*args, **kwargs)

            if output_serializer_class is not None and not isinstance(result, dict):
                serializer = output_serializer_class(validated_data=result)
                result = serializer.prepare_output()

            return result, status

        return wrapper

    return serializable_inner
