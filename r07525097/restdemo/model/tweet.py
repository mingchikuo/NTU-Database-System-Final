
from sqlalchemy import ForeignKey, func

from restdemo import db
from restdemo.model.base import Base


class Tweet(Base):

    sales_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    event_id = db.Column(db.Integer, ForeignKey('event.id'))
    ticket_num = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())

    def __repr__(self):
        return "user_id={}, event_id={}".format(
            self.user_id, self.event_id
        )

    def as_dict(self):
       t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
       t['created_at'] = t['created_at'].isoformat()
       return t

    @staticmethod
    def get_by_id(sales_id):
        return db.session.query(Tweet).filter(
            Tweet.sales_id == sales_id
        ).first()

    # @staticmethod
    # def get_user_list(startingtime, endingtime):
    #     return db.session.query(Tweet).filter(
    #         and_(Tweet.created_at <= endingtime, Tweet.created_at >= startingtime)
    #     )

    @staticmethod
    def get_user_list(startingtime, endingtime):
        return db.session.query(Tweet).filter(Tweet.created_at.between(startingtime, endingtime))
