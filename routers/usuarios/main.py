from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils import OAuth2PasswordBearerWithCookie
from typing import List
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException, Request, responses, status, Response
from .hashing import Hasher
from sql_app.models import Usuario
from jose import jwt
from sqlalchemy.exc import IntegrityError
from config import settings

oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/login/token")

router = APIRouter(prefix="/usuarios", tags=["usuarios"])
templates = Jinja2Templates(directory="templates")

@router.get("/", tags=["usuarios"], response_model=List[schemas.Usuario])
def obtener_usuarios(db: Session = Depends(get_db)):
  usuario = db.query(models.Usuario).all()
  return usuario


@router.get("/inicio_sesion")
def login(request: Request):
    return templates.TemplateResponse("inicio_sesion.html", {"request": request})


@router.post("/login/token")
def retrieve_token_for_authenticated_user(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(Usuario).filter(Usuario.correo_de_usuario == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario incorrecto"
        )
    if not Hasher.verify_password(form_data.password, user.contraseña_encriptada):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Contraseña incorrecta"
        )
    data = {"sub": form_data.username}
    jwt_token = jwt.encode(data, settings.SECRET_KEY,
                           algorithm=settings.ALGORITHM)
    response.set_cookie(key="access_token",
                        value=f"Bearer {jwt_token}", httponly=True)
    return {"access_token": jwt_token, "token_type": "bearer"}


@router.post("/inicio_sesion")
async def login(response: Response, request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    errors = []
    if not email:
        errors.append("Por favor ingrese un correo electrónico válido")
    if not password:
        errors.append("Ingrese una contraseña")
    if len(errors) > 0:
        return templates.TemplateResponse(
            "inicio_sesion.html", {"request": request, "errors": errors}
        )
    try:
        user = db.query(Usuario).filter(Usuario.email == email).first()
        if user is None:
            errors.append("El correo electrónico no existe!!")
            return templates.TemplateResponse(
                "inicio_sesion.html", {"request": request, "errors": errors}
            )
        else:
            if Hasher.verify_password(password, user.password):
                data = {"sub": email}
                jwt_token = jwt.encode(
                    data, settings.SECRET_KEY, algorithm=settings.ALGORITHM
                )
                # if we redirect response in below way, it will not set the cookie
                # return responses.RedirectResponse("/?msg=Login Successfull", status_code=status.HTTP_302_FOUND)
                msg = "Inicio de Sesión correctamente"
                response = templates.TemplateResponse(
                    "inicio_sesion.html", {"request": request, "msg": msg}
                )
                response.set_cookie(
                    key="access_token", value=f"Bearer {jwt_token}", httponly=True
                )
                return response
            else:
                errors.append("Invalid Password")
                return templates.TemplateResponse(
                    "inicio_sesion.html", {
                        "request": request, "errors": errors}
                )
    except:
        errors.append(
            "Algo está Mail mientras te autentificabas o con tu token!")
        return templates.TemplateResponse(
            "inicio_sesion.html", {"request": request, "errors": errors}
        )


@router.get("/crear_cuenta")
def registration(request: Request):
    return templates.TemplateResponse("crear_cuenta.html", {"request": request})


@router.post("/crear_cuenta")
async def registration(request: Request, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
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