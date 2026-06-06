from fastapi import FastAPI

from . import models
from .database import engine
from sqlalchemy.orm import Session
from passlib.context import  CryptContext
from .database import get_db
from .routers import blog,user,authentication


app = FastAPI()

models.base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)