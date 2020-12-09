def multiplica(finaliza):

    inicio=1
    while inicio<finaliza:
        yield inicio * 2
        inicio+=1

muestra_tabla=multiplica(10) #guardando objeto iterable

#print(muestra_tabla)

secuencia = 0
for i in muestra_tabla:
    secuencia+=1
    print(2, "*", secuencia, '=', i)