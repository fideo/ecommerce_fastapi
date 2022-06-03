from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/categorias", tags=["categorias"])

@router.get("/", tags=["categorias"], response_model=List[schemas.Categoria])
def crear_categorias(categoria:schemas.Categoria, db: Session = Depends(get_db)):
    categoria = models.Categoria(
        nombre_categoria = categoria.nombre_categoria,
        descripcion = categoria.descripcion,
        esta_activo = categoria.esta_activo
    )
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

@router.get("/{categoria_id}", tags=["categorias"], response_model=List[schemas.ActualizarCategoria])
def actualizar_categorias(categoria_id:int, categoria_actualizada:schemas.ActualizarCategoria, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter_by(categoria_id=categoria_id).first()
    print(categoria_id)
    categoria.nombre_categoria = categoria_actualizada.nombre_categoria
    categoria.descripcion = categoria_actualizada.descripcion
    categoria.esta_activo = categoria_actualizada.esta_activo
    db.commit()
    db.refresh(categoria)
    return categoria

@router.get("/{categoria_id}", tags=["categorias"], response_model=List[schemas.EliminarCategoria])
def eliminar_categorias(categoria_id:int, db: Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter_by(categoria_id=categoria_id).first()
    db.delete(categoria)
    db.commit()
    mensaje= schemas.EliminarCategoria(mensaje="La categoria "+ str(categoria_id) +" ha sido eliminada correctamente",categoria_id=categoria_id)
    return mensaje
