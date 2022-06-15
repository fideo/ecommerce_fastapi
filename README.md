# e-Commerce FastAPI
Repo del ecommerce que desarrollaremos con FastAPI en #hagamos-equipo de Python en Español



### Itegrantes (usuarios discord)
@Her204 --> Herbert Vente 

@javierespinoza --> Javier Espinoza

@Fideox --> Federico Mazzei

@leo.guanco --> Leo Guanco 



### Mentor (usuarios discord)
@ancaneo --> Aldo Caneo

### Estructura del proyecto


- sql_app:
  - Aqui se desarrolla la conexion al servidor con la aplicacion web.

- Schemas:
  - Aqui se encuentra la estructura del json que pedira el sitio web para subir un registro a la base de datos. 

- Models:
  - En models se encuentran todas las tablas ORM que se usaran en el proyecto. 

- Services:
  - En services se encuentran las funciones que se ejecutaran en routers para cada endpoint.   

- Router:
  - En los routers se encuentran los endpoints de cada objeto del proyecto. (Productos, Usuarios, Categorias, etc) 

- Static: 
  - Aqui se encuentran todas las dependencias del frontend. (css, javascript o imagenes)

- Templates:
  - Aqui se añade el html que se subira al sitio web. 

### Arbol del proyecto

- dependencies.py
  - ecommerce_fastapi.db
  - __init__.py

├── dependencies.py\n├── ecommerce_fastapi.db\n├── __init__.py\n├── main.py\n├── models\n│\xa0\xa0 ├── categoria.py\n│\xa0\xa0 ├── producto.py\n│\xa0\xa0 ├── __pycache__\n│\xa0\xa0 │\xa0\xa0 ├── categoria.cpython-310.pyc\n│\xa0\xa0 │\xa0\xa0 ├── producto.cpython-310.pyc\n│\xa0\xa0 │\xa0\xa0 ├── usuario.cpython-310.pyc\n│\xa0\xa0 │\xa0\xa0 └── venta.cpython-310.pyc\n│\xa0\xa0 ├── usuario.py\n│\xa0\xa0 └── venta.py\n├── __pycache__\n│\xa0\xa0 ├── dependencies.cpython-310.pyc\n│\xa0\xa0 └── main.cpython-310.pyc\n├── README.md\n├── requirements.txt\n├── routers\n│\xa0\xa0 ├── categorias\n│\xa0\xa0 │\xa0\xa0 ├── __init__.py\n│\xa0\xa0 │\xa0\xa0 ├── main.py\n│\xa0\xa0 │\xa0\xa0 └── __pycache__\n│\xa0\xa0 │\xa0\xa0     ├── __init__.cpython-310.pyc\n│\xa0\xa0 │\xa0\xa0     └── main.cpython-310.pyc\n│\xa0\xa0 ├── __init__.py\n│\xa0\xa0 ├── productos\n│\xa0\xa0 │\xa0\xa0 ├── __init__.py\n│\xa0\xa0 │\xa0\xa0 ├── main.py\n│\xa0\xa0 │\xa0\xa0 └── __pycache__\n│\xa0\xa0 │\xa0\xa0     ├── __init__.cpython-310.pyc\n│\xa0\xa0 │\xa0\xa0     └── main.cpython-310.pyc\n│\xa0\xa0 ├── __pycache__\n│\xa0\xa0 │\xa0\xa0 └── __init__.cpython-310.pyc\n│\xa0\xa0 ├── usuarios\n│\xa0\xa0 │\xa0\xa0 ├── __init__.py\n│\xa0\xa0 │\xa0\xa0 ├── main.py\n│\xa0\xa0 │\xa0\xa0 └── __pycache__\n│\xa0\xa0 │\xa0\xa0     ├── __init__.cpython-310.pyc\n│\xa0\xa0 │\xa0\xa0     └── main.cpython-310.pyc\n│\xa0\xa0 └── ventas.py\n├── schemas\n│\xa0\xa0 ├── categorias.py\n│\xa0\xa0 ├── productos.py\n│\xa0\xa0 ├── __pycache__\n│\xa0\xa0 │\xa0\xa0 ├── categorias.cpython-310.pyc\n│\xa0\xa0 │\xa0\xa0 └── productos.cpython-310.pyc\n│\xa0\xa0 ├── usuarios.py\n│\xa0\xa0 └── venta.py\n├── services\n│\xa0\xa0 ├── categorias\n│\xa0\xa0 │\xa0\xa0 ├── main.py\n│\xa0\xa0 │\xa0\xa0 └── __pycache__\n│\xa0\xa0 │\xa0\xa0     └── main.cpython-310.pyc\n│\xa0\xa0 ├── __init__.py\n│\xa0\xa0 ├── productos\n│\xa0\xa0 │\xa0\xa0 ├── main.py\n│\xa0\xa0 │\xa0\xa0 └── __pycache__\n│\xa0\xa0 │\xa0\xa0     └── main.cpython-310.pyc\n│\xa0\xa0 ├── __pycache__\n│\xa0\xa0 │\xa0\xa0 └── __init__.cpython-310.pyc\n│\xa0\xa0 └── ventas.py\n├── sql_app\n│\xa0\xa0 ├── database.py\n│\xa0\xa0 └── __pycache__\n│\xa0\xa0     └── database.cpython-310.pyc\n├── static\n│\xa0\xa0 ├── css\n│\xa0\xa0 │\xa0\xa0 └── styles.css\n│\xa0\xa0 ├── images\n│\xa0\xa0 │\xa0\xa0 └── favicon.ico\n│\xa0\xa0 └── js\n│\xa0\xa0     └── index.js\n├── templates\n│\xa0\xa0 ├── categorias.html\n│\xa0\xa0 ├── contenido.html\n│\xa0\xa0 ├── index.html\n│\xa0\xa0 ├── inicio_sesion.html\n│\xa0\xa0 ├── navegacion.html\n│\xa0\xa0 ├── piedepagina.html\n│\xa0\xa0 └── productos.html\n└── test_db.py
