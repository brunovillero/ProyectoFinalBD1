from helpers.database import mysql_connection
import argon2

def register_user(data):
    try:
        validate(data)
        insert_func(data)
        return "Funcionario registrado correctamente"
    except Exception as error:
        return str(error)

def validate(data):

    if not(data["logid"]) or data["logid"] == "":
       raise Exception("Usuario requerido")

    if not(data["password"]) or data["password"] == "":
       raise Exception("Password requerido")
    
    if not(data["ci"]) or data["ci"] == "":
        raise Exception("Cedula requerida")

    if not(data["nombre"]) or data["nombre"] == "":
        raise Exception("Nombre requerido")

    if not(data["apellido"]) or data["apellido"] == "":
        raise Exception("Apellido requerido")

    if not(data["fecha_de_nacimiento"]) or data["fecha_de_nacimiento"] == "":
        raise Exception("Fecha de nacimiento requerido")

    if not(data["domicilio"]) or data["domicilio"] == "":
        raise Exception("Domicilio requerido")

    if not(data["email"]) or data["email"] == "":
        raise Exception("Email requerido")

    if not(data["telefono"]) or data["telefono"] == "":
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

    try:
        mysql = mysql_connection()
        mysql_cursor = mysql.cursor()
        mysql_cursor.execute(insert_login, data)
        mysql_cursor.execute(insert_func, data)
        mysql.commit()
        mysql_cursor.close()
        mysql.close()
    except Exception:
        mysql_cursor.close()
        mysql.close()
        raise Exception("No se pudo registrar usuario, puede que la cedula o el usuario ya esten registrados.")