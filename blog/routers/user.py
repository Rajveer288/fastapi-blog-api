from fastapi import APIRouter,status,responses,Depends,HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import schemas,database,models
from ..database import get_db
from ..repository import user

router=APIRouter(
    prefix="/user",
    tags=['user']
)

pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.create_user_blogs,
                db:Session=Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.show_user)
def show_user(id:int,db:Session=Depends(get_db)):
    return user.get(id,db)