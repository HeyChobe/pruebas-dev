# #La funcion1 recibirá como parámetro la funcion2
# def funcion1(parametro):

#     #hacemos que la funcion1 retorne una nueva funcion3
#     def funcion3():

#         print("Código antes de ejecutar la funcion")
#         parametro() #ejecutamos la funcion
#         print("Código después de ejecutar la funcion")

#     return funcion3

# @funcion1 #utilizamos @ para poder decorar una función

# def funcion2():
#     print("Decoraremos esta función 2")
# #Una vez decorada la función la invocamos
# funcion2()

def funcion_decoradora(funcion_parametro):

    def funcion_interna():
        print("A punto de realizar un calculo")
        # funcion_parametro()
        print("Ya se realizó el calculo")
    return funcion_interna

@funcion_decoradora
def suma():
    print(20+10)

suma()

def resta():
    print(30-12)

resta()

def multiplicación():
    print(3*3)
multiplicación()