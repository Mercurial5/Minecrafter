from flask import Blueprint

app = Blueprint('users', __name__)

from minecrafter.users import routes
