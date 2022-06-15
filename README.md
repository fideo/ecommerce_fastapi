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

├── dependencies.py
├── ecommerce_fastapi.db
├── __init__.py
├── main.py
├── models
│   ├── categoria.py
│   ├── producto.py
│   ├── __pycache__
│   │   ├── categoria.cpython-310.pyc
│   │   ├── producto.cpython-310.pyc
│   │   ├── usuario.cpython-310.pyc
│   │   └── venta.cpython-310.pyc
│   ├── usuario.py
│   └── venta.py
├── __pycache__
│   ├── dependencies.cpython-310.pyc
│   └── main.cpython-310.pyc
├── README.md
├── requirements.txt
├── routers
│   ├── categorias
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-310.pyc
│   │       └── main.cpython-310.pyc
│   ├── __init__.py
│   ├── productos
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-310.pyc
│   │       └── main.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   ├── usuarios
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-310.pyc
│   │       └── main.cpython-310.pyc
│   └── ventas.py
├── schemas
│   ├── categorias.py
│   ├── productos.py
│   ├── __pycache__
│   │   ├── categorias.cpython-310.pyc
│   │   └── productos.cpython-310.pyc
│   ├── usuarios.py
│   └── venta.py
├── services
│   ├── categorias
│   │   ├── main.py
│   │   └── __pycache__
│   │       └── main.cpython-310.pyc
│   ├── __init__.py
│   ├── productos
│   │   ├── main.py
│   │   └── __pycache__
│   │       └── main.cpython-310.pyc
│   ├── __pycache__
│   │   └── __init__.cpython-310.pyc
│   └── ventas.py
├── sql_app
│   ├── database.py
│   └── __pycache__
│       └── database.cpython-310.pyc
├── static
│   ├── css
│   │   └── styles.css
│   ├── images
│   │   └── favicon.ico
│   └── js
│       └── index.js
├── templates
│   ├── categorias.html
│   ├── contenido.html
│   ├── index.html
│   ├── inicio_sesion.html
│   ├── navegacion.html
│   ├── piedepagina.html
│   └── productos.html
└── test_db.py
