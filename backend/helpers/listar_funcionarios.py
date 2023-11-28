import csv
from helpers.database import mysql_connection

def listar_funcionarios():
    try:
        
        select_func_sin_carne = ("SELECT Ci, Email, Nombre, Apellido, Telefono, Email FROM Funcionarios WHERE "
        "CI NOT IN (SELECT CI FROM Carnet_Salud)")

        mysql = mysql_connection()
        mysql_cursor = mysql.cursor(dictionary=True)
        mysql_cursor.execute(select_func_sin_carne)
        query = mysql_cursor.fetchall()
        mysql_cursor.close()
        mysql.close()

        with open('listado_funcionarios.csv', 'w', newline='') as csvfile:
            
            fieldnames = ['Ci', 'Email', 'Nombre', 'Apellido', 'Telefono'] 
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(query)
            csvfile.close()
    except Exception as error:
        print("Error al generar el listado: " + error)