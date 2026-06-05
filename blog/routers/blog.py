from fastapi import APIRouter,Depends,HTTPException,status,Request,Response
from typing import List
from sqlalchemy.orm import Session
from .. import database,models,schemas
from ..main import get_db
from ..oauth2 import get_current_user
from ..repository import blog
from ..oauth2 import get_current_user

router=APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get('/',response_model=List[schemas.show_all_blogs])
def all_blogs(db:Session=Depends(get_db),current_user:schemas.user=Depends(get_current_user)):
    return blog.all_blogs(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.blog,db:Session=Depends(get_db),current_user:schemas.user=Depends(get_current_user)):
    return blog.create_blog()
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=schemas.showblog_by_id)
def blog_by_id(id,response:Response,db:Session=Depends(get_db),current_user:schemas.user=Depends(get_current_user)):
    return blog.get_blog_by_id(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db),current_user:schemas.user=Depends(get_current_user)):
    return blog.remove(db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog_id(id,request:schemas.blog,db:Session=Depends(get_db),current_user:schemas.user=Depends(get_current_user)):
    return blog.update(id,request,db)


