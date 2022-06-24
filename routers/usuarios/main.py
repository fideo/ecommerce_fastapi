from typing import List
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends, Request, responses, status
from .hashing import Hasher
from sql_app.models import Usuario
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/usuarios", tags=["usuarios"])
templates = Jinja2Templates(directory="templates")

@router.get("/", tags=["usuarios"], response_model=List[schemas.Usuario])
def obtener_usuarios(db: Session = Depends(get_db)):
  usuario = db.query(models.Usuario).all()
  return usuario


@router.get("/inicio_sesion")
def login(request: Request):
    return templates.TemplateResponse("inicio_sesion.html", {"request": request})


@router.get("/crear_cuenta")
def registration(request: Request):
    return templates.TemplateResponse("crear_cuenta.html", {"request": request})


@router.post("/crear_cuenta")
async def registration(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    pais = form.get("pais")
    ciudad= form.get("ciudad")
    errors = []
    if not password or len(password) < 6:
        errors.append("La contraseña debería ser mayor a 6 caracteres")
    if not email:
        errors.append("Email no puede ser blanco")
    user = Usuario(correo_de_usuario=email, contraseña_encriptada=Hasher.get_hash_password(password))
    if len(errors) > 0:
        return templates.TemplateResponse(
            "crear_cuenta.html", {"request": request, "errors": errors}
        )
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return responses.RedirectResponse(
            "/?msg=rigistrado exitosamente", status_code=status.HTTP_302_FOUND
        )
    except IntegrityError:
        errors.append("Correo electrónico duplicado")
        return templates.TemplateResponse(
            "crear_cuenta.html", {"request": request, "errors": errors}
        )