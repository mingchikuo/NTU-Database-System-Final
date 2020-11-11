from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from restdemo.model.user import User as UserModel
from restdemo.model.tweet import Tweet as TweetModel

import datetime, time


class Tweet(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'event_id', type=int,
        help='event_id required'
    )
    parser.add_argument(
        'ticket_num', type=int,
        help='ticket_num required'
    )
    parser.add_argument(
        'startingtime', type=str,
        help='event_id required'
    )
    parser.add_argument(
        'endingtime', type=str,
        help='event_id required'
    )


    # @jwt_required()
    def post(self, username):
        # if current_identity.username != username:
        #     return {'message': 'please use the right token'}
        user = UserModel.get_by_username(username)
        if not user:
            return {'message': 'user not found'}, 404
        data = Tweet.parser.parse_args()
        tweet = TweetModel(event_id=data['event_id'], user_id=user.id, ticket_num=data['ticket_num'])
        tweet.add()
        return tweet.as_dict()

    def get(self, username):
        data = Tweet.parser.parse_args()
        user_id = username
        startingtime = data['startingtime']
        endingtime = data['endingtime']
        users = TweetModel.get_user_list(startingtime, endingtime)

        return [u.as_dict() for u in users if u.user_id==username]
    
    def delete(self, username):

        user = TweetModel.get_by_id(username)
        if user:
            user.delete()
            return {'message': 'sale deleted'}
        else:
            return {'message': 'sale not found'}, 400    

class TweetList(Resource):
    # @jwt_required()
    def get(self):
        data = Tweet.parser.parse_args()
        startingtime = data['startingtime']
        endingtime = data['endingtime']
        users = TweetModel.get_user_list(startingtime, endingtime)

        return [u.as_dict() for u in users]