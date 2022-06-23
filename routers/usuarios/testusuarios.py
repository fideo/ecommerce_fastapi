from datetime import datetime, timedelta
from typing import Union, List

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
import hashlib

from dependencies import get_db
from sqlalchemy.orm import Session
from models import usuario as usermod
from services.usuario import crud
from schemas import usuarios as userschem

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuario/token")

router = APIRouter(prefix="/usuario", tags=["usuario"])

def verify_password(plain_password, hashed_password):
    return hashlib.sha256(bytes(plain_password, 'utf-8')).hexdigest() == hashed_password

def get_user(db: Session, user_id: int):
     return db.query(usermod.Usuario).filter(usermod.Usuario.id == user_id).first()


def authenticate_user(db: Session, username: str, password: str):
    user =crud.get_user_by_username(db, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: userschem.Usuario = Depends(get_current_user)):
    if not current_user.esta_activo:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token", response_model=Token)
def login_for_access_token(db : Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/users/", response_model=userschem.Usuario)
def create_user(user: userschem.UsuarioCreate, db: Session = Depends(get_db)):
     db_user = crud.get_user_by_username(db, username=user.username)
     if db_user:
         raise HTTPException(status_code=400, detail="Email or Username already registered") 
     return crud.create_user(db=db, user=user) 

@router.get("/users/", response_model=List[userschem.Usuario]) 
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit) 
    return users

@router.get("/users/me/", response_model=userschem.Usuario)
async def read_users_me(current_user: userschem.Usuario = Depends(get_current_active_user)):
    return current_user

@router.get("/users/{user_id}", response_model=userschem.Usuario)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id) 
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found") 
    return db_user