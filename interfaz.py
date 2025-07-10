import tkinter as tk
from tkinter import messagebox
from funciones_db import registrar_cliente

def guardar_cliente():
    nombre = entry_nombre.get()
    whatsapp = entry_whatsapp.get()
    email = entry_email.get()

    if nombre == "":
        messagebox.showwarning("Atención", "El nombre es obligatorio.")
        return

    registrar_cliente(nombre, whatsapp, email)
    messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
    entry_nombre.delete(0, tk.END)
    entry_whatsapp.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def iniciar_interfaz():
    global entry_nombre, entry_whatsapp, entry_email

    ventana = tk.Tk()
    ventana.title("Registro de Clientes - Estética")

    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="WhatsApp:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_whatsapp = tk.Entry(ventana)
    entry_whatsapp.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_email = tk.Entry(ventana)
    entry_email.grid(row=2, column=1, padx=10, pady=5)

    boton_guardar = tk.Button(ventana, text="Guardar Cliente", command=guardar_cliente)
    boton_guardar.grid(row=3, column=0, columnspan=2, pady=10)

    ventana.mainloop()
