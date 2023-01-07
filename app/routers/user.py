from .. import models, schemas, utils
from .. database import get_db
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# CREATE USER PATH OPERATIONS

# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):

    #hashing the password
    hashed_password =utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # similar to RETURNING *

    return new_user



#GET USER INFO BY id
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id : int, db:Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")
    
    return user
