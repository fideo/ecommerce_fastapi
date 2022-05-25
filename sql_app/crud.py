from sqlalchemy.orm import Session
from . import models, schemas
import datetime


def crear_usuario():
    pass


def crear_vendedor(db: Session,
                        vendedor:schemas.VendedorCreate):

    db_vendedor = models.Vendedor(nombre=vendedor.nombre,
                            correo_de_vendedor=vendedor.correo_de_vendedor,
                            contraaeña_encriptada=vendedor.contraseña_encriptada,
                            pais=vendedor.pais,
                            ciudad=vendedor.ciudad)
    db.add(db_vendedor)
    db.commit()
    db.refresh(db_vendedor)
    return db_vendedor


def crear_producto(db: Session,
                        producto:schemas.ProductoCreate,
                        vendedor_id:int):

    db_producto = models.Producto(nombre_producto=producto.nombre_producto,
                                fecha_de_publicacion=datetime.datetime.now(),
                                descripcion=producto.descripcion,
                                numero_de_productos_subidos=producto.numero_de_productos_subidos,
                                precio_unitario_de_producto =producto.precio_unitario_de_producto,
                                vendedor_del_producto=vendedor_id,
                                )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto


def eliminar_producto(db: Session, producto_id: int):
    producto_a_eliminar = db.query(models.Producto).filter(
                            models.Producto.producto_id == producto_id).first()

    if producto_a_eliminar is None:
        return

    db.delete(producto_a_eliminar)
    db.commit()

    return producto_a_eliminar


def buscar_producto(db: Session, palabra_clave:str):
    return db.query(models.Producto).filter(
                models.Producto.nombre_producto.contains(palabra_clave)).all()


def subir_producto_a_carrito():
    pass
