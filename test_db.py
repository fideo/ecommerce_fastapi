import datetime
from sqlalchemy.orm import Session
from sql_app.database import engine
from sql_app.models import Usuario, Vendedor, Producto, Categoria,Venta,VentaDeProducto

with Session(bind=engine) as session:

    #usuario = Usuario(correo_de_usuario="admin@ecommerce.com",
    #                  contraseña_encriptada="password",
    #                  pais="Argentina",
    #                  ciudad="Buenos Aires",
    #                  esta_activo=True)

    #vendedor1 = Vendedor(correo_de_vendedor="hola@craq.com",
    #                    nombre="hola soy test",
    #                    contraseña_encriptada = "124sfsrwq",
    #                    pais = "peru",ciudad="lima",esta_activo=True)
    #
    #vendedor2 = Vendedor(correo_de_vendedor="hola@craq_2.com",
    #                    nombre="hola soy test_2",
    #                    contraseña_encriptada = "124sfsrwq_2",
    #                    pais = "india",ciudad="tu vieja",esta_activo=True)
    #
    producto1 = Producto(nombre_producto = "mayonesa australiana cream de la cream",
                    fecha_de_publicacion = datetime.datetime.now(),
                    numero_de_productos_subidos = 12,
                    precio_unitario_de_producto =1500)
    #
    producto2 = Producto(nombre_producto = "ketchup australiana cream de la cream",
                    fecha_de_publicacion = datetime.datetime.now(),
                    numero_de_productos_subidos = 15,
                    precio_unitario_de_producto =1000)

    producto3 = Producto(nombre_producto = "mostasa australiana cream de la cream",
                    fecha_de_publicacion = datetime.datetime.now(),
                    numero_de_productos_subidos = 8,
                    precio_unitario_de_producto =2000)
    venta1 = Venta(fecha_de_venta=datetime.datetime.fromisoformat("2022-06-18"))
    venta2 = Venta(fecha_de_venta=datetime.datetime.fromisoformat("2022-06-21"))
    venta3 = Venta(fecha_de_venta=datetime.datetime.fromisoformat("2022-06-19"))

    session.add_all([producto1,venta1,producto2,venta2,producto3,venta3])
    session.commit()

    print(venta1.venta_id,producto1.producto_id)

    ventadeproducto1 = VentaDeProducto(venta_id=venta1.venta_id,producto_id=producto1.producto_id,precio_unitario=25.4,cantidad=15)
    ventadeproducto2 = VentaDeProducto(venta_id=venta2.venta_id,producto_id=producto2.producto_id,precio_unitario=15.4,cantidad=30)
    ventadeproducto3 = VentaDeProducto(venta_id=venta3.venta_id,producto_id=producto3.producto_id,precio_unitario=19.4,cantidad=25)
    #
    #categoria1 = Categoria(nombre_categoria = "aderezos", descripcion = "condimentos para la comida", esta_activo = True)
    #categoria2 = Categoria(nombre_categoria = "bebidas", descripcion = "todo tipos de bebidas", esta_activo = True)
    #categoria3 = Categoria(nombre_categoria = "electrodomésticos", descripcion = "articulos para el hogar", esta_activo = True)
    #
    #producto1.vendedores = [vendedor1]
    #producto2.vendedores = [vendedor2]
    #producto3.vendedores = [vendedor1,vendedor2]
    #producto1.categorias = [categoria1]
    #producto2.categorias = [categoria1]
    #producto3.categorias = [categoria1]
    #
    session.add_all([ventadeproducto1,ventadeproducto2,ventadeproducto3])
    session.commit()
