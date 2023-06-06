import cmath
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calcular_bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta >= 0:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        resultado = f"As raízes da equação são:\nx1 = {x1:.2f}\nx2 = {x2:.2f}"
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2*a)
        x2 = (-b - cmath.sqrt(delta)) / (2*a)
        resultado = f"As raízes da equação são:\nx1 = {x1:.2f} + {x1.imag:.2f}j\nx2 = {x2:.2f} + {x2.imag:.2f}j\nAs raízes não são reais."

    dialogo_resultado(resultado)

def dialogo_resultado(resultado):
    dialogo = tk.Toplevel()
    dialogo.title("Resultado")
    dialogo.geometry("300x120")
    dialogo.resizable(False, False)
    dialogo.configure(bg="#f0f0f0")

    frame = ttk.Frame(dialogo, padding="20")
    frame.pack(fill="both", expand=True)

    label = ttk.Label(frame, text=resultado)
    label.pack(pady=5)

    btn_ok = ttk.Button(frame, text="OK", command=dialogo.destroy)
    btn_ok.pack(pady=10)

def calcular(event=None):
    try:
        coeficiente_a = float(entry_a.get())
        coeficiente_b = float(entry_b.get())
        coeficiente_c = float(entry_c.get())

        calcular_bhaskara(coeficiente_a, coeficiente_b, coeficiente_c)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para os coeficientes.")

# Criação da interface gráfica
window = tk.Tk()
window.title("Calculadora de Bhaskara")
window.geometry("300x280")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

main_frame = ttk.Frame(window, padding="20")
main_frame.pack(fill="both", expand=True)

label_a = ttk.Label(main_frame, text="Coeficiente a:")
label_a.pack(pady=5)
entry_a = ttk.Entry(main_frame)
entry_a.pack(pady=5)
entry_a.bind("<Return>", calcular)

label_b = ttk.Label(main_frame, text="Coeficiente b:")
label_b.pack(pady=5)
entry_b = ttk.Entry(main_frame)
entry_b.pack(pady=5)
entry_b.bind("<Return>", calcular)

label_c = ttk.Label(main_frame, text="Coeficiente c:")
label_c.pack(pady=5)
entry_c = ttk.Entry(main_frame)
entry_c.pack(pady=5)
entry_c.bind("<Return>", calcular)

btn_calcular = ttk.Button(main_frame, text="Calcular", command=calcular)
btn_calcular.pack(pady=10)

window.mainloop()
