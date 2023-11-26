from flask import Flask, render_template, request, jsonify
from helpers.registration_controller import register_user
from helpers.login_controller import login_func
from helpers.dashboard_controller import get_dashboard_data, upload_carne_salud

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

@app.route('/dashboard', methods = ['GET'])
def dashboard():
    if request.method == 'GET':
        return render_template('./dashboard.html')
    return jsonify("Tipo de solicitud invalida")

@app.route('/get-dashboard-data', methods = ['POST'])
def update_period():
    if request.method == 'POST':
        return jsonify(get_dashboard_data(request.json))
    return jsonify("Tipo de solicitud invalida")

@app.route('/upload-carne-salud', methods = ['POST'])
def upload_carne():
    if request.method == 'POST':
        try:
            return jsonify(upload_carne_salud(request))

        except Exception as e:
            # Handle errors
            return jsonify({'error': str(e)}), 500
    return jsonify("Tipo de solicitud invalida")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
