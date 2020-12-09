# def bienvenida(nombre):
#     print(f'Bienvenidos a Python {nombre}, tome su dato')
#     dato = "dato"
#     return dato

# var =  bienvenida("Carlos")

# print(var)

def registro(nombre, apellido, edad, sexo="M"):
    return {  
        # objeto diccionario (JSON para mi)
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'sexo': sexo  # sin coma
    }


llamada = registro("Carlos", "Cortez", 20, "M")

print(llamada["nombre"])  # Descomposición
print(llamada["apellido"])
print(llamada["edad"])
print(llamada["sexo"])
