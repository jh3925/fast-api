#This file is used to verify the types of the data being passed to the database

#TODO: Add password hashing via OAuth2

import pydantic as Pydantic
import datetime as DateTime

class BaseUser(Pydantic.BaseModel):
    username: str
    email: str

class User(BaseUser):
    id: int
    date_created: DateTime.datetime

    class Config:
        orm_mode = True

class CreateUser(BaseUser):
    password: str

class BaseMessage(Pydantic.BaseModel):
    text: str

class Message(BaseMessage):
    id: int
    date_created: DateTime.datetime

    class Config:
        orm_mode = True

class CreateMessage(BaseMessage):
    user_id: int


class Token(Pydantic.BaseModel):
    access_token: str
    token_type: str

class TokenData(Pydantic.BaseModel):
    username: str | None = None