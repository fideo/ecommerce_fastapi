from typing import List
from sqlalchemy.orm import Session
from sql_app import models, schemas
from dependencies import get_db
from fastapi import APIRouter, Depends
import datetime

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("/", tags=["productos"], response_model=List[schemas.ProductoCreate])
def crear_producto(producto:schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = models.Producto(nombre_producto=producto.nombre_producto,
                                fecha_de_publicacion=datetime.datetime.now(),
                                descripcion=producto.descripcion,
                                numero_de_productos_subidos=producto.numero_de_productos_subidos,
                                precio_unitario_de_producto =producto.precio_unitario_de_producto,
                                )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

# @router.get("/", tags=["productos"], response_model=List[schemas.ProductoEliminar])
# def eliminar_producto(db: Session, producto_id: int):
#     producto_a_eliminar = db.query(models.Producto).filter(
#                             models.Producto.producto_id == producto_id).first()

#     if producto_a_eliminar is None:
#         return

#     db.delete(producto_a_eliminar)
#     db.commit()

#     return producto_a_eliminar
