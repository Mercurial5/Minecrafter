from typing import Protocol

from minecrafter.users.models import User


class UserRepositoriesProtocol(Protocol):

    @staticmethod
    def get_users(**kwargs) -> list[User]: ...

    @staticmethod
    def get_user(**kwargs) -> User: ...

    @staticmethod
    def create(data: dict) -> User: ...


class UserRepositories:

    @staticmethod
    def get_users(**kwargs) -> list[User]:
        return User.objects(**kwargs)

    @staticmethod
    def get_user(**kwargs) -> User:
        return User.objects(**kwargs)

    @staticmethod
    def create(data: dict) -> User:
        return User(**data).save()
