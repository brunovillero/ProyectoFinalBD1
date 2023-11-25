alert(sessionStorage.getItem('auth'))

window.onload(periodo_de_actualizacion())

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
    .then((response) => console.log("Success:", response))
}