window.onload = datos_del_funcionario()

function datos_del_funcionario(){
    url = "http://localhost:5000/get-dashboard-data"

    fetch(url, {
        method: "POST", 
        body: JSON.stringify(sessionStorage.getItem('auth')), 
        headers: {
            "Content-Type": "application/json",
    },
    })
    .then((res) => res.json())
    .catch((error) => console.error("Error:", error))
    .then((response) => {
        if(response.hasOwnProperty("mensaje")){
            desplegar_mensaje(response.mensaje)
        }else{
            procesar_datos(response)
        }
    })
}

function procesar_datos(response){
    if(response.hasOwnProperty("agenda") && response.agenda != null) {
        agenda_div = document.getElementById("datos-agenda")
        agenda_div.innerHTML = "Ultima fecha agendada: " + response.agenda.Fch_Agenda
        
        historial_agenda_div = document.getElementById("historial-agenda")
        historial_agenda_div.removeAttribute("hidden")
    }
    if(response.hasOwnProperty("carne") && response.carne != null) {
        carne_div = document.getElementById("datos-carne")
        carne_div.innerHTML = "Fecha de emisión: " 
            + response.carne.Fch_Emision + 
            ", Fecha de vencimiento: " + response.carne.Fch_Vencimiento
        
        historial_carne_div = document.getElementById("historial-carne")
        historial_carne_div.removeAttribute("hidden")
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
    if(response.hasOwnProperty("periodo") && response.periodo != null){
        
        fecha_agenda = document.getElementById("fecha-agenda")
        today = new Date()
        today = today.toISOString()
        today = today.substring(0, today.indexOf("."))
        fecha_agenda.setAttribute("min", today)

        fecha_fin = new Date(response.periodo.Fch_Fin)
        fecha_fin = fecha_fin.toISOString()
        fecha_fin = fecha_fin.substring(0, fecha_fin.indexOf("."))

        fecha_agenda.setAttribute("max", fecha_fin)   
    }
}

function carnea_al_dia_si(){
    contenedor_subir_carne = document.getElementById("contenedor-subir-carne")
    contenedor_subir_carne.removeAttribute("hidden")

    contenedor_agendar = document.getElementById("contenedor-agendar")
    contenedor_agendar.setAttribute("hidden", true)
}

function carnea_al_dia_no(){
    contenedor_agendar = document.getElementById("contenedor-agendar")
    contenedor_agendar.removeAttribute("hidden")

    contenedor_subir_carne = document.getElementById("contenedor-subir-carne")
    contenedor_subir_carne.setAttribute("hidden", true)
}

function registrar_carne_salud(){
    data = new FormData();

    fecha_de_emision = document.getElementById("fecha_de_emision")
    fecha_de_vencimiento = document.getElementById("fecha_de_vencimiento")
    archivo_carne = document.getElementById("carnet-archivo").files[0]
    
    data.append('archivo_carne', archivo_carne)
    data.append('fecha_de_vencimiento', fecha_de_vencimiento.value) 
    data.append('fecha_de_emision', fecha_de_emision.value)
    data.append('auth', sessionStorage.getItem('auth'))

    url = "http://localhost:5000/upload-carne-salud"

    fetch(url, {
        method: "POST", 
        body: data, 
    })
    .then((res) => res.json())
    .catch((error) => console.error("Error:", error))
    .then((response) => {
        if(response.hasOwnProperty("mensaje")){
            desplegar_mensaje(response.mensaje)
        }
    })
}


function registrar_agenda(){
    data = {}
    data.auth = sessionStorage.getItem('auth')
    data.fecha_agenda = document.getElementById("fecha-agenda").value

    url = "http://localhost:5000/create-agenda"

    fetch(url, {
        method: "POST", 
        body: JSON.stringify(data), 
        headers: {
            "Content-Type": "application/json",
    },
    })
    .then((res) => res.json())
    .catch((error) => console.error("Error:", error))
    .then((response) => {
        if(response.hasOwnProperty("mensaje")){
            desplegar_mensaje(response.mensaje)
        }
    })
}

function desplegar_mensaje(mensaje){
    document.getElementById("respuesta-servidor").innerHTML = mensaje 
}