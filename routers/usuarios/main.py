from dependencies import get_db
from sqlalchemy.orm import Session
from models.usuario import Usuario
from datetime import datetime, timedelta
from schemas import usuarios as usuarios_schemas
from fastapi.security import OAuth2PasswordRequestForm
from services.usuarios import main as usuarios_services
from fastapi import Depends, APIRouter, HTTPException, status

router = APIRouter(prefix="/usuario", tags=["usuario"])

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/token", response_model=usuarios_schemas.Token)
def login_para_acceder_token(db : Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = usuarios_services.autentificar_usuario(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = usuarios_services.crear_acceso_al_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/users/", response_model=usuarios_schemas.Usuario)
def crear_usuario(usuario: usuarios_schemas.UsuarioCreate, db: Session = Depends(get_db)):
     db_user = usuarios_services.obtener_usuario_por_nombre(db, nombre_de_usuario=usuario.nombre_de_usuario)
     if db_user:
         raise HTTPException(status_code=400, detail="Email or Username already registered") 
     return usuarios_services.crear_usuario(db=db, user=usuario) 

@router.get("/users/", response_model=usuarios_schemas.Usuario) 
def leer_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = usuarios_services.obtener_varios_usuarios(db, skip=skip, limit=limit) 
    return users

@router.get("/users/me/", response_model=usuarios_schemas.Usuario)
async def leer_mis_usuarios(current_user: usuarios_schemas.Usuario = Depends(usuarios_services.obtener_usuario_activo_actual)):
    return current_user

@router.get("/users/{usuario_id}", response_model=usuarios_schemas.Usuario)
def leer_un_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_user = usuarios_services.obtener_usuario(db, usuario_id=usuario_id) 
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found") 
    return 
