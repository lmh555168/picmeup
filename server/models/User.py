#-*-coding:utf-8-*-

from server import db
from datetime import datetime
import json
import models

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nickname=db.Column(db.String(255),nullable=False,unique=True)
    username=db.Column(db.String(255),nullable=False,unique=True)
    email=db.Column(db.String(255),nullable=True,unique=True)
    mobile=db.Column(db.String(255),nullable=True,unique=True)
    password=db.Column(db.String(512),nullable=False)
    description=db.Column(db.Text,nullable=True)
    # from where minimography weixin qq
    origin=db.Column(db.Text,nullable=True)
    # if the user from other site, the url of this author
    origin_url=db.Column(db.Text,nullable=True)
    # is this user from other site?
    is_imported = db.Column(db.Boolean,nullable=True)
    last_log_time=db.Column(db.DateTime,nullable=True)
    last_log_ip = db.Column(db.String(50),nullable=True)
    role = db.Column(db.String(255),nullable=True)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Integer, nullable=False)
    coin_num = db.Column(db.Integer,nullable=True,default=5)


    def __repr__(self):
        return json.dumps(self.serialize)

    @property
    def serialize(self):
        return {
            'id'            :   self.id,
            'username'      :   self.username,
            'nickname'      :   self.nickname,
            'description'   :   self.description,
            'last_log_time' :   models.dump_datetime(self.last_log_time),
            'created_time'  :   models.dump_datetime(self.created_time),
        }