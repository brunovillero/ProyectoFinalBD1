function ingresar(data){
    let url = "http://localhost:5000/";

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
            //guardamos el hash creado para la session
            sessionStorage.setItem("auth", response.auth)
            //redirigimos al dashboard
        })
}

function validar(){
    let data = {}
    
    let logid = document.getElementById("logid")
    let password = document.getElementById("password")

    if(esValido(logid.value)){
        data.logid = logid.value
    }
    
    if(esValido(password.value)){
        data.password = password.value
    }

    console.log(data)

    ingresar(data)
}

function esValido(str) {
    //removemos espacios a los extremos y chequeamos que no exista ninguno en el medio
    return str.trim().length > 0 && !str.includes(" ");
}