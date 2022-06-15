from typing import List
from sqlalchemy.orm import Session
from schemas import productos as productos_schemas
from dependencies import get_db
from fastapi import APIRouter, Depends
from services.productos import main as productos_services

router = APIRouter(prefix="/productos", tags=["productos"])

#creamos un endpoint que se conecte a la funcion que retorna todos los productos en el services
@router.get("/", tags=["productos"], response_model=List[productos_schemas.Producto])
def obtener_productos(db: Session = Depends(get_db)):
    producto = productos_services.obtener_productos(db=db)
    return producto

#creamos un endpoint que se conecte a la  funcion que busca productos por nombre en el services
@router.get("/buscar", tags=["productos"], response_model=List[productos_schemas.Producto])
def buscar_producto(palabra_clave:str, db: Session = Depends(get_db)):
    return productos_services.buscar_producto(palabra_clave=palabra_clave, db=db)

#creamos un endpoint que se conecte a la funcion que crea un producto en el services
@router.get("/crear/", tags=["productos"], response_model=productos_schemas.ProductoCreate)
def crear_producto(producto: productos_schemas.ProductoCreate,db: Session = Depends(get_db)):
    return productos_services.crear_producto(db=db,producto=producto)

#creamos un endpoint que se conecte a la funcion que elimina un producto en el services
@router.get("/eliminar/{producto_id}", tags=["productos"], response_model=productos_schemas.Producto) 
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    return productos_services.eliminar_producto(db=db, producto_id=producto_id)