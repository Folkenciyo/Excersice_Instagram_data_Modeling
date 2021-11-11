import os
import sys
from sqlalchemy import Column, Table, Enum,ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

""" SE HACE ASÍ"""

""" follower = Table('follower',
    Column('user_from_id', Integer, ForeignKey('person.id'), primary_key=True),
    Column('user_to_id', Integer, ForeignKey('person.id'), primary_key=True)
) """

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)



""" Así no se hace, pero es solo para q salga en la preview, sabemos que el id está muy mal puesto pero es necesario para terminar de pintarlo"""
class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table Follower.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('person.id'))
    user_to_id = Column(Integer, ForeignKey('person.id'))


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table Comment.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(300), nullable=True)
    author_id = Column(Integer, ForeignKey('person.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table Post.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('person.id'))


class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type_of_media = Column(Enum, nullable=False)
    url = Column(String(500), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e