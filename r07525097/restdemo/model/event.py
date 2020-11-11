from datetime import datetime, timedelta

import jwt
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

from restdemo import db
from restdemo.model.base import Base


class Event(Base):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    eventtype = db.Column(db.Integer)
    eventdesc = db.Column(db.String(100))
    eventdate = db.Column(db.String(100))
    startingtime = db.Column(db.String(100))
    endingtime = db.Column(db.String(100))
    saleroles = db.Column(db.Integer)
    saleslimit = db.Column(db.Integer)
    salespermember =db.Column(db.Integer)
    # tweet = relationship('Tweet')

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
        return db.session.query(Event).filter(
            Event.username == username
        ).first()
    
    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).filter(
            User.id == user_id
        ).first()

    @staticmethod
    def get_user_list():
        return db.session.query(Event).all()

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

class EventType(Base):
    __tablename__ = 'eventtype'
    id = db.Column(db.Integer, primary_key=True)
    eventdesc = db.Column(db.String(128))

    def __repr__(self):
        return "id={}, eventtypedesc={}".format(
            self.id, self.eventtypedesc
        )

class EventTypeMapping(Base):
    __tablename__ = 'eventtypemapping'
    id = db.Column(db.Integer, primary_key=True)
    eventdesc = db.Column(db.String(128))
    eventid = db.Column(db.Integer, db.ForeignKey("event.id", ondelete="CASCADE"), nullable=False) 
    eventtypeid = db.Column(db.Integer, db.ForeignKey("eventtype.id", ondelete="CASCADE"), nullable=False) 