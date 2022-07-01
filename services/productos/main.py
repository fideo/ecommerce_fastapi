#from sql_app import models
from models import producto as producto_models
from models import categoria as categoria_models
from services.categorias import main as  services_categorias
from schemas import productos as productos_schemas
from sqlalchemy.orm import Session
import datetime

#funcion que retorna todos los productos
def obtener_productos(db: Session):
    return db.query(producto_models.Producto).all()

#funcion que crea un producto
def crear_producto(db: Session,producto:productos_schemas.ProductoCreate):

    db_producto = producto_models.Producto(nombre_producto=producto.nombre_producto,stock=producto.stock,
                                    fecha_de_publicacion= datetime.datetime.now(),
                                    descripcion=producto.descripcion,
                                    link_de_imagen= producto.link_de_imagen,
                                    numero_de_productos_subidos=producto.numero_de_productos_subidos,
                                    precio_unitario_de_producto =producto.precio_unitario_de_producto,
                                    )

    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    for cat in producto.categorias:
        categoria = services_categorias.buscar_categoria(db=db,nombre_categoria=cat)
        try: 
            categoria_id = categoria.categoria_id        
        except:
            db_categoria = categoria_models.Categoria(nombre_categoria=cat)
            db.add(db_categoria)
            db.commit()
            db.refresh(db_categoria)
            categoria_id = db_categoria.categoria_id

        print(categoria_id)
    
        db_producto_categoria = producto_models.CategoriaProducto(categoria_id=categoria_id,
                                                                producto_id=db_producto.producto_id)
        db.add(db_producto_categoria)
        db.commit()
        db.refresh(db_producto_categoria)

    return db_producto

def actualizar_producto(producto_id:int, producto_actualizado:productos_schemas.ActualizarProducto, db: Session):
    producto = db.query(producto_models.Producto).filter_by(producto_id=producto_id).first()
    print(producto_id)
    producto.nombre_producto=producto_actualizado.nombre_producto
    producto.stock=producto_actualizado.stock
    producto.descripcion=producto_actualizado.descripcion
    producto.link_de_imagen= producto_actualizado.link_de_imagen
    producto.precio_unitario_de_producto =producto_actualizado.precio_unitario_de_producto
    db.commit()
    db.refresh(producto)
    return producto

#funcion que elimina un producto
def eliminar_producto(db: Session, producto_id: int):
    producto_a_eliminar = db.query(producto_models.Producto).filter(
                            producto_models.Producto.producto_id == producto_id).first()

    if producto_a_eliminar is None:
        return

    db.delete(producto_a_eliminar)
    db.commit()

    return producto_a_eliminar

#funcion que busca un producto por nombre
def buscar_productos(db: Session, palabra_clave:str):
    return db.query(producto_models.Producto).filter(
                producto_models.Producto.nombre_producto.contains(palabra_clave)).all()
