document.getElementById('agenda-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Obtén los valores del formulario
    var ci = document.getElementById('ci').value;
    var fechaAgenda = document.getElementById('fecha_agenda').value;

    // Construye los datos a enviar
    var data = {
        ci: ci,
        fecha_agenda: fechaAgenda
    };

    // Hace la petición al servidor
    fetch('/agendar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Aquí puedes redirigir al usuario o mostrar un mensaje de éxito/error
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});