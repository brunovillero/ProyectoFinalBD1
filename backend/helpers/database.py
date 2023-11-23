import mysql.connector
import redis

def mysql_connection():
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

def redis_connection():
    redis_connection = redis.StrictRedis(host="redis", port=6379, decode_responses=True)
    return redis_connection