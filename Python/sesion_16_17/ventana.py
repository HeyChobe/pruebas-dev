# Importo la librería
import tkinter as tk

# Creando un contenedor
window = tk.Tk()
window.geometry("500x300") # Dimensiones (alto x ancho)

# Labels
label1 = tk.Label(window, bg="red")
label1.pack(fill = tk.X) # Colocación
# label1.pack(fill = tk.BOTH, expand = True) 
# label1.pack(fill = tk.Y, expand = True) 
# label1.pack(side = tk.BOTTOM)
# label1.pack(side = tk.RIGHT)

# Input
text = tk.Entry(window, font = "Roboto 20") 
text.pack()

def getText():
    valueText = text.get() #Así se obtiene el value
    label1["text"] = valueText #En un label se accede a la propiedad como en diccionarios

# Botones
btn1 = tk.Button(window, text="Click prro", padx= 25, pady= 45, command = getText) #Command es para funciones
btn1.pack()

# Es necesario para controlar el registro de todo lo que sucede en la ventana
window.mainloop()


