from datetime import datetime, timedelta

import jwt
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

from restdemo import db
from restdemo.model.base import Base


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    roles = db.Column(db.Integer)
    roledesc = db.Column(db.String(128))
    tweet = relationship('Tweet')

    def __repr__(self):
        return "id={}, username={}".format(
            self.id, self.username
        )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @staticmethod
    def get_by_username(username):
        return db.session.query(User).filter(
            User.username == username
        ).first()
    
    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).filter(
            User.id == user_id
        ).first()

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()

    @staticmethod
    def authenticate(username, password):
        user = User.get_by_username(username)
        if user:
            # check password
            if user.check_password(password):
                return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = User.get_by_id(user_id)
        return user

class UserType(Base):
    __tablename__ = 'usertype'
    id = db.Column(db.Integer, primary_key=True)
    roledesc = db.Column(db.String(128))

    def __repr__(self):
        return "id={}, roledesc={}".format(
            self.id, self.roledesc
        )

class UserTypeMapping(Base):
    __tablename__ = 'usertypemapping'
    id = db.Column(db.Integer, primary_key=True)
    roledesc = db.Column(db.String(128))
    userid = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False) 
    usertypeid = db.Column(db.Integer, db.ForeignKey("usertype.id", ondelete="CASCADE"), nullable=False) 
    
    
    