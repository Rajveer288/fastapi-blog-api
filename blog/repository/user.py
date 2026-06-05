from passlib.context import CryptContext
from .. import schemas,models
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException
from ..database import get_db

pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")

def create(request:schemas.create_user_blogs,db:Session=Depends(get_db)):
    hashed_passwd=pwd_cxt.hash(request.password)
    new_user = models.user_table(name=request.name, email=request.email, password=hashed_passwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session=Depends(get_db)):
    new_user = db.query(models.user_table).filter(models.user_table.id == id).first()
    if not new_user:
        raise HTTPException(status_code=404,
                            detail=f'user with id {id} is not available')
    return new_user
