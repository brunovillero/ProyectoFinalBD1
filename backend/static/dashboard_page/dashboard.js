alert(sessionStorage.getItem('auth'))

window.onload = periodo_de_actualizacion()

function periodo_de_actualizacion(){
    let url = "http://localhost:5000/update-period";

    fetch(url, {
        method: "POST", 
        body: JSON.stringify(sessionStorage.getItem('auth')), 
        headers: {
            "Content-Type": "application/json",
    },
    })
    .then((res) => res.json())
    .catch((error) => console.error("Error:", error))
    .then((response) => procesar_datos(response))
}

function procesar_datos(response){
    if (response.hasOwnProperty("mensaje")) {
        mensajes_div = document.getElementById("mensaje")
        mensajes_div.innerHTML = response.mensaje
        mensajes_div.removeAttribute("hidden")
    }
    if(response.hasOwnProperty("agenda") && response.agenda != null) {
        agenda_div = document.getElementById("datos-agenda")
        agenda_div.innerHTML = "Ultima fecha agendada: " + response.agenda.Fch_Agenda
        agenda_div.removeAttribute("hidden")
    }
    if(response.hasOwnProperty("funcionario") && response.funcionario != null) {
        ci = document.getElementById("ci")
        ci.value = response.funcionario.Ci
        
        nombre = document.getElementById("nombre")
        nombre.value = response.funcionario.Nombre

        apellido = document.getElementById("apellido")
        apellido.value = response.funcionario.Apellido

        fecha_de_nacimiento = document.getElementById("fecha_de_nacimiento")
        fecha_de_nac_fm = new Date(response.funcionario.Fch_Nacimiento)
        fecha_de_nacimiento.valueAsDate = fecha_de_nac_fm

        div_datos_funcionario = document.getElementById("datos-funcionario")
        div_datos_funcionario.removeAttribute("hidden")

        div_contenedor_carne_al_dia = document.getElementById("contenedor-carne-al-dia")
        div_contenedor_carne_al_dia.removeAttribute("hidden")
    }
}

function carneaAlDiaSi(){
    contenedor_subir_carne = document.getElementById("contenedor-subir-carne")
    contenedor_subir_carne.removeAttribute("hidden")

    contenedor_agendar = document.getElementById("contenedor-agendar")
    contenedor_agendar.setAttribute("hidden", true)
}

function carneaAlDiaNo(){
    contenedor_agendar = document.getElementById("contenedor-agendar")
    contenedor_agendar.removeAttribute("hidden")

    contenedor_subir_carne = document.getElementById("contenedor-subir-carne")
    contenedor_subir_carne.setAttribute("hidden", true)
}