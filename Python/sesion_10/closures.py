# def lista_alumnos(listado):
#     def listar():
#         for alumno in listado:
#             print(alumno)
#     listar()
#     print(listado)

# #imprimimos todo el parámetro después de ejecutar listar
# #el parámetro impreso aparece antes de ser declarado

# listado = ['Luis', 'Ana', 'Carlos', 'Laura', 'Rafael', 'Frank']
# lista_alumnos(listado)

################################

# '''

# Si necesitamos cambiar las variables locales debemos hacer
# uso de nonlocal
# '''

# def lista_alumnos(listado):
#     def listar():

#         nonlocal listado #Con nonlocal modificamos la variable enviada
#         listado = ['Claudia','Juan','Iris']
#         for alumno in listado:
#             print(alumno)

#     listar()
#     print(listado)

# listado = ['Luis', 'Ana', 'Carlos', 'Laura', 'Rafael', 'Frank']
# lista_alumnos(listado)

################################

# def closure(parametro):
#     def funcion():
#         return parametro + 1 # parametro es de la función closure()
#     return funcion

# variable = closure(parametro=2)
# print (variable()) # Imprime 3

#closure
def lista_alumnos(listado):
    listado = listado #local

    def listar():

        print(listado)

    return listar #retornamos la función listar

#asignamos la función lista_alumnos a una variable
nueva_variable = lista_alumnos("Luis, Ana, Carlos, Laura")
#llamamos a la nueva funcion creada en la variable
nueva_variable()