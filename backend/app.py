from flask import Flask, jsonify
import mysql.connector
import redis
import time

app = Flask(__name__)

def connect_to_mysql():
    for _ in range(24):  # 24 intentos
        try:
            connection = mysql.connector.connect(
                host="mysql",
                user="root",
                password="root",
                database="BD1_Final"
            )
            if connection.is_connected():
                print("conectado!!")
                return connection

        except mysql.connector.Error as err:
            print("No se puede conectar a MySQL:", err)
            time.sleep(5)  # Espera de 5 segundos entre cada intento
    raise Exception("Failed to connect to MySQL after several attempts")

# Intenta conectarse a MySQL con reintentos
mysql_connection = connect_to_mysql()


# Conexion a la redis
redis_connection = redis.StrictRedis(host="redis", port=6379, db=0)

@app.route('/')
def hello():
    return jsonify(message="Welcome!!!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
