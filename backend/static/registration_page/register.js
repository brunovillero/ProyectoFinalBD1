function ingresar(data){
    let url = "http://localhost:5000/register";

    fetch(url, {
        method: "POST", 
        body: JSON.stringify(data), 
        headers: {
            "Content-Type": "application/json",
    },
    })
        .then((res) => res.json())
        .catch((error) => console.error("Error:", error))
        .then((response) => console.log("Success:", response))
}

function validar(){
    let data = {}
    
    let logid = document.getElementById("logid")
    let password = document.getElementById("password")
    let ci = document.getElementById("ci")
    let nombre = document.getElementById("nombre")
    let apellido = document.getElementById("apellido")
    let fecha_de_nacimiento = document.getElementById("fecha_de_nacimiento")
    let domicilio = document.getElementById("domicilio")
    let email = document.getElementById("email")
    let telefono = document.getElementById("telefono")

    if(esValido(logid.value)){
        data.logid = logid.value
    }
    
    if(esValido(password.value)){
        data.password = password.value
    }

    if(esValido(ci.value)){
        data.ci = ci.value
    }
    
    if(esValidoConEspacios(nombre.value)){
        data.nombre = nombre.value
    }

    if(esValidoConEspacios(apellido.value)){
        data.apellido = apellido.value
    }

    if(esValido(fecha_de_nacimiento.value)){
        data.fecha_de_nacimiento = fecha_de_nacimiento.value
    }

    if(esValidoConEspacios(domicilio.value)){
        data.domicilio = domicilio.value
    }

    if(esValido(email.value)){
        data.email = email.value
    }

    if(esValido(telefono.value)){
        data.telefono = telefono.value
    }

    console.log(data)

    ingresar(data)
}

function esValido(str) {
    //removemos espacios a los extremos y chequeamos que no exista ninguno en el medio
    return str.trim().length > 0 && !str.includes(" ");
}

function esValidoConEspacios(str) {
    // Solo aseguramos que la cadena no esté vacía después de quitar espacios al inicio y al final
    return str.trim().length > 0;
}
