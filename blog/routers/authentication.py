from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models,token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..hashing import hash
from datetime import timedelta


router = APIRouter(
    prefix="/login",
    tags=["login"]
)

@router.post('/')
def verify(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
    user=db.query(models.user_table).filter(models.user_table.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")
    if not hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}

