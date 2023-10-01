from pydantic import BaseModel, EmailStr
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class User(BaseModel):
    email: EmailStr
    password: str


class NewUserResponse(BaseModel):
    email: EmailStr
