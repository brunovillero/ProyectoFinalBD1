from flask import Flask, jsonify
import mysql.connector
import redis
import time

app = Flask(__name__)

# Retrasamos la execucion hasta que el contenedor de mysql se encuentre disponible
time.sleep(12)
# Conexion a la base de datos
mysql_connection = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="BD1_Final"
)

# Conexion a la redis
redis_connection = redis.StrictRedis(host="redis", port=6379, db=0)

@app.route('/')
def hello():
    return jsonify(message="Welcome!!!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
