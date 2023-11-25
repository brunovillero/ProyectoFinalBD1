from helpers.database import redis_connection
from helpers.database import mysql_connection
from datetime import date


def get_dashboard_data(session_hash):
    redis_service = redis_connection()
    logid = redis_service.get(session_hash)
    
    if not logid:
        return {"mensaje": "Usuario no autorizado"}
    
    today_date = date.today()
    sql_data = { "today": today_date.strftime('%Y-%m-%d'), "logid": logid }

    select_period = ("SELECT Fch_Inicio, Fch_Fin FROM Periodos_Actualizacion "
        "WHERE Fch_Inicio <= %(today)s "
        "And Fch_Fin >= %(today)s")
    
    mysql = mysql_connection()
    
    mysql_cursor = mysql.cursor(dictionary=True)
    mysql_cursor.execute(select_period, sql_data)
    period = mysql_cursor.fetchone()
    
    if not period:
        return {"mensaje": "Periodo finalizado"}
    
    select_func = ("SELECT Ci, Nombre, Apellido, Fch_Nacimiento, Direccion, Telefono, Email FROM Funcionarios "
        "WHERE LogId = %(logid)s")
    
    mysql_cursor.execute(select_func, sql_data)
    func = mysql_cursor.fetchone()

    select_agenda = ("SELECT Fch_Agenda FROM Agenda "
        "WHERE Ci = %(Ci)s ORDER BY Fch_Agenda DESC LIMIT 1")

    mysql_cursor.execute(select_agenda, func)
    agenda = mysql_cursor.fetchone()

    select_carne_salud = ("SELECT Fch_Emision, Fch_Vencimiento FROM Carnet_Salud "
        "WHERE Ci = %(Ci)s ORDER BY Fch_Vencimiento DESC LIMIT 1")

    mysql_cursor.execute(select_carne_salud, func)
    carne = mysql_cursor.fetchone()

    mysql_cursor.close()
    mysql.close()

    response = {
        "periodo": period,
        "funcionario": func,
        "agenda": agenda,
        "carne": carne
    }

    return response