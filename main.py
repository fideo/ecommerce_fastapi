from typing import List
from urllib import request

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from dependencies import get_db
from sql_app.database import SessionLocal,Base, engine
from routers.productos import main as productos_router
from routers.categorias import main as categorias_router
from routers.usuarios import main as usuarios_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
#agregando las rutas de usuarios
app.include_router(usuarios.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
async def index(request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

templates = Jinja2Templates(directory="templates")

app.include_router(productos_router.router)

app.include_router(categorias_router.router)

app.include_router(usuarios_router.router)
