import re
from http import HTTPStatus
from typing import Union

from flask import request
from mongoengine.errors import NotUniqueError

from minecrafter.users import app
from minecrafter.users.models import User
from minecrafter.users.serializers import UserCreateSerializer, UserOutputSerializer
from minecrafter.users.services import UserService
from utils.decorators import serializable


@app.route('/', endpoint='list_users', methods=['GET'])
@serializable(request, output_serializer_class=UserOutputSerializer)
def list_users():
    service = UserService()
    users = service.get_users()

    return users, HTTPStatus.OK


@app.route('/', endpoint='create_user', methods=['POST'])
@serializable(request, input_serializer_class=UserCreateSerializer, output_serializer_class=UserOutputSerializer)
def create_user(data: dict) -> tuple[Union[dict, User], int]:
    service = UserService()

    try:
        user = service.create(data)
    except NotUniqueError as e:
        duplicate_field = re.search(r'(?<=index: )(.*?)(?=_\d+ dup key)', str(e)).group()
        return {duplicate_field: f'User with this {duplicate_field} already exists'}, HTTPStatus.BAD_REQUEST

    return user, HTTPStatus.CREATED
