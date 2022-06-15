from typing import List
from sqlalchemy.orm import Session
#from sql_app import models, schemas
from models.categoria import Categoria
from schemas import categorias as categorias_schemas
from dependencies import get_db
from fastapi import Depends


def obtener_categorias(db: Session = Depends(get_db)):
    categoria = db.query(Categoria).all()
    return categoria


def crear_categorias(categoria:categorias_schemas.Categoria, db: Session = Depends(get_db)):
    categoria = Categoria(
        nombre_categoria = categoria.nombre_categoria,
        descripcion = categoria.descripcion,
        esta_activo = categoria.esta_activo
    )
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria


def actualizar_categorias(categoria_id:int, categoria_actualizada:categorias_schemas.ActualizarCategoria, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter_by(categoria_id=categoria_id).first()
    print(categoria_id)
    categoria.nombre_categoria = categoria_actualizada.nombre_categoria
    categoria.descripcion = categoria_actualizada.descripcion
    categoria.esta_activo = categoria_actualizada.esta_activo
    db.commit()
    db.refresh(categoria)
    return categoria


def eliminar_categorias(categoria_id:int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter_by(categoria_id=categoria_id).first()
    db.delete(categoria)
    db.commit()
    mensaje= categorias_schemas.EliminarCategoria(mensaje="La categoria "+ str(categoria_id) +" ha sido eliminada correctamente",categoria_id=categoria_id)
    return mensaje
