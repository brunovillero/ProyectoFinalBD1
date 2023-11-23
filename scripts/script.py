from backend import mysql_connection
import mysql.connector
import schedule
import time

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'nombre_de_tu_base_de_datos',
    'raise_on_warnings': True
}

def buscar_funcionarios_sin_carne_o_vencido():
    # Establece la conexión con la base de datos
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Consulta para encontrar funcionarios sin carné de salud o con carné vencido y que no están en agenda
    query = """
    SELECT f.Ci, f.Nombre, f.Apellido
    FROM Funcionarios f
    LEFT JOIN Carnet_Salud cs ON f.Ci = cs.Ci
    LEFT JOIN Agenda a ON f.Ci = a.Ci
    WHERE (cs.Ci IS NULL OR cs.Fch_Vencimiento < CURDATE()) AND a.Ci IS NULL;
    """

    cursor.execute(query)

    # Procesa los resultados
    for (ci, nombre, apellido) in cursor:
        print(f"Funcionario: {nombre} {apellido}, CI: {ci}, no tiene carné de salud válido y no está en agenda.")

    # Cierra la conexión
    cursor.close()
    connection.close()

# Programa la tarea para que se ejecute cada cierto tiempo, por ejemplo, cada día
schedule.every().day.at("10:00").do(buscar_funcionarios_sin_carne_o_vencido)

# Ejecuta indefinidamente
while True:
    schedule.run_pending()
    time.sleep(1)

