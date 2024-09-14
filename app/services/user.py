from sqlalchemy.orm import Session

from ..models import User


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, username: str, email: str) -> User:
        user = User(username=username, email=email)
        User.save(self.session, user)
        return user

    def get_user(self, user_id: int) -> User:
        return User.get_by_id(self.session, user_id)

    def delete_user(self, user: User) -> None:
        User.delete(self.session, user)