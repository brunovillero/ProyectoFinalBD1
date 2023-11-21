from helpers.database import mysql_connection
import argon2

def login_func(data):
    try:
        validate(data)
        login(data)
        return "Funcionario verificado correctamente"
    except Exception as error:
        return str(error)

def validate(data):
    if not(data["logid"]) or data["logid"] == "":
       raise Exception("Usuario requerido")

    if not(data["password"]) or data["password"] == "":
       raise Exception("Password requerido")
    
def login(data):
    ph = argon2.PasswordHasher()
    
    select_login = ("SELECT LogId, Password FROM Logins "
        "WHERE LogId = %(logid)s")
    
    mysql = mysql_connection()
    mysql_cursor = mysql.cursor()
    mysql_cursor.execute(select_login, data)
    myresult = mysql_cursor.fetchone()
    mysql_cursor.close()
    mysql.close()
    
    if(not ph.verify(myresult[1], data["password"])):
        raise Exception("Credenciales invalidas, intente nuevamente")
