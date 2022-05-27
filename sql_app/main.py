from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from . import crud, models, schemas
from main import app
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

@app.get('/categorias', response_model=List[schemas.Categoria])
def mostrar_categorias(db:Session = Depends(get_db)):
    categoria = crud.obtener_categorias(db)
    return categoria

@app.post('/categorias', response_model=schemas.Categoria)
def crear_categorias(categoria:schemas.Categoria, db:Session = Depends(get_db)):
    categoria = models.Categoria(
        nombre_categoria = categoria.nombre_categoria,
        descripcion = categoria.descripcion,
        esta_activo = categoria.esta_activo
    )
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

@app.put('/categorias/{categoria_id}', response_model=schemas.ActualizarCategoria)
def actualizar_categorias(categoria_id:int, categoria_actualizada:schemas.ActualizarCategoria, db:Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter_by(categoria_id=categoria_id).first()
    print(categoria_id)
    categoria.nombre_categoria = categoria_actualizada.nombre_categoria
    categoria.descripcion = categoria_actualizada.descripcion
    categoria.esta_activo = categoria_actualizada.esta_activo
    db.commit()
    db.refresh(categoria)
    return categoria

@app.delete('/categorias/{categoria_id}', response_model=schemas.EliminarCategoria)
def eliminar_categorias(categoria_id:int, db:Session = Depends(get_db)):
    categoria = db.query(models.Categoria).filter_by(categoria_id=categoria_id).first()
    db.delete(categoria)
    db.commit()
    mensaje= schemas.EliminarCategoria(mensaje="La categoria "+ str(categoria_id) +" ha sido eliminada correctamente")
    return mensaje


