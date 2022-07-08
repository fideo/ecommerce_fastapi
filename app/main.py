import sys

sys.path.append("app")
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
from routers.ventas import main as ventas_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get('/')
async def index(request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

@app.get('/explorando_por_categoria/{categoria_id}')
async def index(categoria_id:int,request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

@app.get('/productos_buscados')
async def index(palabra_clave:str,request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

@app.get('/crear_producto')
async def index(request:Request):
  entradas = ["nombre_producto",
          "numero_de_productos_subidos","stock","link_de_imagen",
          "precio_unitario_de_producto","descripcion","categorias"]
  tipos = ["text","number","number","string","number","text","text"]
  context = {
    "request":request,
    "entradas": [a for a in zip(entradas,tipos)]
  }
  return templates.TemplateResponse("endpoints_producto/crear_productos_planilla.html", context)

templates = Jinja2Templates(directory="app/templates")

app.include_router(productos_router.router)

app.include_router(categorias_router.router)

app.include_router(usuarios_router.router)

app.include_router(ventas_router.router)
