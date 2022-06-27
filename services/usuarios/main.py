import hashlib
from typing import Union
from fastapi import Depends
from pydantic import BaseModel
from jose import JWTError, jwt
from dependencies import get_db
from sqlalchemy.orm import Session
from models.usuario import Usuario
from passlib.context import CryptContext
from datetime import datetime, timedelta
from schemas import usuarios as schemas_usuarios
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="usuario/token")


def verificar_contrasenia(contrasenia_base, contrasenia_encriptada):
    return hashlib.sha256(bytes(contrasenia_base, 'utf-8')).hexdigest() == contrasenia_encriptada


def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()


def obtener_varios_usuarios(db: Session, skip: int = 0, limite: int = 100):
    return db.query(Usuario).offset(skip).limit(limite).all()


def obtener_contrasenia_encriptada(contrasenia):
    return hashlib.sha256(bytes(contrasenia, 'utf-8')).hexdigest()


def obtener_usuario_por_nombre(db: Session,nombre_de_usuario: str):
    print(nombre_de_usuario)
    return db.query(Usuario).filter(Usuario.nombre_de_usuario == nombre_de_usuario).first()


def autentificar_usuario(db:Session,nombre_de_usuario: str, contrasenia: str):
    usuario = obtener_usuario_por_nombre(db, nombre_de_usuario=nombre_de_usuario)
    if not usuario:
        return False
    if not verificar_contrasenia(contrasenia, usuario.contrasenia_encriptada):
        return False
    return usuario


def crear_acceso_al_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def crear_usuario(db: Session,  user: schemas_usuarios.UsuarioCreate): 
    hashed_password = obtener_contrasenia_encriptada(user.contrasenia_encriptada)
    db_user = Usuario(nombre_de_usuario=user.nombre_de_usuario,
            correo_de_usuario=user.correo_de_usuario,
            pais = user.pais,
            ciudad = user.ciudad,
            contrasenia_encriptada=hashed_password) 
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user)
    return db_user


async def obtener_usuario_actual(db : Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
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
        token_data = schemas_usuarios.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = obtener_usuario_por_nombre(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def obtener_usuario_activo_actual(current_user: schemas_usuarios.Usuario = Depends(obtener_usuario_actual)):
    if not current_user.esta_activo:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


