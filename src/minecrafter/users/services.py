from typing import Protocol

from minecrafter.users.models import User, UserAuthorizationKey
from minecrafter.users.repositories import UserRepositories
from minecrafter.users.repositories import UserRepositoriesProtocol


class UserServicesProtocol(Protocol):
    repo: UserRepositoriesProtocol

    def get_users(self, **kwargs) -> list[User]: ...

    def get_user(self, **kwargs) -> User: ...

    def create(self, data: dict) -> User: ...

    def generate_key(self, user: User) -> UserAuthorizationKey: ...


class UserService:
    repo: UserRepositoriesProtocol = UserRepositories()

    def get_users(self, **kwargs) -> list[User]:
        return self.repo.get_users(**kwargs)

    def get_user(self, **kwargs) -> User:
        return self.repo.get_user(**kwargs)

    def create(self, data: dict) -> User:
        return self.repo.create(data)

    def generate_key(self, user: User) -> UserAuthorizationKey:
        return self.repo.generate_key(user)
