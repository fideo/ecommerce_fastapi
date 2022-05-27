axios.get("/categorias/").then(r => {
  r.data.categorias.forEach(categoria => {
    const a = document.createElement("a")
    a.innerHTML = categoria.nombre_categoria
    a.href = "/categoria/" + categoria.nombre_categoria
    a.className = "block font-medium text-gray-500 dark:text-gray-300 hover:underline"
    document.getElementById("listaCategorias").appendChild(a)
  });
})