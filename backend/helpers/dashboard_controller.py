from helpers.database import redis_connection
from helpers.database import mysql_connection
from datetime import date


def get_update_period(session_hash):
    redis_service = redis_connection()
    logid = redis_service.get(session_hash)
    
    if not logid:
        return "Usuario no authorizado"
    
    today_date = date.today()
    sql_data = { "today": today_date.strftime('%Y-%m-%d') }

    select_period = ("SELECT Fch_Inicio, Fch_Fin FROM Periodos_Actualizacion "
        "WHERE Fch_Inicio <= %(today)s "
        "And Fch_Fin >= %(today)s")
    
    mysql = mysql_connection()
    mysql_cursor = mysql.cursor()
    mysql_cursor.execute(select_period, sql_data)
    myresult = mysql_cursor.fetchone()
    mysql_cursor.close()
    mysql.close()
    
    return myresult
    
