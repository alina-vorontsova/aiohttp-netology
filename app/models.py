from typing import Type

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType


Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(EmailType, unique=True, nullable=False)
    password = Column(String, nullable=False)

    advertisements = relationship("Advertisement", back_populates="user")

    def __str__(self):
        f"Id: {self.id},\nEmail: {self.email}"


class Advertisement(Base):

    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False) 

    user = relationship(User, back_populates="advertisements")

    def __str__(self):
        f"Owner's id: {self.owner_id},\nTitle: {self.title},\nDescription: {self.description},\nCreation time: {self.created_at}"


ORM_MODEL = Advertisement | User
ORM_MODEL_CLS = Type[Advertisement] | Type[User]