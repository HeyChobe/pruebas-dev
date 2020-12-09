print("Ingrese alguna cadena de texto: ")
cadena = input()

# Vocales

a = cadena.lower().count('a')
e = cadena.lower().count('e')
i = cadena.lower().count('i')
o = cadena.lower().count('o')
u = cadena.lower().count('u')

# Boleanos

resHello = "hola" in cadena.lower()
resWelcome = "bienvenido" in cadena.lower()

# Nueva cadena con concatenación
newC = cadena
cant = cadena.count(' ')
i = 0

while i < cant:
    index = newC.index(' ')
    newC = newC[0:index-1] + newC[index+1:]
    i+=1


print(f'Tu cadena de texto fue: {cadena}')
print(f'Cantidad de letras a: {a}')
print(f'Cantidad de letras e: {e}')
print(f'Cantidad de letras i: {i}')
print(f'Cantidad de letras o: {o}')
print(f'Cantidad de letras u: {u}')
print(f'"Hola" se encuentra dentro de la cadena? : {resHello}')
print(f'"Bienvenido" se encuentra dentro de la cadena? : {resWelcome}')
print(f'Tu cadena de texto en minúsculas es {cadena.lower()}')
print(f'Tu cadena de texto en mayúsculas es {cadena.upper()}')
print(f'Tu cadena de texto sin espacios es: {newC}')
