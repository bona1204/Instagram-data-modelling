import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post=relationship(Post)
class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user=relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_to_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    user=relationship(User)
    post=relationship(Post)
    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
