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
    
    let ci = document.getElementById("ci")
    let nombre = document.getElementById("nombre")
    let apellido = document.getElementById("apellido")
    let fecha_de_nacimiento = document.getElementById("fecha_de_nacimiento")
    let domicilio = document.getElementById("domicilio")
    let email = document.getElementById("email")
    let telefono = document.getElementById("telefono")
    let password = document.getElementById("password")

    if(isValid(ci.value)){
        data.ci = ci.value
    }
    
    if(isValid(nombre.value)){
        data.nombre = nombre.value
    }

    if(isValid(apellido.value)){
        data.apellido = apellido.value
    }

    if(isValid(fecha_de_nacimiento.value)){
        data.fecha_de_nacimiento = fecha_de_nacimiento.value
    }

    if(isValid(domicilio.value)){
        data.domicilio = domicilio.value
    }

    if(isValid(email.value)){
        data.email = email.value
    }

    if(isValid(telefono.value)){
        data.telefono = telefono.value
    }

    if(isValid(password.value)){
        data.password = password.value
    }

    console.log(data)

    ingresar(data)
}

function isValid(str) {
    //removemos espacios a los extremos y chequeamos que no exista ninguno en el medio
    return str.trim().length > 0 && !str.includes(" ");
}