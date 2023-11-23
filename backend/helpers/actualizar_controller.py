import base64
import mysql.connector

def actualizar_controller(data):
    # Descomprime y procesa los datos recibidos
    ci = data['ci']
    fecha_emision = data['fecha_emision']
    fecha_vencimiento = data['fecha_vencimiento']
    comprobante_base64 = data['comprobante']

    # Decodifica el comprobante desde base64 a binario
    comprobante = base64.b64decode(comprobante_base64)

    # Conecta a la base de datos (ajusta estos valores según tu configuración)
    connection = mysql.connector.connect(
        host='localhost',
        user='tu_usuario',
        password='tu_contraseña',
        database='nombre_de_tu_base_de_datos'
    )
    cursor = connection.cursor()

    # Prepara la consulta SQL para insertar o actualizar el carné de salud
    query = """
    INSERT INTO Carnet_Salud (Ci, Fch_Emision, Fch_Vencimiento, Comprobante)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    Fch_Emision = VALUES(Fch_Emision),
    Fch_Vencimiento = VALUES(Fch_Vencimiento),
    Comprobante = VALUES(Comprobante);
    """

    # Ejecuta la consulta
    try:
        cursor.execute(query, (ci, fecha_emision, fecha_vencimiento, comprobante))
        connection.commit()
        return "Carné de salud actualizado correctamente"
    except mysql.connector.Error as err:
        return f"Error al actualizar el carné de salud: {err}"
    finally:
        cursor.close()
        connection.close()
