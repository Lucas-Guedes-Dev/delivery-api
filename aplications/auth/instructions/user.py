from aplications import db
from aplications.auth.models import User


class IUser():
    def get_user_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def get_all_users(self):
        return User.query.all()

    def create_user(self, username, password):
        new_user = User(username=username)
        new_user.set_password(password)