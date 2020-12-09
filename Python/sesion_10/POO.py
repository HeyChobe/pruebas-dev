# class MiClase:
#     #método
#     def funcion(self): #Se coloca self "en si"
#         print("Bienvenidos al curso de Python 3")

# nombre = MiClase() #Objeto
# nombre.funcion()

# class Alumnos:

#     def fnalumnos(self,elnombre):
#         return elnombre + " Bienvenido al curso de Python 3"

#     def imprimir(self):
#             print(self.nombre)
#             print(self.apellido)

# alumno = Alumnos()
# tutor = Alumnos() # Ejemplo xd
# #atributos
# alumno.edad=33
# tutor.nombre="Carlos"
# tutor.apellido = "Cortez"
# tutor.imprimir()
# alumno.nombre="Francisco"
# alumno.apellido="Quezada"
# alumno.dui="03569852-0"
# alumno.email="alumno@alumno.com"
# alumno.imprimir()

########################################################

# Creando atributos para los objetos dentro de la clase
# class Registro:

#     def imprime_nombre(self):
#         print(self.nombre)

#         # método que crea atributo
#     def crea_objeto_nombre(self, nombre):

#             self.nombre = nombre  # objeto.nombre=nombre

#         # método que imprime el atributo
#     def imprime_objeto_nombre(self):

#             print(self.nombre)


# alumno = Registro()
# alumno.crea_objeto_nombre("Francisco Quezada")
# alumno.imprime_objeto_nombre()

#####################################

# class Registro:

#     # __init__ me ayuda a no estar declarando en otros lados las variables que usaré
#     #Constructor
#     def __init__(self, nombre='', apellido='', edad='', dui='', sexo=''):

#         self.nombre = nombre #valor por defecto
#         self.apellido = apellido
#         self.edad = edad
#         self.dui = dui
#         self.sexo = sexo

#     def mensaje(self):
#         return "Bienvenido al curso de Python 3:" + self.nombre

#     def imprime_apellido(self):
#         print(self.apellido)

# alumno = Registro("Francisco","Quezada",33,"01256459-2","Hombre") #Creando un objeto con las variables específicas

# respuesta = alumno.mensaje()
# print(respuesta)

#####################################

class Vehiculos:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmovimiento = False
        self.acelera = False
        self.frena = False

    def se_mueve(self):
        self.enmovimiento = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado_vehiculo(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn movimiento:", self.enmovimiento,
              "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Moto(Vehiculos):  # Hereadando de Vehículos
    pass  # No ejecuta nada

    # creamos las instancias de la clase moto
    # podremos utilizar los métodos de la clase vehiculos


lamoto = Moto("Toyota", "Corolla")  # parámetros marca y modelo

# llamamos a cualquiera de los métodos heredados
lamoto.estado_vehiculo()
