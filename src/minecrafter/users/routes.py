from flask import request

from decorators import serializable
from minecrafter.users import app
from minecrafter.users.serializers import UserCreateSerializer


@app.route('/', methods=['POST'])
@serializable(request, UserCreateSerializer)
def test(data: dict):
    return data
