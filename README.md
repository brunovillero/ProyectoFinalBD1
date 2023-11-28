# ProyectoFinalBD1

Requisitos: 
Tener instalado docker-compose, todas las dependencias se descargan automáticamente.

Setup:
1. En una linea de comando situada en la raiz del proyecto, ejecutar: docker-compose up --build
Como MySQL demora en iniciar por primera vez, se recomienda que se esperen unos minutos o hasta que se vea en el terminal
un mensaje del tipo /usr/sbin/mysqld: ready for connections. Version: '8.1.0'  socket: '/var/run/mysqld/mysqld.sock'  
port: 3306  MySQL Community Server - GPL.
Este proceso se hace solamente la primera vez que se carga la aplicación, las siguientes ocasiones solamente se 
ejecuta el comando docker-compose up, el cual demora pocos segundos en levantar todo.
2. Una vez finalizado visitar con cualquier navegador: localhost:5000, el cual lo llevará a la página de login.

Funcionamiento:
-Una vez en la página principal, ingrese con su usuario y contraseña. Si no tiene haga click en el hipervinculo
 debajo del botón "Ingresar" para que lo redirija a la página de registro de usuario.
-Si necesita crear un usuario, debe completar todos los campos del formulario. En caso de que haya alguno faltante
 o que lo ingresado no fuera válido, verá un mensaje de error en la parte inferior de la página.
-Cuando se haya creado el usuario o logeado en la página, se llevará al dashboard donde debe indicar si tiene el carné
de salud al día. 
-En caso positivo, despliega la opción para subir el archivo del carné (JPG o PDF, máximi 16MB) y registrar
la fecha de emisión y vencimiento del mismo. Una vez completado, si se recarga la página aparecerá la fecha de emisión 
y vencimiento del carné vigente.
-Si no se tiene carné de salud al día, despliega el calendario para agendarse dentro de los días disponibles y permite
elegir una hora. Luego de que se confirme, al recargar la página aparecerá en la parte superior el historial de la 
última fecha agendada.

-Por último, si se dirige a la página localhost:5000/listado_funcionarios se descarga automáticamente un .csv con los
datos (CI, correo, nombre, apellido y teléfono) de los funcionarios que no tienen el carné de salud al día.