function ingresar(){
    
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

    if(ci.value != ""){
        data.ci = ci.value
    }
    
    if(nombre.value != ""){
        data.nombre = nombre.value
    }

    if(apellido.value != ""){
        data.apellido = apellido.value
    }

    if(fecha_de_nacimiento.value != ""){
        data.fecha_de_nacimiento = fecha_de_nacimiento.value
    }

    if(domicilio.value != ""){
        data.domicilio = domicilio.value
    }

    if(email.value != ""){
        data.email = email.value
    }

    if(telefono.value != ""){
        data.telefono = telefono.value
    }

    if(password.value != ""){
        data.password = password.value
    }

    console.log(data)
}