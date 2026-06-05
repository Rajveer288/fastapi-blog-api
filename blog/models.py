from .database import base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class blog_table(base):
    __tablename__='blog'

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    content=Column(String)

    user_id=Column(Integer,ForeignKey('user.id'))

    creator=relationship('user_table',back_populates='blog')

class user_table(base):
    __tablename__='user'

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)

    blog=relationship('blog_table',back_populates='creator')