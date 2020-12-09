print('Ingrese su nombre: ')
Name = input()
print('Ingrese su DUI: ')
DUI = input()
print('Ingrese su NIT: ')
NIT = input()
print('Ingrese su sueldo: ')
salary = float(input())
print('Ingrese el monto del bono (si no lo tiene, colocar 0): ')
amount = float(input())

#Cálculo del ISSS
ISSS = 0

#Techo $1000
if salary < 1000:
    ISSS = salary*0.03
else :
    ISSS = 30

#Cálculo del AFP
AFP = 0

#Techo $7028.29
if salary < 7028.29:
    AFP = salary*0.0725
else:
    AFP = 398.57

#Cálculo Renta
RENTA = 0

netSalary = salary - ISSS - AFP

#Techo a partir de $4064
if netSalary > 487.60:
    exceso = netSalary - 487.60 #Salario Neto - Exceso
    RENTA = (exceso*0.10) + 17.48

#Cálculo del salario final
finalSalary = salary - ISSS - AFP - RENTA

print(f'Nombre: {Name}\nDUI: {DUI}\nNIT: {NIT}\nDescuentos:\n\tISSS: ${ISSS}\n\tAFP: ${AFP}\n\tRENTA: ${RENTA}\n\tDescuento Total: ${ISSS + AFP + RENTA}\nBono: ${amount}\nSalario neto: ${finalSalary}\nSalario + bono: {finalSalary + amount}')


