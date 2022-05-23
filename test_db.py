import datetime
from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.models import Vendedor,Producto

with Session(bind=engine) as session:

    vendedor1 = Vendedor(correo_de_vendedor="hola@craq.com",
                        nombre="hola soy test",
                        contraseña_encriptada = "124sfsrwq",
                        pais = "peru",ciudad="lima",esta_activo=True)
                        
    vendedor2 = Vendedor(correo_de_vendedor="hola@craq_2.com",
                        nombre="hola soy test_2",
                        contraseña_encriptada = "124sfsrwq_2",
                        pais = "india",ciudad="tu vieja",esta_activo=True)
    
    producto1 = Producto(nombre_producto = "mayonesa australiana cream de la cream",
                    fecha_de_publicacion = datetime.datetime.now(),
                    numero_de_productos_subidos = 12,
                    precio_unitario_de_producto =1500)
                    
    producto2 = Producto(nombre_producto = "ketchup australiana cream de la cream",
                    fecha_de_publicacion = datetime.datetime.now(),
                    numero_de_productos_subidos = 15,
                    precio_unitario_de_producto =1000)
                    
    producto3 = Producto(nombre_producto = "mostasa australiana cream de la cream",
                    fecha_de_publicacion = datetime.datetime.now(),
                    numero_de_productos_subidos = 8,
                    precio_unitario_de_producto =2000)
    
    producto1.vendedores = [vendedor1]
    producto2.vendedores = [vendedor2]
    producto3.vendedores = [vendedor1,vendedor2]
    
    session.add_all([vendedor1, vendedor2, producto1, producto2, producto3])
    session.commit()

