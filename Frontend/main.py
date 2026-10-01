import tkinter as tk
from tkinter import messagebox
from frames.notebooks import crear_notebooks


# =========================
# VENTANA PRINCIPAL
# =========================

ventana = tk.Tk()
ventana.title("Protec - Inicio de sesión")
ventana.geometry("800x600")
ventana.resizable(False, False)

# Colores
AZUL = "#0866E8"
AZUL_OSCURO = "#0645A5"
FONDO = "#F4F1E5"


# =========================
# FUNCIÓN PARA ABRIR NOTEBOOKS
# =========================

def abrir_notebooks():
    # Eliminar todo lo que haya en la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

    frame = crear_notebooks(ventana)
    frame.pack(fill="both", expand=True)


# =========================
# VALIDAR LOGIN
# =========================

def iniciar_sesion():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    # Usuario y contraseña de ejemplo
    if usuario == "admin" and contraseña == "12345678":
        abrir_notebooks()
    else:
        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos."
        )


# =========================
# FONDO ESTILO WINDOWS XP
# =========================

canvas = tk.Canvas(
    ventana,
    width=800,
    height=600,
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)

# Cielo
canvas.create_rectangle(
    0, 0, 800, 600,
    fill="#2D80E8",
    outline=""
)

# Nubes
def nube(x, y):
    canvas.create_oval(
        x, y, x + 80, y + 35,
        fill="white",
        outline=""
    )
    canvas.create_oval(
        x + 25, y - 20, x + 100, y + 35,
        fill="white",
        outline=""
    )
    canvas.create_oval(
        x + 65, y, x + 145, y + 35,
        fill="white",
        outline=""
    )


nube(40, 90)
nube(650, 80)
nube(550, 230)

# Pasto
canvas.create_rectangle(
    0, 430, 800, 600,
    fill="#55A92B",
    outline=""
)

# =========================
# PANEL DE LOGIN
# =========================

panel = tk.Frame(
    ventana,
    bg=FONDO,
    highlightbackground=AZUL_OSCURO,
    highlightthickness=5
)

panel.place(
    x=195,
    y=70,
    width=410,
    height=500
)


# =========================
# BARRA SUPERIOR
# =========================

barra = tk.Frame(
    panel,
    bg=AZUL,
    height=70
)
barra.pack(fill="x")

# Icono
tk.Label(
    barra,
    text="👥",
    font=("Arial", 28),
    bg=AZUL,
    fg="white"
).pack(side="left", padx=15)

tk.Label(
    barra,
    text="Inicio de sesión",
    font=("Arial", 22, "bold"),
    bg=AZUL,
    fg="white"
).pack(side="left")


# Botón X
def cerrar():
    ventana.destroy()


tk.Button(
    barra,
    text="✕",
    command=cerrar,
    font=("Arial", 20, "bold"),
    bg="#F0442E",
    fg="white",
    activebackground="#C92F20",
    activeforeground="white",
    relief="raised",
    bd=2,
    width=3
).pack(side="right", padx=8, pady=10)


# =========================
# IMAGEN / ICONO DE USUARIO
# =========================

usuario_icono = tk.Label(
    panel,
    text="👤",
    font=("Arial", 70),
    bg="#477BC9",
    fg="white",
    width=3,
    height=1,
    relief="solid",
    bd=2
)

usuario_icono.pack(pady=(30, 20))


# =========================
# MENSAJE
# =========================

tk.Label(
    panel,
    text="Bienvenido,\npor favor, inicie sesión\npara continuar.",
    font=("Arial", 18, "bold"),
    bg=FONDO,
    fg="#164B91",
    justify="center"
).pack(pady=(0, 25))


# =========================
# USUARIO
# =========================

tk.Label(
    panel,
    text="Usuario:",
    font=("Arial", 15),
    bg=FONDO,
    anchor="w"
).pack(fill="x", padx=55)

entrada_usuario = tk.Entry(
    panel,
    font=("Arial", 16),
    bd=2,
    relief="solid"
)

entrada_usuario.pack(
    fill="x",
    padx=55,
    pady=(5, 20)
)

entrada_usuario.insert(0, "admin")


# =========================
# CONTRASEÑA
# =========================

tk.Label(
    panel,
    text="Contraseña:",
    font=("Arial", 15),
    bg=FONDO,
    anchor="w"
).pack(fill="x", padx=55)

entrada_contraseña = tk.Entry(
    panel,
    font=("Arial", 16),
    bd=2,
    relief="solid",
    show="●"
)

entrada_contraseña.pack(
    fill="x",
    padx=55,
    pady=(5, 25)
)


# =========================
# BOTÓN INGRESAR
# =========================

boton_ingresar = tk.Button(
    panel,
    text="Ingresar",
    command=iniciar_sesion,
    font=("Arial", 16, "bold"),
    bg=AZUL,
    fg="white",
    activebackground="#0754C5",
    activeforeground="white",
    relief="raised",
    bd=3,
    cursor="hand2"
)

boton_ingresar.pack(
    ipadx=45,
    ipady=8
)


# =========================
# ENTER PARA INICIAR SESIÓN
# =========================

ventana.bind("<Return>", lambda event: iniciar_sesion())

entrada_usuario.focus()

ventana.mainloop()