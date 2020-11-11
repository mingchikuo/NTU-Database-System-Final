from flask_restful import Resource, reqparse
from flask import request, current_app
from flask_jwt import jwt_required

from restdemo.model.event import Event as EventModel


def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception('password required')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("String must be at least %i characters long" % min_length)
    return validate


class Event(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        'eventtype', type=int, required=True, help='required eventType'
    )
    parser.add_argument(
        'eventdesc', type=str, required=True,
        help='{error_msg}'
    )
    parser.add_argument(
        'eventdate', type=str, required=True,
        help='{error_msg}'
    )
    parser.add_argument(
        'startingtime', type=str, required=True,
        help='{error_msg}'
    )
    parser.add_argument(
        'endingtime', type=str, required=True,
        help='{error_msg}'
    )
    parser.add_argument(
        'saleroles', type=int, required=True, help='required saleroles'
    )
    parser.add_argument(
        'saleslimit', type=int, required=True, help='required saleslimit'
    )
    parser.add_argument(
        'salespermember', type=int, required=True, help='required salespermember'
    )
    parser.add_argument(
        'changename', type=str, required=False, help='required salespermember'
    )



    def get(self, username):
        """
        get user detail information
        """
        user = EventModel.get_by_username(username)
        if user:
            return user.as_dict()
        return {'message': 'event not found'}, 404

    def post(self, username):
        """ create a user"""
        data = Event.parser.parse_args()
        user = EventModel.get_by_username(username)
        if user:
            return {'message': 'event already exist'}
        user = EventModel(
            username=username,
            eventtype=data['eventtype'],
            eventdesc=data['eventdesc'],
            eventdate=data['eventdate'],
            startingtime=data['startingtime'],
            endingtime=data['endingtime'],
            saleroles=data['saleroles'],
            saleslimit=data['saleslimit'],
            salespermember=data['salespermember']
        )

        user.add()
        return user.as_dict(), 201
    
    def delete(self, username):
        """delete user"""
        user = EventModel.get_by_username(username)
        if user:
            user.delete()
            return {'message': 'event deleted'}
        else:
            return {'message': 'event not found'}, 204
    
    def put(self, username):
        """update user"""
        user = EventModel.get_by_username(username)
        if user:
            data = Event.parser.parse_args()
            # user.password_hash = data['password']
            user.username=data['changename']
            user.eventtype=data['eventtype']
            user.eventdesc=data['eventdesc']
            user.eventdate=data['eventdate']
            user.startingtime=data['startingtime']
            user.endingtime=data['endingtime']
            user.saleroles=data['saleroles']
            user.saleslimit=data['saleslimit']
            user.salespermember=data['salespermember']
            
            user.update()
            return user.as_dict()
        else:
            return {'message': "event not found"}, 204    


class EventList(Resource):

    # @jwt_required()
    def get(self):
        users = EventModel.get_user_list()
        return [u.as_dict() for u in users]

class GetOneEvent(Resource):

    # @jwt_required()
    def get(self):
        users = EventModel.get_user_list()
        return [u.as_dict() for u in users]


class EventType(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument(
        'eventtypedesc', type=str, required=True, help='required eventtypedesc'
    )

    def put(self, username):
        """update user"""
        user = EventModel.get_by_username(username)
        if user:
            data = EventType.parser.parse_args()
            user.eventdesc = data['eventtypedesc']
            user.update()
            return user.as_dict()
        else:
            return {'message': "user not found"}, 204  
    