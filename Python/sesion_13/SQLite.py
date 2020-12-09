import sqlite3

conexion = sqlite3.connect("AdministraciónAlumnos")
cursor = conexion.cursor()


#AUTOINCREMENT con INTEGER
#UNIQUE para campos no repetibles
# cursor.execute('''
#     CREATE TABLE CURSOS(
#     id_curso INTEGER PRIMARY KEY AUTOINCREMENT, 
#     nombre_curso VARCHAR(50) UNIQUE, cupos_curso INTEGER, horas_curso INTEGER)
# ''')

# cursos = [
#     ("Python básico",50,36),
#     ("Java",50,60),
#     ("C#",50,70),
#     ("Python Intermedio",50,40),
#     ("Python Avanzado",50,40),
# ]

# #Se coloca NULL en el autoincrementable
# cursor.executemany("INSERT INTO CURSOS VALUES(NULL,?,?,?)", cursos)
# conexion.commit()

cursor.execute(
    '''
    SELECT * FROM CURSOS 
    WHERE nombre_curso = 'Java'
    '''
)
conexion.commit()
cursos = cursor.fetchall()

print(cursos)

cursor.execute(
    '''
    DELETE FROM CURSOS
    WHERE nombre_curso = 'C#'
    '''
)
conexion.commit()

name = input("Digite el nombre del curso a consultar: ")

cursor.execute(
    f'''
    SELECT * FROM CURSOS
    WHERE nombre_curso = '{name}'
    '''
)

curso_pedido = cursor.fetchall()

print(curso_pedido[0])

conexion.commit()

conexion.close()