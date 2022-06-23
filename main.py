from typing import List
from urllib import request

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
<<<<<<< HEAD
from sql_app import crud,models,schemas
from routers.categorias import main as categorias
from routers.productos import main as productos
from routers.usuarios import usuarios
from admin.routers.categorias import main as adminCategorias
from admin.routers.productos import main as adminProductos
from sql_app.database import SessionLocal, engine
=======
from sql_app.database import SessionLocal,Base, engine
>>>>>>> her204-test-branch
from sqlalchemy.orm import Session
from dependencies import get_db
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

<<<<<<< HEAD
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
=======
>>>>>>> her204-test-branch
