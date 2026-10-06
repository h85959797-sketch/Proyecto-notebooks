import tkinter as tk
from tkinter import messagebox
import requests

from frames.inicio import crear_inicio


# =========================================================
# FUNCIONES
# =========================================================

def mostrar_inicio():
    global contenedor

    # Eliminar todo lo que haya en la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    # Crear contenedor
    contenedor = tk.Frame(
        ventana,
        bg="#eef1f5"
    )

    contenedor.pack(
        fill="both",
        expand=True
    )

    # Crear pantalla de inicio
    frame_inicio = crear_inicio(contenedor)

    frame_inicio.pack(
        fill="both",
        expand=True
    )


def iniciar_sesion():

    usuario = entrada_usuario.get().strip()
    contraseña = entrada_contraseña.get()

    # Validar campos
    if usuario == "" or contraseña == "":
        messagebox.showwarning(
            "Campos vacíos",
            "Ingrese usuario y contraseña."
        )
        return

    datos = {
        "nombre_usuario": usuario,
        "contrasena": contraseña
    }

    try:

        respuesta = requests.post(
            "http://localhost:3000/api/login",
            json=datos,
            timeout=5
        )

        if respuesta.status_code == 200:

            messagebox.showinfo(
                "Inicio de sesión",
                "¡Bienvenido!"
            )

            mostrar_inicio()

        elif respuesta.status_code == 401:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )

        else:

            messagebox.showerror(
                "Error",
                f"Ocurrió un error al iniciar sesión.\n"
                f"Código: {respuesta.status_code}"
            )

    except requests.exceptions.RequestException:

        messagebox.showerror(
            "Error",
            "No se pudo conectar con el servidor."
        )


def cerrar():
    ventana.destroy()


# =========================================================
# VENTANA PRINCIPAL
# =========================================================

ventana = tk.Tk()

ventana.title("Protec - Inicio de sesión")

# Tamaño de la ventana
ventana.geometry("800x600")

# Evita que el usuario cambie el tamaño y desacomode el diseño
ventana.resizable(False, False)


# =========================================================
# COLORES
# =========================================================

AZUL = "#0866E8"
AZUL_OSCURO = "#0645A5"
FONDO = "#F4F1E5"


# =========================================================
# FONDO ESTILO WINDOWS XP
# =========================================================

canvas = tk.Canvas(
    ventana,
    width=800,
    height=600,
    highlightthickness=0,
    bd=0
)

canvas.place(
    x=0,
    y=0,
    width=800,
    height=600
)


# =========================================================
# CIELO
# =========================================================

canvas.create_rectangle(
    0,
    0,
    800,
    600,
    fill="#2D80E8",
    outline=""
)


# =========================================================
# NUBES
# =========================================================

def nube(x, y):

    canvas.create_oval(
        x,
        y,
        x + 80,
        y + 35,
        fill="white",
        outline=""
    )

    canvas.create_oval(
        x + 25,
        y - 20,
        x + 100,
        y + 35,
        fill="white",
        outline=""
    )

    canvas.create_oval(
        x + 65,
        y,
        x + 145,
        y + 35,
        fill="white",
        outline=""
    )


nube(40, 90)
nube(650, 80)
nube(550, 230)


# =========================================================
# PASTO
# =========================================================

canvas.create_rectangle(
    0,
    430,
    800,
    600,
    fill="#55A92B",
    outline=""
)


# =========================================================
# PANEL DE LOGIN
# =========================================================

panel = tk.Frame(
    ventana,
    bg=FONDO,
    highlightbackground=AZUL_OSCURO,
    highlightcolor=AZUL_OSCURO,
    highlightthickness=4
)

# Panel más compacto para que entre todo
panel.place(
    x=195,
    y=35,
    width=410,
    height=530
)


# =========================================================
# BARRA SUPERIOR
# =========================================================

barra = tk.Frame(
    panel,
    bg=AZUL,
    height=60
)

barra.pack(
    fill="x"
)

barra.pack_propagate(False)


# Icono
tk.Label(
    barra,
    text="👥",
    font=("Arial", 25),
    bg=AZUL,
    fg="white"
).pack(
    side="left",
    padx=12
)


# Título
tk.Label(
    barra,
    text="Inicio de sesión",
    font=("Arial", 20, "bold"),
    bg=AZUL,
    fg="white"
).pack(
    side="left"
)


# Botón X
tk.Button(
    barra,
    text="✕",
    command=cerrar,
    font=("Arial", 16, "bold"),
    bg="#F0442E",
    fg="white",
    activebackground="#C92F20",
    activeforeground="white",
    relief="raised",
    bd=2,
    width=2,
    cursor="hand2"
).pack(
    side="right",
    padx=8,
    pady=8
)


# =========================================================
# ICONO DE USUARIO
# =========================================================

usuario_icono = tk.Label(
    panel,
    text="👤",
    font=("Arial", 55),
    bg="#477BC9",
    fg="white",
    width=3,
    height=1,
    relief="solid",
    bd=2
)

usuario_icono.pack(
    pady=(15, 10)
)


# =========================================================
# MENSAJE DE BIENVENIDA
# =========================================================

tk.Label(
    panel,
    text="Bienvenido,\npor favor, inicie sesión\npara continuar.",
    font=("Arial", 15, "bold"),
    bg=FONDO,
    fg="#164B91",
    justify="center"
).pack(
    pady=(0, 12)
)


# =========================================================
# USUARIO
# =========================================================

tk.Label(
    panel,
    text="Usuario:",
    font=("Arial", 13),
    bg=FONDO,
    anchor="w"
).pack(
    fill="x",
    padx=55
)


entrada_usuario = tk.Entry(
    panel,
    font=("Arial", 14),
    bd=2,
    relief="solid"
)

entrada_usuario.pack(
    fill="x",
    padx=55,
    pady=(3, 12),
    ipady=3
)

entrada_usuario.insert(
    0,
    "admin"
)


# =========================================================
# CONTRASEÑA
# =========================================================

tk.Label(
    panel,
    text="Contraseña:",
    font=("Arial", 13),
    bg=FONDO,
    anchor="w"
).pack(
    fill="x",
    padx=55
)


entrada_contraseña = tk.Entry(
    panel,
    font=("Arial", 14),
    bd=2,
    relief="solid",
    show="●"
)

entrada_contraseña.pack(
    fill="x",
    padx=55,
    pady=(3, 15),
    ipady=3
)


# =========================================================
# BOTÓN INGRESAR
# =========================================================

boton_ingresar = tk.Button(
    panel,
    text="Ingresar",
    command=iniciar_sesion,
    font=("Arial", 15, "bold"),
    bg=AZUL,
    fg="white",
    activebackground="#0754C5",
    activeforeground="white",
    relief="raised",
    bd=3,
    cursor="hand2"
)

boton_ingresar.pack(
    ipadx=40,
    ipady=5
)


# =========================================================
# ENTER PARA INICIAR SESIÓN
# =========================================================

ventana.bind(
    "<Return>",
    lambda event: iniciar_sesion()
)


# =========================================================
# ENFOCAR CAMPO USUARIO
# =========================================================

entrada_usuario.focus()


# =========================================================
# INICIAR APLICACIÓN
# =========================================================

ventana.mainloop()
