Instruciones para el correcto funcionamiento del programa 
By:
Rodrigo Lazo 
Ricardo Vides 
Fabiola Guardado 
Eduardo Torruella 
Jafet Rosales 

# Co-cu-Manager 8B
El presente proyecto es un programa que permite gestionar actividades cocurriculares, registrando participantes y controlando asistencias, con almacenamiento automático en un archivo JSON. Ideal para llevar un seguimiento organizado desde la terminal.
Detalles sobre las librerías necesarias, si las hubiera.
Cualquier otro paso relevante para ejecutar correctamente su solución.

#desarrollo 

-json: permite guardar y leer datos en formato JSON.
-os: se usa para verificar si existe un archivo.
-datetime: se usa para registrar la fecha actual

-Define el nombre del archivo donde se guardarán los datos de los cocurriculares.

#clase cocurricular 
-Se define una clase para representar cada cocurricular.
-Método constructor: se llama automáticamente al crear una instancia. Recibe el nombre y listas opcionales.

-Asigna el nombre.
-Si no se pasa una lista de participantes o asistencias, se crean vacías por defecto.

-Método para convertir el objeto en un diccionario (clave para guardarlo como JSON).

-Devuelve un diccionario con toda la información del cocurricular.

#funciones para archivo 

-La siguiente función guarda una lista de cocurriculares en el archivo JSON.

-Abre el archivo en modo escritura ("w").
-Convierte cada objeto en diccionario con to_dict() y guarda la lista en formato JSON.

-Esta función carga la lista de cocurriculares desde el archivo.

-Si el archivo no existe, retorna una lista vacía.

-Abre y lee el archivo, cargando el contenido como lista de diccionarios.

-Reconstruye los objetos Cocurricular a partir de los datos del archivo.

#menu principal 

-Carga la lista de cocurriculares desde el archivo al iniciar el menú.

-Ciclo infinito hasta que el usuario elija salir.

-Muestra las opciones del menú.

-Lee la opción elegida por el usuario.

##Opción 1: Agregar cocurricular

-Pide un nombre, crea un nuevo objeto y lo guarda en la lista y en el archivo.

##opcion 2 : ver cocurriculares 

-Muestra una lista numerada de todos los cocurriculares.

##opcion 3 : administrar cocurriculares 

-Muestra todos los cocurriculares numerados para que el usuario elija uno.

-El usuario elige uno (el índice se ajusta a base 0).

-Si el índice es válido, abre el submenú de administración para ese cocurricular.

##Opción 4: Salir

-Sale del menú principal y termina el programa.

#Cualquier otra opción

-Muestra un mensaje si se ingresa una opción no válida.
 print("Opción inválida")
 
#sub menu de administracion 

-Función para administrar un cocurricular específico (c).

-Ciclo infinito hasta que se seleccione "Volver".

-Muestra las opciones del submenú y lee la opción elegida.

##opcion 1: ver participantes 

-Muestra todos los participantes o avisa si no hay ninguno.

##opcion 2: agregar participante 

-Pide un nombre y lo agrega si no está repetido

##opcion 3 : quitar participantes 

-Pide un nombre y lo elimina si está en la lista.

##opcion 4: registrar asistencia 

-Si no hay participantes, no se puede registrar asistencia.

-Crea un diccionario para registrar la asistencia.

-Para cada participante, el usuario escribe "A" o "F" y se guarda el estado. (A para asistencia y F para falta)

-Agrega el registro con fecha actual al historial.

##opciones 5 : ver asistencia de participantes 

-Muestra un mensaje si no hay asistencias guardadas.

-Recorre los registros y muestra la fecha y el estado de cada participante

## opcion 6: volver 

-Sale del submenú y regresa al menú principal.

#opcion no valida 
-Muestra error si se ingresa una opción no válida.
 print("Opción inválida")

#ejecucion del programa 

-Esto asegura que el menú principal se ejecute solo si el archivo es ejecutado directamente, no si es importado desde otro script.




