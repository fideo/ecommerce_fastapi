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

@router.get("/productos_por_categoria/{categoria_id}",tags=["productos"],response_model=List[productos_schemas.Producto])
def obtener_productos_por_categoria(categoria_id:int,db: Session = Depends(get_db)):
    productos_seleccionados = productos_services.seleccionar_productos_por_categorias(categoria_id=categoria_id,
                                                                                    db=db)
    return productos_seleccionados

#creamos un endpoint que se conecte a la  funcion que busca productos por nombre en el services
@router.get("/buscar", tags=["productos"], response_model=List[productos_schemas.Producto])
def buscar_producto(palabra_clave:str, db: Session = Depends(get_db)):
    productos_buscados = productos_services.buscar_productos(palabra_clave=palabra_clave, db=db)
    return productos_buscados

#creamos un endpoint que se conecte a la funcion que crea un producto en el services
@router.post("/crear/", tags=["productos"], response_model=productos_schemas.Producto)
async def crear_producto(producto: productos_schemas.ProductoCreate,db: Session = Depends(get_db)):
    return productos_services.crear_producto(db=db,producto=producto)

@router.put("/actualizar/{producto_id}", tags=["productos"], response_model=productos_schemas.Producto) 
def actualizar_producto(producto_id: int,producto_actualizado:productos_schemas.ActualizarProducto, db: Session = Depends(get_db)):
    return productos_services.actualizar_producto(db=db, producto_id=producto_id,producto_actualizado=producto_actualizado)


#creamos un endpoint que se conecte a la funcion que elimina un producto en el services
@router.delete("/eliminar/{producto_id}", tags=["productos"], response_model=productos_schemas.Producto) 
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    return productos_services.eliminar_producto(db=db, producto_id=producto_id)
