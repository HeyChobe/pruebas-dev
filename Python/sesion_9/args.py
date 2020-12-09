# def suma(*args):
#     sumatotal = 0
#     for valoresasumar in args:
#         sumatotal += valoresasumar
#     print(sumatotal)


# sumatotal = suma(10, 15)

# def nombrecompleto(**kwargs):
#     print(kwargs['nombre'])

# nombrecompleto(nombre="Francisco", apellido="Quezada")

def impresionmultiple(obligatorio, *args, **kwargs):
    print(obligatorio)  
    print(args)
    print(kwargs)

impresionmultiple("Valor obligatorio", 5, 4, "lunes",
                  10.5, nombre="Francisco", edad=33)
