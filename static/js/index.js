axios.get("/categorias/").then(r => {
  console.log(r.data);
  r.data.forEach(categoria => {
    console.log(categoria)
    const a = document.createElement("a")
    a.innerHTML = categoria.nombre_categoria
    a.href = "/categoria/" + categoria.nombre_categoria
    a.className = "block font-medium text-gray-500 dark:text-gray-300 hover:underline"
    document.getElementById("listaCategorias").appendChild(a)
  });
})

axios.get("/productos/").then(r => {
  r.data.forEach(producto => {
    const div = document.createElement("div")
    div.className = "flex flex-col items-center justify-center w-full max-w-lg mx-auto"
    document.getElementById("listaProductos").appendChild(div)
    const img = document.createElement("img")
    img.src = "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=634&q=80"
    img.alt = producto.nombre_producto
    img.className = "object-cover w-full rounded-md h-72 xl:h-80"
    document.getElementById("listaProductos").appendChild(div).appendChild(img)
    const h4 = document.createElement("h4")
    h4.className = "mt-2 text-lg font-medium text-gray-700 dark:text-gray-200"
    h4.innerHTML = producto.nombre_producto
    document.getElementById("listaProductos").appendChild(div).appendChild(h4)
    const p = document.createElement("p")
    p.className = "text-blue-500"
    p.innerHTML = producto.precio_unitario_de_producto
    document.getElementById("listaProductos").appendChild(div).appendChild(p)
    const button = document.createElement("button")
    button.className = "flex items-center justify-center w-full px-2 py-2 mt-4 font-medium tracking-wide text-white capitalize transition-colors duration-200 transform bg-gray-800 rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700"
    document.getElementById("listaProductos").appendChild(div).appendChild(button)
    const svg = document.createElement("svg")
    svg.xmlns = "http://www.w3.org/2000/svg"
    svg.className = "w-5 h-5 mx-1"
    svg.viewBox = "0 0 20 20"
    svg.fill = "currentColor"
    document.getElementById("listaProductos").appendChild(div).appendChild(button).appendChild(svg)
    const path = document.createElement("path")
    path.d = "M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"
    document.getElementById("listaProductos").appendChild(div).appendChild(button).appendChild(svg).appendChild(path)
    const span = document.createElement("span")
    span.className = "mx-1"
    span.innerHTML = "Agregar al carro"
    document.getElementById("listaProductos").appendChild(div).appendChild(button).appendChild(span)
  });
})