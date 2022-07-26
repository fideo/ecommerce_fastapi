document.getElementById("boton_crear_categoria").onclick = async function () {
    let nombre_categoria = await document.getElementById("post_nombre_categoria").value;
    let descripcion = await document.getElementById("post_descripcion").value;

    let json_response = {
        "nombre_categoria": nombre_categoria,
        "descripcion": descripcion,
    }

    await axios.post("/categorias/crear", json_response);
    location.href = "/";
};