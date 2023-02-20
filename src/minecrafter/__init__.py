from flask import Flask

from minecrafter.users import app as users_app


def create_app() -> Flask:
    app = Flask(__name__)

    applications = [users_app]

    for application in applications:
        app.register_blueprint(application, url_prefix=f'/{application.name}')

    return app
