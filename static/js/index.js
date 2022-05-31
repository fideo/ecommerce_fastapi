axios.get("/categorias/").then(r => {
  r.data.categorias.forEach(categoria => {
    const a = document.createElement("a")
    a.innerHTML = categoria.nombre_categoria
    a.href = "/categoria/" + categoria.nombre_categoria
    a.className = "block font-medium text-gray-500 dark:text-gray-300 hover:underline"
    document.getElementById("listaCategorias").appendChild(a)
  });
})

axios.get("/productos/").then(r => {
  r.data.productos.forEach(producto => {
    const img = document.createElement("img")
    img.src = "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80"
    img.alt = producto.nombre_producto
    document.getElementById("listaProductos").appendChild(img)
  });
})