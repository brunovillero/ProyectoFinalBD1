from flask import Flask, render_template, request, jsonify
from helpers.registration_controller import register_user
from helpers.login_controller import login_func
from helpers.agenda_controller import agenda_controller
from helpers.actualizar_controller import actualizar_controller


app = Flask(__name__, template_folder='templates')

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('./login.html')
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            return jsonify(login_func(request.json))
    return jsonify("Tipo de solicitud invalida")

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('./register.html')
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            return jsonify(register_user(request.json))
    return jsonify("Tipo de solicitud invalida")

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'GET':
        return render_template('./agendar.html')
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type') 
        if (content_type == 'application/json'):
            return jsonify(agenda_controller(request.json))
    return  jsonify("Tipo de solicitud invalida") 

@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar():
    if request.method == 'GET':
        # Retorna la página de actualización o el formulario necesario
        return render_template('./actualizar.html')
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            # Llama a la función actualizar_controller para manejar la petición
            return jsonify(actualizar_controller(request.json))
        else:
            return jsonify("Tipo de solicitud invalida")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
