axios.get("/categorias").then(r=>{
    r.data.forEach(function(cat) {
        let select = document.getElementById("post_categorias");
        let option =  document.createElement("option");
        option.setAttribute("value", cat.nombre_categoria);
        let optionTexto = document.createTextNode(cat.nombre_categoria);
        option.appendChild(optionTexto);
 
        select.appendChild(option);
    })
})

document.getElementById("boton_crear_producto").onclick = async function () {
    let nombre_producto = await document.getElementById("post_nombre_producto").value;
    let numero_de_productos_subidos = await document.getElementById("post_numero_de_productos_subidos").value;
    let stock = await document.getElementById("post_stock").value;
    let link_de_imagen = await document.getElementById("post_link_de_imagen").value;
    let precio_unitario_de_producto = await document.getElementById("post_precio_unitario_de_producto").value;
    let descripcion = await document.getElementById("post_descripcion").value;
    let categorias = await document.getElementById("post_categorias").value;

    let json_response = {
        "nombre_producto": nombre_producto,
        "numero_de_productos_subidos": parseInt(numero_de_productos_subidos),
        "stock": parseInt(stock),
        "link_de_imagen": link_de_imagen,
        "precio_unitario_de_producto": parseInt(precio_unitario_de_producto),
        "descripcion": descripcion,
        "categorias": [
        categorias
        ]
    }
    
    await axios.post("/productos/crear",json_response);
    location.href = "/";
};