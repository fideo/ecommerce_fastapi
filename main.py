from typing import List
from urllib import request

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_app import crud,models,schemas
from routers.categorias import main as categorias
from routers.productos import main as productos
from routers.usuarios import main as usuarios
from admin.routers.categorias import main as adminCategorias
from admin.routers.productos import main as adminProductos
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from dependencies import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

#agregando las rutas de categorias
app.include_router(categorias.router, tags=["categorias"])
app.include_router(adminCategorias.router, tags=["categorias"])
app.include_router(usuarios.router, tags=["usuarios"])

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def index(request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

@app.get('/productos/')
def mostrar_productos(db: Session = Depends(get_db)):
    producto = productos.obtener_productos(db=db)
    context = {
        "productos": producto
    }
    return context


@app.post('/crear_productos/', response_model=schemas.ProductoBase)
def crear_producto(producto:schemas.ProductoBase, db: Session = Depends(get_db)):
    return adminProductos.crear_producto(producto=producto, db=db)

@app.get('/usuarios/')
def mostrar_usuarios(db: Session = Depends(get_db)):
    usuario = usuarios.obtener_usuarios(db=db)
    context = {
        "categorias": usuario
    }
    return context


@app.post("/crear_vendedor",response_model=schemas.Vendedor)
async def crear_vendedor(
    correo_de_vendedor:str,
    pais:str,
    nombre:str,
    ciudad:str,
    contraseña_encriptada:str,
    db: Session = Depends(get_db)
):
    return crud.crear_vendedor(db=db,nombre=nombre,pais=pais,ciudad=ciudad,
                            correo_de_vendedor=correo_de_vendedor,contraseña_encriptada=contraseña_encriptada)

@app.post("/crear_producto/",response_model=schemas.ProductoBase)
async def crear_producto_nuevo(
    vendedor_id: int,
    producto:schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_producto(db=db,producto=producto,vendedor_id=vendedor_id)

@app.get("/buscar_producto")
async def buscar_producto(palabra_clave:str,db: Session = Depends(get_db)):
    return crud.buscar_producto(db=db,palabra_clave=palabra_clave)
