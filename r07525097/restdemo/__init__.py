from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT

db = SQLAlchemy()

from restdemo.model.user import User as UserModel
from restdemo.model.event import Event as EventModel
from restdemo.resource.user import User, UserList, UserType
from restdemo.resource.hello import Helloworld
from restdemo.resource.tweet import Tweet, TweetList
from restdemo.resource.event import Event, EventList, EventType
from restdemo.config import Config

jwt = JWT(None, UserModel.authenticate, UserModel.identity)


def create_app():

    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/signup/<string:username>')
    api.add_resource(UserList, '/users')
    api.add_resource(Tweet, '/deletesale/<string:username>','/buyTicket/<string:username>','/sales/<int:username>')
    api.add_resource(Event, '/event/<string:username>', '/modifyevent/<string:username>')
    api.add_resource(EventList, '/getallevent')
    api.add_resource(UserType, '/membertype/<string:username>')
    api.add_resource(EventType, '/eventtype/<string:username>')
    api.add_resource(TweetList, '/getsales')
    return app
