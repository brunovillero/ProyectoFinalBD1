from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def login():
    return render_template('./login.html')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('./register.html')
    else:
        print(request.json)
        return request.json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
