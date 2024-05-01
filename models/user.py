#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from squalchemy.orm import relationship

#class User(BaseModel):
#    """This class defines a user by various attributes"""
#    email = ''
#    password = ''
#    first_name = ''
#    last_name = ''

class user(Base):
    __tablename__ = 'user'
    email = Column(String(128), nullable = False)
    password = Column(String(128), nullable = False)
    first_name = Column(String(128), nullable = True)
    last_name = Column(String(128), nullable = True)

    places = relationship('place', backref = 'user', cascade = 'all, delete-orphan')
    reviews = relationship('Review', backref = 'user', cascade = 'all, delete-orphan')
