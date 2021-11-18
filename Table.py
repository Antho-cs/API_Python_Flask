from dataclasses import dataclass
from sqlalchemy_utils import UUIDType
from conf import *

db = SQLAlchemy(app)


# Table Utilisateur
@dataclass
class User(db.Model):
    # Nom de la table
    __tablename__ = "User"

    # Les attributs de la table
    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self._first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self.email = email

    id: UUIDType(binary=False)
    first_name: str
    last_name: str
    email: str
    # Colonnes
    id = db.Column(UUIDType(binary=False), primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


# Table Friends
@dataclass
class Friends(db.Model):
    # Nom de la Table
    __tablename__ = "Friends"
    # Les attributs de la table
    user_id: UUIDType(binary=False)
    user_friend_id: UUIDType(binary=False)
    # Colonnes
    user_id = db.Column(UUIDType(binary=False), primary_key=True)
    user_friend_id = db.Column(UUIDType(binary=False), primary_key=True)
