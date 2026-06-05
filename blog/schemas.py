from pydantic import BaseModel
from typing import List,Optional

class blog(BaseModel):
    title: str
    content: str
    class Config:
        from_attributes = True


class show_all_blogs(BaseModel):
    title: str
    class Config:
        from_attributes=True

class create_user_blogs(BaseModel):
    name: str
    email: str
    password: str
class show_user(BaseModel):
    name: str
    email: str
    blog:List[blog]
    class Config:
        from_attributes=True

class user(BaseModel):
    name: str
    email: str
    class Config:
        from_attributes=True

class showblog_by_id(BaseModel):
    title: str
    content: str
    creator:user

    class Config:
        from_attributes=True

class login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


