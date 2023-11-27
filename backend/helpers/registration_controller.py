from helpers.database import mysql_connection
from helpers.database import redis_connection
import argon2

def register_user(data):
    try:
        validate(data)
        return insert_func(data)
    except Exception as error:
        return {"mensaje": "No se pudo registrar usuario: " + str(error)}

def validate(data):
    if not("logid" in data) or data["logid"] == "":
       raise Exception("Usuario requerido")

    if not("password" in data) or data["password"] == "":
       raise Exception("Password requerido")
    
    if not("ci" in data) or data["ci"] == "":
        raise Exception("Cedula requerida")

    if not("nombre" in data) or data["nombre"] == "":
        raise Exception("Nombre requerido")

    if not("apellido" in data) or data["apellido"] == "":
        raise Exception("Apellido requerido")

    if not("fecha_de_nacimiento" in data) or data["fecha_de_nacimiento"] == "":
        raise Exception("Fecha de nacimiento requerido")

    if not("domicilio" in data) or data["domicilio"] == "":
        raise Exception("Domicilio requerido")

    if not("email" in data) or data["email"] == "":
        raise Exception("Email requerido")

    if not("telefono" in data) or data["telefono"] == "":
        raise Exception("Telefono requerido")

def insert_func(data):
    ph = argon2.PasswordHasher()
    data["password"] = ph.hash(data["password"])

    insert_login = ("INSERT INTO Logins "
              "(LogId, Password) "
              "VALUES (%(logid)s, %(password)s)")
    
    insert_func = ("INSERT INTO Funcionarios "
              "(Ci, Nombre, Apellido, Fch_Nacimiento, Direccion, Telefono, Email, LogId) "
              "VALUES (%(ci)s, %(nombre)s, %(apellido)s, %(fecha_de_nacimiento)s, %(domicilio)s, %(telefono)s, %(email)s, %(logid)s)")
    
    mysql = mysql_connection()
    mysql_cursor = mysql.cursor()
    mysql_cursor.execute(insert_login, data)
    mysql_cursor.execute(insert_func, data)
    mysql.commit()
    mysql_cursor.close()
    mysql.close()

    #Hash nuevo para la session
    session_hash = ph.hash(data["password"])
    redis_service = redis_connection()
    redis_service.set(session_hash, data["logid"])
    
    return {"auth": session_hash}