# #Ejercicio 01

# print("Cantidad de notas a ingresar: ")
# cant = int(input())

# i=0
# notasTotal = 0

# while i<cant:
#     print(f'Ingrese la nota {i+1}: ')
#     notasTotal += float(input())
#     i+=1

# promedio = notasTotal/cant
# print(f'El promedio total es de {promedio}')


# # Ejercicio 02

# print('Qué desea convertir?: \n1)Libras a kilos\n2)Kilos a libras\n3)Euros a dólares\n4)Dólares a euros')

# res = int(input())

# if res == 1:
#     print("Libras: ")
#     lb = float(input())
#     k = lb * 0.453592
#     print(f'{lb} lb son {k} kilos')
# elif res == 2:
#     print("Kilos: ")
#     k = float(input())
#     lb = k * 2.20462
#     print(f'{k} kilos son {lb} libras')
# elif res == 3:
#     print("Euros: ")
#     e = float(input())
#     dolar = e * 1.20
#     print(f'{e} euros son ${dolar}')
# elif res == 4:
#     print("Dólares: ")
#     dolar = float(input())
#     e = dolar * 0.84
#     print(f'${dolar} son {e} euros')
#     dolar = e * 1.20
#     print(f'{e} euros son ${dolar}')

# # Ejercicio 03

# passDefault = "1234"
# salir = False

# while salir == False:
#     print("Ingrese la contraseña: ")
#     passNew = input()

#     if passNew != passDefault:
#         print('Contraseña incorrecta ¿desea intentarlo nuevamente?\n1) Si\n2) No')
#         res = int(input())

#         if res==2:
#             print("Script terminado")
#             break 
#     else:
#         print("Bienvenido al sistema")
#         salir = True

# # Ejercicio 04

# print('Escriba la distancia de su destino en metros: ')
# d = float(input())
# print('Escriba la velocidad que se pretende llevar en m/s: ')
# v = float(input())
# t = d/v
# print(f'El tiempo estimado de llegada es de {t} segundos')

# # Ejercicio 05

# print('Ingrese su peso en kilos: ')
# w = float(input())
# print('Ingrese su estatura en metros ')
# h = float(input())

# imc = w/pow(h,2)

# print(f'Su índice de masa corporal es de {imc}')

# Ejercicio 06

print('Cantidad de dinero a invertir: ')
cantD = float(input())
print('Interés anual: ')
i = float(input())
print('Número de años: ')
years = float(input())

Cf = cantD + (i*years)

print(f'Capital final {Cf}')

