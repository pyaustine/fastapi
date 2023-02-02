from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint



#Pydatic model/Schema

#USER REGISTRATION MODEL

# CREATE

class UserCreate(BaseModel):
    email : EmailStr
    password : str

# RESPONSE

class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime

    class Config:
        orm_mode = True


#POSTS PYDANTIC SCHEMA

#CREATING POST MODEL

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

#RESPONSE MODEL

class Post(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserOut
# Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict,
# but an ORM model (or any other arbitrary object with attributes).
    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post : Post
    votes : int

    class Config:
        orm_mode = True



#USER LOGIN AUTH

class UserLogin(BaseModel):
    email : EmailStr
    password : str


#SCHEMA FOR ACCESS TOKEN
class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str] = None


#VOTE SCHEMA

class Vote(BaseModel):
    post_id : int
    dir: conint(le=1)