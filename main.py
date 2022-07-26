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
from schemas import productos as productos_schemas
from schemas import categorias as categorias_schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static/"), name="static")

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
  entradas = eval(productos_schemas.ProductoCreate.schema_json())["properties"].keys()

  tipos = ["text","number","number","string",
          "number","text","text"]

  context = {
    "request":request,
    "entradas": [a for a in zip(entradas,tipos)]
  }
  return templates.TemplateResponse("crear_productos_planilla.html", context)

@app.get('/crear_categoria')
async def index(request:Request):
  entradas = eval(categorias_schemas.CategoriaCreate.schema_json())["properties"].keys()

  tipos = ["text","text"]

  print(str(request.url.path))

  context = {
    "request":request,
    "entradas": [a for a in zip(entradas,tipos)],
    "url": str(request.url.path)
  }
  return templates.TemplateResponse("crear_categoria.html", context)

templates = Jinja2Templates(directory="templates")

app.include_router(productos_router.router)
app.include_router(categorias_router.router)
app.include_router(usuarios_router.router)
app.include_router(ventas_router.router)

