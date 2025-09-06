import tkinter as tk
from tkinter import ttk

def main():
    # Crear ventana principal
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("300x250")
    root.resizable(False, False)

    # ===== FRAME PRINCIPAL =====
    mainframe = ttk.Frame(root, padding="10")
    mainframe.pack(fill="both", expand=True)

    # ===== ENTRADAS =====
    ttk.Label(mainframe, text="Número 1:").grid(column=0, row=0, sticky="w")
    entrada1 = ttk.Entry(mainframe, width=15)
    entrada1.grid(column=1, row=0, padx=5, pady=5)

    ttk.Label(mainframe, text="Número 2:").grid(column=0, row=1, sticky="w")
    entrada2 = ttk.Entry(mainframe, width=15)
    entrada2.grid(column=1, row=1, padx=5, pady=5)

    # ===== BOTONES DE OPERACIONES =====
    botones_frame = ttk.Frame(mainframe)
    botones_frame.grid(column=0, row=2, columnspan=2, pady=10)

    ttk.Button(botones_frame, text="Suma").grid(column=0, row=0, padx=5, pady=5)
    ttk.Button(botones_frame, text="Resta").grid(column=1, row=0, padx=5, pady=5)
    ttk.Button(botones_frame, text="Multiplicación").grid(column=0, row=1, padx=5, pady=5)
    ttk.Button(botones_frame, text="División").grid(column=1, row=1, padx=5, pady=5)

    # ===== RESULTADO =====
    ttk.Label(mainframe, text="Resultado:").grid(column=0, row=3, sticky="w", pady=10)
    resultado_label = ttk.Label(mainframe, text="---", font=("Arial", 12, "bold"))
    resultado_label.grid(column=1, row=3, sticky="w")

    root.mainloop()

if __name__ == "__main__":
    main()

