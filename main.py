from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_app import crud,models,schemas
from sql_app.database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def index(request: Request):
  context = {
    "request": request,
  }
  return templates.TemplateResponse("index.html", context)

@app.post("/crear_vendedor",response_model=schemas.VendedorCreate)
async def crear_vendedor(
    correo_de_vendedor:str,pais:str,nombre:str,
    ciudad:str,constraseña_encriptada:str,
    db: Session = Depends(get_db)
):
    return crud.crear_vendedor(db=db,nombre=nombre,pais=pais,ciudad=ciudad,
                            correo_de_vendedor=correo_de_vendedor,contraseña_encriptada=contraseña_encriptada)

@app.post("/productos/{vendedor_id}/",response_model=schemas.ProductoCreate)
async def crear_producto_nuevo(
    vendedor_id: int,
    producto:schemas.ProductoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_producto(db=db,producto=producto,vendedor_id=vendedor_id)

@app.get("/buscar_producto")
async def buscar_producto(palabra_clave:str,db: Session = Depends(get_db)):
    return crud.buscar_producto(db=db,palabra_clave=palabra_clave)
