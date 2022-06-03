from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from routers.usuarios.main import obtener_usuarios

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "b75d41cd31ece069ca2392ea2883b37b77f19e6a268f5644b4daf91c62a36e7c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_contrasenia(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def obtener_contrasenia_hash(password):
    return pwd_context.hash(password)


def autenticar_usuario(fake_db, username: str, password: str):
    user = obtener_usuarios(fake_db, username)
    if not user:
        return False
    if not verificar_contrasenia(password, user.hashed_password):
        return False
    return user
