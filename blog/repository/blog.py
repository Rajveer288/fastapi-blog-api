from flask import Response

from FastAPI_env.blog import models
from sqlalchemy.orm import Session
from fastapi import Depends,requests,HTTPException,status
from ..main import get_db
from .. import schemas




def all_blogs(db:Session=Depends(get_db)):
    blogs=db.query(models.blog_table).all()
    return blogs
def create_blog(request:schemas.blog,db:Session=Depends(get_db)):
    new_blog = models.blog_table(title=request.title, content=request.content, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
def get_blog_by_id(id:int,response:Response,db:Session=Depends(get_db)):
    blog = db.query(models.blog_table).filter(models.blog_table.id == id).first()
    if not blog:
        raise HTTPException(status_code=404,
                            detail=f'blog with id {id} is not available')

    return blog
def remove(db:Session=Depends(get_db)):
    blog = db.query(models.blog_table).filter(models.blog_table.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'
def update(id:int,request:schemas.blog,db:Session=Depends(get_db)):
    blog = db.query(models.blog_table).filter(models.blog_table.id == id)
    if not blog:
        raise HTTPException(status_code=404,
                            detail=f'blog with id {id} is not available')
    blog.update(request.model_dump())
    db.commit()
    return 'updated'
