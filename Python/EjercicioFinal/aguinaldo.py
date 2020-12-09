import tkinter as tk

# Excepción para cuando hayan campos vacíos
class EmptyValue(Exception):
    pass

# Excepción para la falta de caracteres en DUI y en NIT
class NumberOfChars(Exception):
    pass

# Excepción para verficiar si se ha colocado correctamente un DUI o NIT
class IsNotADuiOrNit(Exception):
    pass

# Ventana principal
root = tk.Tk()
root.geometry("400x390")
root.title("Cálculo de aguinaldo")
root.resizable(0, 0)  # No permite aumentar el tamaño

# Función que calcula el aguinaldo
def onClickButton():
    # Manejo de excepciones
    try:
        NAME = txt_name.get()
        DUI = txt_dui.get()
        NIT = txt_nit.get()
        SALARY = float(txt_salary.get())
        DAYS = int(txt_days_work.get())
        dailySalary = SALARY/30
        bonus = 0

        # Lanzando EmptyValue si hay campos vacíos
        if NAME == '' or DUI == '' or NIT == '' or SALARY == '' or DAYS == '':
            raise EmptyValue

        # Lanzando NumberOfChars si la cantidad de caractares en DUI o NIT no son los adecuados
        if len(DUI) != 10 or len(NIT) != 17:
            raise NumberOfChars

        # Lanzando IsNotADuiOrNit si en el recorrido de las cadenas obtenidas no se encuentra un valor numérico o un "-"
        if DUI[8] != "-" or (NIT[4] != "-" and NIT[11] != "-" and NIT[15] != "-"):
            raise IsNotADuiOrNit
        
        i=0
        while i < len(DUI):
            if DUI[i] == "-" or DUI[i].isdecimal():
                i+=1
            else:
                raise IsNotADuiOrNit

        j=0
        while j < len(NIT):
            if NIT[i] == "-" or NIT[i].isdecimal():
                j+=1
            else:
                raise IsNotADuiOrNit

        # Menor que un año de trabajo
        if DAYS < 365:
            salaryPerDay = (dailySalary*15)/365
            bonus = salaryPerDay * DAYS

        # De 1 año y menos de 3 años de trabajo
        elif DAYS >= 365 and DAYS < 1098:
            bonus = dailySalary*15

        # De 3 años y menos de 10 años de trabajo
        elif DAYS >= 1098 and DAYS < 3660:
            bonus = dailySalary*19

        # De 10 años de trabajo en adelante
        elif DAYS >= 3660:
            bonus = dailySalary*21

        # Actualizando la etiqueta que muestra un posible error
        lbl_error["text"] = ''

        # Abriendo la ventana de resultados
        result = tk.Toplevel(root)
        result.geometry("400x190")
        result.title("Resultado Aguinaldo")
        result.resizable(0, 0)  # No permite aumentar el tamaño

        # Etiquetas para mostrar el resultado
        lbl_name = tk.Label(result, text= f"Nombre Completo: {NAME}", font="Roboto 18")
        lbl_dui = tk.Label(result, text= f"DUI: {DUI}", font="Roboto 18")
        lbl_nit = tk.Label(result, text= f"NIT: {NIT}", font="Roboto 18")
        lbl_salary = tk.Label(result, text= f"Salario neto mensual: ${SALARY}", font="Roboto 18")
        lbl_days_work = tk.Label(
        result, text= f"Días trabajados en la empresa: {DAYS}", font="Roboto 18")
        lbl_bonus = tk.Label(result, text= f"Aguinaldo a recibir: ${bonus}", font="Roboto 18")

        lbl_name.pack()
        lbl_dui.pack()
        lbl_nit.pack()
        lbl_salary.pack()
        lbl_days_work.pack()
        lbl_bonus.pack()

    except ValueError:
        lbl_error["text"] = "ERROR: Valor no numérico en el salario y/o días trabajados"

    except EmptyValue:
        lbl_error["text"] = "ERROR: Campos vacíos"

    except NumberOfChars:
        lbl_error["text"] = "ERROR: El número de caracteres en DUI y/o NIT son incorrectos"

    except IsNotADuiOrNit:
        lbl_error["text"] = "ERROR: Su DUI y/o NIT fueron escritos incorrectamente"


# Etiquetas
lbl_name = tk.Label(root, text="Nombre Completo:", font="Roboto 18")
lbl_dui = tk.Label(root, text="DUI:", font="Roboto 18")
lbl_nit = tk.Label(root, text="NIT:", font="Roboto 18")
lbl_salary = tk.Label(root, text="Salario neto mensual ($):", font="Roboto 18")
lbl_days_work = tk.Label(root, text="Días trabajados en la empresa:", font="Roboto 18")
lbl_error = tk.Label(root, font='Roboto 12', fg="red")

# Entradas de Texto
txt_name = tk.Entry(root, font="Roboto 16", justify="center", fg="white", width=30, bg="#ACACAC")
txt_dui = tk.Entry(root, font="Roboto 16", justify="center", fg="#C8C8C8", width=30, bg="#ACACAC")
txt_nit = tk.Entry(root, font="Roboto 16", justify="center", fg="#C8C8C8", width=30, bg="#ACACAC")
txt_salary = tk.Entry(root, font="Roboto 16", justify="center", fg="white", width=30, bg="#ACACAC")
txt_days_work = tk.Entry(root, font="Roboto 16", justify="center", fg="white", width=30, bg="#ACACAC")

# PlaceHolder de los Entry al inicio del programa
txt_dui.insert(0, 'Ej: 06096092-7')
txt_nit.insert(0, 'Ej: 0604-280800-138-2')

# Al darle click a los Entry, borra el "PlaceHolder" que tenían como ejemplo
def clickDui(event):
    txt_dui.delete(0, 'end')
    txt_dui["fg"] = "white"


def clickNit(event):
    txt_nit.delete(0, 'end')
    txt_nit["fg"] = "white"

txt_dui.bind('<Button-1>', clickDui)
txt_nit.bind('<Button-1>', clickNit)

# Botón
btn_calculate = tk.Button(root, text="Calcular Aguinaldo", width="20", height="3", justify="center", font="Roboto 18 bold", command=onClickButton)

# Posicionamiento de los widgets
lbl_name.pack()
txt_name.pack()
lbl_dui.pack()
txt_dui.pack()
lbl_nit.pack()
txt_nit.pack()
lbl_salary.pack()
txt_salary.pack()
lbl_days_work.pack()
txt_days_work.pack()
lbl_error.pack()
btn_calculate.pack(side=tk.BOTTOM)

root.mainloop()
