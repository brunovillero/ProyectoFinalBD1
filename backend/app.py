from flask import Flask, render_template, request
from helpers.registration_controller import register_user

app = Flask(__name__, template_folder='templates')

@app.route('/')
def login():
    return render_template('./login.html')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('./register.html')
    if request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            return register_user(request.json)
    return "Tipo de solicitud invalida"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
