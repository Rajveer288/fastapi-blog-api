from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/blog/{id}")
def blog(id:str):
    return {"id": id}


app.get("/blog/unpublished")
def unpublished():
    return {"data": "all Unpublished blogs"}


@app.get("/about")
def about():
    return {'about':'new project'}
@app.get("/blog")
def blog(limit=10,publish:bool=True,sort:Optional[str]=None):
    if publish:
        return {'data':f'{limit} publish blog from the list'}
    else:
        return {'data':f'{limit} blog from the list'}

class Blog(BaseModel):
    title: str
    body: str
    published:Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return request
    return {'data':f'blog is created with title as {request.title}'}

#if __name__=='__main__':
#   uvcorn.run(app,host='127.0.0.1',port=9000,reload=True)