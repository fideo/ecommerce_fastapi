#from sql_app import models
from models.producto import Producto
from schemas import productos as productos_schemas
from sqlalchemy.orm import Session


#funcion que retorna todos los productos
def obtener_productos(db: Session):
    return db.query(Producto).all()

#funcion que crea un producto
def crear_producto(db: Session,producto:productos_schemas.ProductoCreate):

    db_producto = Producto(nombre_producto=producto.nombre_producto,
                                fecha_de_publicacion= datetime.datetime.now(),
                                descripcion=producto.descripcion,
                                link_de_imagen= producto.link_de_imagen,
                                numero_de_productos_subidos=producto.numero_de_productos_subidos,
                                precio_unitario_de_producto =producto.precio_unitario_de_producto,
                                )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

#funcion que elimina un producto
def eliminar_producto(db: Session, producto_id: int):
    producto_a_eliminar = db.query(Producto).filter(
                            Producto.producto_id == producto_id).first()

    if producto_a_eliminar is None:
        return

    db.delete(producto_a_eliminar)
    db.commit()

    return producto_a_eliminar

#funcion que busca un producto por nombre
def buscar_producto(db: Session, palabra_clave:str):
    return db.query(Producto).filter(
                Producto.nombre_producto.contains(palabra_clave)).all()
