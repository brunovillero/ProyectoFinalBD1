from helpers.database import mysql_connection
from helpers.database import redis_connection
import argon2

def login_func(data):
    try:
        validate(data)
        return login(data)
    except Exception as error:
        return {"mensaje": str(error)}

def validate(data):
    if not("logid" in data) or data["logid"] == "":
       raise Exception("Usuario requerido")

    if not("password" in data) or data["password"] == "":
       raise Exception("Password requerido")
    
def login(data):
    ph = argon2.PasswordHasher()
    
    select_login = ("SELECT LogId, Password FROM Logins "
        "WHERE LogId = %(logid)s")
    
    mysql = mysql_connection()
    mysql_cursor = mysql.cursor(dictionary=True)
    mysql_cursor.execute(select_login, data)
    login = mysql_cursor.fetchone()
    mysql_cursor.close()
    mysql.close()

    try:
        if login and ph.verify(login["Password"], data["password"]):
            
            #Creamos un nuevo hash en cache para la session
            #El cual se va a utilizar en el front para validar las solicitudes en el backend
            session_hash = ph.hash(data["password"])
            redis_service = redis_connection()
            redis_service.set(session_hash, data["logid"])
            
            return {"auth": session_hash}
        else:
            raise Exception("Credenciales invalidas")
    except Exception: 
        raise Exception("Credenciales invalidas")