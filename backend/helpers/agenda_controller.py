from .database import mysql_connection
import argon2

def agenda_controller(data):
    # Asegúrate de que todos los campos necesarios estén presentes
    if not data.get("ci") or not data.get("fecha_agenda"):
        return {"error": "Información incompleta para agendar"}

    # Conecta con la base de datos
    conn = mysql_connection()
    cursor = conn.cursor()

    # Aquí va la lógica para insertar en la tabla Agenda
    try:
        insert_query = """
        INSERT INTO Agenda (Ci, Fch_Agenda) VALUES (%s, %s)
        """
        cursor.execute(insert_query, (data["ci"], data["fecha_agenda"]))
        conn.commit()
        return {"success": "Agendamiento realizado con éxito"}
    except Exception as e:
        # Asegúrate de manejar correctamente la excepción y de hacer rollback si es necesario
        conn.rollback()
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()
