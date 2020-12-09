#Se importa la librería
import sqlite3

#Creamos la conexión
conexion = sqlite3.connect('PrimeraConexión')

#Interactuamos con la BD
cursor = conexion.cursor()

# # Creando una tabla
# cursor.execute(
#     "CREATE TABLE ALUMNOS(nombre_alumno VARCHAR(50), edad_alumno INTEGER, curso VARCHAR(50))")

##############################

# # Insertando un registro
# cursor.execute("INSERT INTO ALUMNOS VALUES ('Carlos Cortez', 20, 'Python 3')")

# conexion.commit() # Se realiza el commit

##############################

# # Insertando varios registros
# alumnos = [("Samantha Cortez", 22, "Python 3"),("Adriana Guardado", 19, "Python 3"),("Roberto Cortez", 54, "Python 3")]

# #Se utiliza ? por cada cantidad de campos a utilizar
# cursor.executemany("INSERT INTO ALUMNOS VALUES(?,?,?)",alumnos) 

# conexion.commit() # Se realiza el commit

##############################

# # Listando resultados

# cursor.execute("SELECT * FROM ALUMNOS")
# registros = cursor.fetchall() #Obtengo un array de tuplas

# for alumno in registros:
#     print(alumno)

# conexion.commit() # Se realiza el commit

#Cerrarmos la conexión

conexion.close()