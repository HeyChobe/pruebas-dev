# Ejercicio 1
print("Base: ")
b=float(input())
print("Altura: ")
h=float(input())
area=(b*h)/2
print("Área del triángulo:",area)

# Ejercicio 2
print("Ingrese la cantidad en dólares:")
dolares= float(input())
colones= dolares * 8.75
print(f'${dolares} son {colones} en colones')

# Ejercicio 3
print("Ingrese la cantidad en colones:")
colones= float(input())
dolares= colones * 0.11
print(f'{colones} son {dolares} en colones')

# Ejercicio 4
print('Ingrese la distancia de su destino en metros')
d=float(input())
print('Velocidad que lleva')
v=float(input())
t=d/v
print(f'Se tardará {t} segundos')
