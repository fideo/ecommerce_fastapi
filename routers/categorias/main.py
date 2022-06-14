from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends
from services.categorias import main as categorias_services

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.get("/crear", tags=["categorias"], response_model=List[schemas.Categoria])
def crear_categorias(categoria:schemas.Categoria, db: Session = Depends(get_db)):
    categoria = categorias_services.crear_categorias(db=db,categoria=categoria)
    return categoria

@router.get("/actualizar/{categoria_id}", tags=["categorias"], response_model=List[schemas.ActualizarCategoria])
def actualizar_categorias(categoria_id:int, categoria_actualizada:schemas.ActualizarCategoria, db: Session = Depends(get_db)):
    categoria = categorias_services.actualizar_categorias(db=db,categoria_id=categoria_id,categoria_actualizada=categoria_actualizada)
    return categoria

@router.get("/eliminar/{categoria_id}", tags=["categorias"], response_model=List[schemas.EliminarCategoria])
def eliminar_categorias(categoria_id:int, db: Session = Depends(get_db)):
    mensaje = categorias_services.eliminar_categorias(db=db,categoria_id=categoria_id)
    return mensaje
