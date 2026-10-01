import tkinter as tk
from frames.notebooks import crear_notebooks

ventana = tk.Tk()
ventana.title("Protec")
ventana.geometry("800x500")

def mostrar_frame(funcion_frame):
    for widget in contenedor.winfo_children():
        widget.destroy()
    frame= funcion_frame(contenedor)
    frame.pack(fill="both", expand=True)

def mostrar_menu():
    menu=tk.Frame(ventana, bg="blue", height=60)
    menu.pack(side="top", fill="x")

    global contenedor
    contenedor = tk.Frame(ventana, bg="white")
    contenedor.pack(fill="both", expand=True)

    tk.Button(menu, text="Notebooks", command=lambda:mostrar_frame(crear_notebooks)).pack(side="left", padx=10, pady=10)

mostrar_menu()
ventana.mainloop()