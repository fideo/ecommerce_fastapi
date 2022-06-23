from sqlalchemy.orm import Session
from . import models, schemas
import datetime
import hashlib

def get_password_hashed(password):
    return hashlib.sha256(bytes(password, 'utf-8')).hexdigest()

def get_user(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id == user_id).first()

#def get_user_by_email(db: Session, email: str):
    #return db.query(models.Usuario).filter(models.Usuario.email == email).first()

def get_user_by_username(db: Session,username: str):
    print(username)
    return db.query(models.Usuario).filter(models.Usuario.username == username).first()
  
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def create_user(db: Session,  user: schemas.UsuarioCreate): # pendienre arreglar conflito en los atributos username y email de la base de datos
    hashed_password = get_password_hashed(user.password)
    db_user = models.Usuario(username=user.username, password=hashed_password) 
    db.add(db_user) 
    db.commit() 
    db.refresh(db_user)
    return db_user

#def crear_usuario():
#    pass


def crear_vendedor(db: Session,
                        vendedor:schemas.VendedorCreate):

    db_vendedor = models.Vendedor(nombre=vendedor.nombre,
                            correo_de_vendedor=vendedor.correo_de_vendedor,
                            contraseña_encriptada=vendedor.contraseña_encriptada,
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