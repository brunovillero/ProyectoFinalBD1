function enviarDatos() {
    const ci = document.getElementById('ci').value;
    const fechaEmision = document.getElementById('fecha_emision').value;
    const fechaVencimiento = document.getElementById('fecha_vencimiento').value;
    const comprobante = document.getElementById('comprobante').files[0];

    if (!comprobante) {
        alert('Por favor, selecciona un archivo.');
        return;
    }

    const reader = new FileReader();
    reader.readAsDataURL(comprobante);
    reader.onload = function() {
        const base64Comprobante = reader.result.split(',')[1];
        const data = JSON.stringify({
            ci,
            fecha_emision: fechaEmision,
            fecha_vencimiento: fechaVencimiento,
            comprobante: base64Comprobante
        });

        fetch('http://localhost:5000/ruta-del-servidor', {
            method: 'POST',
            body: data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => console.log('Respuesta del servidor:', data))
        .catch(error => console.error('Error:', error));
    };
    reader.onerror = function(error) {
        console.error('Error al leer el archivo:', error);
    };
}

// Asignar el evento 'submit' al formulario
document.getElementById('formCarnetSalud').addEventListener('submit', function(event) {
    event.preventDefault();
    enviarDatos();
});
