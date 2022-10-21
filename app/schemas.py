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
    pass
