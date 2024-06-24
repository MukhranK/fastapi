from typing import Optional,List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, utils
from .database import engine, get_db
# from .schemas import PostCreate, Post, UserCreate, UserOut

from .routers import user, post, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

 

while True:
    try:
        conn = psycopg2.connect(host='localhost', database = 'fastapi', user = 'postgres',
                                password = 'redsea', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("connection succesfully")
        break
    except Exception as error:
        print("Failed to connect")
        print("Error: ", error)
        time.sleep(2)    



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World dato!!!!! "}








    

#uvicorn app.main:app --reload