from http import HTTPStatus
from typing import Callable, Type

from flask import Request

from serializers import BaseSerializer


def jsonable(request: Request) -> Callable:
    def jsonable_inner(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if request.is_json:
                return func(*args, **kwargs)

            return dict(description='To access this endpoint, you need to pass json.'), HTTPStatus.BAD_REQUEST

        return wrapper

    return jsonable_inner


def serializable(request: Request, input_serializer_class: Type[BaseSerializer]) -> Callable:
    def serializable_inner(func: Callable) -> Callable:
        @jsonable(request)
        def wrapper(*args, **kwargs):
            serializer = input_serializer_class(data=request.json)
            validation = serializer.validate()
            status = validation.pop('status')

            if not status:
                return validation, HTTPStatus.BAD_REQUEST

            result = func(serializer.validated_data, *args, **kwargs)

            return result, HTTPStatus.OK

        return wrapper

    return serializable_inner
