from typing import Protocol

from minecrafter.users.models import User, UserAuthorizationKey


class UserRepositoriesProtocol(Protocol):

    @staticmethod
    def get_users(**kwargs) -> list[User]: ...

    @staticmethod
    def get_user(**kwargs) -> User: ...

    @staticmethod
    def create(data: dict) -> User: ...

    @staticmethod
    def generate_key(user: User) -> UserAuthorizationKey: ...


class UserRepositories:

    @staticmethod
    def get_users(**kwargs) -> list[User]:
        return User.objects(**kwargs)

    @staticmethod
    def get_user(**kwargs) -> User:
        users = User.objects(**kwargs)
        return None if len(users) == 0 else users[0]

    @staticmethod
    def create(data: dict) -> User:
        return User(**data).save()

    @staticmethod
    def generate_key(user: User) -> UserAuthorizationKey:
        authorization_key = UserAuthorizationKey(user=user).save()
        return authorization_key
