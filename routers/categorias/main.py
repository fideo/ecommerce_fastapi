from typing import List
from sqlalchemy.orm import Session
from schemas import categorias as categorias_schemas
from dependencies import get_db
from fastapi import APIRouter, Depends
from services.categorias import main as categorias_services

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.get("/", tags=["categorias"], response_model=List[categorias_schemas.Categoria])
def obtener_categorias(db: Session = Depends(get_db)):
    categoria = categorias_services.obtener_categorias(db)
    return categoria

@router.get("/crear", tags=["categorias"], response_model=List[categorias_schemas.Categoria])
def crear_categorias(categoria:categorias_schemas.Categoria, db: Session = Depends(get_db)):
    categoria = categorias_services.crear_categorias(db=db,categoria=categoria)
    return categoria

@router.get("/actualizar/{categoria_id}", tags=["categorias"], response_model=List[categorias_schemas.ActualizarCategoria])
def actualizar_categorias(categoria_id:int, categoria_actualizada:categorias_schemas.ActualizarCategoria, db: Session = Depends(get_db)):
    categoria = categorias_services.actualizar_categorias(db=db,categoria_id=categoria_id,categoria_actualizada=categoria_actualizada)
    return categoria

@router.get("/eliminar/{categoria_id}", tags=["categorias"], response_model=List[categorias_schemas.EliminarCategoria])
def eliminar_categorias(categoria_id:int, db: Session = Depends(get_db)):
    mensaje = categorias_services.eliminar_categorias(db=db,categoria_id=categoria_id)
    return mensaje
