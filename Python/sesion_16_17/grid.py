import tkinter as tk

window = tk.Tk()
window.geometry("500x400")

# btn1 = tk.Button(window, text = "Enviar", width = 10, height = 1)
# caja1 = tk.Entry(window, font = "Arial 15")
# btn2 = tk.Button(window, text = "Borrar", width = 10, height = 2)
# texto1 = tk.Label(window, text = "Python 3")

# texto1.grid(row = 0, column = 0)
# caja1.grid(row = 1, column = 0)
# btn1.grid(row = 1, column = 1)
# btn2.grid(row = 2, column = 0)

btn1 = tk.Button(window, text = "Botón 1", width = 10, height = 5)
btn2 = tk.Button(window, text = "Botón 2", width = 10, height = 5)
btn3 = tk.Button(window, text = "Botón 3", width = 10, height = 5)
btn4 = tk.Button(window, text = "Botón 4", width = 10, height = 5)
btn5 = tk.Button(window, text = "Botón 5", width = 10, height = 5)

btn1.grid(row = 0, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 2, column = 2)
btn4.grid(row = 2, column = 0)
btn5.grid(row = 0, column = 2)

window.mainloop()