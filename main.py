from typing import List
from urllib import request

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_app import crud,models,schemas
from routers.categorias import main 
from admin.routers.categorias import main as adminCategorias
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session
from dependencies import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def index(request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

@app.get('/categorias/')
def mostrar_categorias(db: Session = Depends(get_db)):
    categoria = main.obtener_categorias(db=db)
    context = {
        "categorias": categoria
    }
    return context

@app.post('/categorias/', response_model=schemas.Categoria)
def crear_categoria(categoria:schemas.Categoria, db: Session = Depends(get_db)):
    return adminCategorias.crear_categorias(categoria=categoria, db=db)


@app.post('/eliminar_categorias/{categoria_id}', response_model=schemas.EliminarCategoria)
def eliminar_categorias(categoria_id: int, db: Session = Depends(get_db)):
    return adminCategorias.eliminar_categorias(categoria_id=categoria_id, db=db)


@app.post('/actualizar_categoria/{categoria_id}', response_model=schemas.ActualizarCategoria)
def actualizar_categoria(categoria_id: int, categoria_actualizada:schemas.ActualizarCategoria, db: Session = Depends(get_db)):
    return adminCategorias.actualizar_categorias(categoria_id=categoria_id, categoria_actualizada=categoria_actualizada,  db=db)

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
                            correo_de_vendedor=correo_de_vendedor,contrase_encriptada=contraseña_encriptada)

@app.post("/productos/{vendedor_id}/",response_model=schemas.Producto)
async def crear_producto_nuevo(
    vendedor_id: int,
    producto:schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_producto(db=db,producto=producto,vendedor_id=vendedor_id)

@app.get("/buscar_producto",response_model=schemas.Producto)
async def buscar_producto(palabra_clave:str,db: Session = Depends(get_db)):
    return crud.buscar_producto(db=db,palabra_clave=palabra_clave)
