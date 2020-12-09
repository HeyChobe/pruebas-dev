def cuadrado(numero):
    return numero * numero

lista = [1,2,3,4,5]

#map(función, iterables)
resultado = map(cuadrado, lista)

#Convirtiendolo en una lista nueva
lista_resultado = list(resultado)
print(lista_resultado)