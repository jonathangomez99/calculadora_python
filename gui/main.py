import tkinter as tk
from tkinter import ttk
from operaciones import suma, resta, multiplicacion, division
from validaciones import es_numero

def obtener_valores():
    """Obtiene y valida los valores de los Entry"""
    try:
        a = es_numero(entry_a.get())
        b = es_numero(entry_b.get())
        return a, b
    except ValueError as e:
        label_result.config(text=str(e))
        return None, None

def operar_suma():
    a, b = obtener_valores()
    if a is not None and b is not None:
        resultado = suma(a, b)
        label_result.config(text=f"Resultado: {resultado}")

def operar_resta():
    a, b = obtener_valores()
    if a is not None and b is not None:
        resultado = resta(a, b)
        label_result.config(text=f"Resultado: {resultado}")

def operar_multiplicacion():
    a, b = obtener_valores()
    if a is not None and b is not None:
        resultado = multiplicacion(a, b)
        label_result.config(text=f"Resultado: {resultado}")

def operar_division():
    a, b = obtener_valores()
    if a is not None and b is not None:
        try:
            resultado = division(a, b)
            label_result.config(text=f"Resultado: {resultado}")
        except ValueError as e:
            label_result.config(text=str(e))

# ---------- Interfaz ----------

root = tk.Tk()
root.title("Calculadora Python")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

# Entradas
ttk.Label(frame, text="Número A:").grid(row=0, column=0, sticky="w")
entry_a = ttk.Entry(frame, width=15)
entry_a.grid(row=0, column=1)

ttk.Label(frame, text="Número B:").grid(row=1, column=0, sticky="w")
entry_b = ttk.Entry(frame, width=15)
entry_b.grid(row=1, column=1)

# Botones
ttk.Button(frame, text="Sumar", command=operar_suma).grid(row=2, column=0, pady=5)
ttk.Button(frame, text="Restar", command=operar_resta).grid(row=2, column=1, pady=5)
ttk.Button(frame, text="Multiplicar", command=operar_multiplicacion).grid(row=3, column=0, pady=5)
ttk.Button(frame, text="Dividir", command=operar_division).grid(row=3, column=1, pady=5)

# Resultado
label_result = ttk.Label(frame, text="", foreground="blue")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
