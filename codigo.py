import math
import tkinter as tk
from tkinter import messagebox

def calcular_bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        messagebox.showinfo("Resultado", "A equação não possui raízes reais.")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        messagebox.showinfo("Resultado", f"As raízes da equação são:\nx1 = {x1}\nx2 = {x2}")

def calcular():
    coeficiente_a = float(entry_a.get())
    coeficiente_b = float(entry_b.get())
    coeficiente_c = float(entry_c.get())

    calcular_bhaskara(coeficiente_a, coeficiente_b, coeficiente_c)

# Criação da interface gráfica
window = tk.Tk()
window.title("Calculadora de Bhaskara")

label_a = tk.Label(window, text="Coeficiente a:")
label_a.pack()
entry_a = tk.Entry(window)
entry_a.pack()

label_b = tk.Label(window, text="Coeficiente b:")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()

label_c = tk.Label(window, text="Coeficiente c:")
label_c.pack()
entry_c = tk.Entry(window)
entry_c.pack()

btn_calcular = tk.Button(window, text="Calcular", command=calcular)
btn_calcular.pack()

window.mainloop()
