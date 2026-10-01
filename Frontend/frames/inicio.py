import tkinter as tk


def crear_inicio(parent):

    # =========================
    # FRAME PRINCIPAL
    # =========================

    frame = tk.Frame(
        parent,
        bg="#F4F1E5"
    )

    # =========================
    # ENCABEZADO
    # =========================

    encabezado = tk.Frame(
        frame,
        bg="#0866E8",
        height=70
    )
    encabezado.pack(
        side="top",
        fill="x"
    )

    tk.Label(
        encabezado,
        text="⌂",
        font=("Arial", 38, "bold"),
        bg="#0866E8",
        fg="white"
    ).pack(
        side="left",
        padx=(20, 10)
    )

    tk.Label(
        encabezado,
        text="Menú principal",
        font=("Arial", 24, "bold"),
        bg="#0866E8",
        fg="white"
    ).pack(
        side="left"
    )

    # =========================
    # CONTENIDO
    # =========================

    contenido = tk.Frame(
        frame,
        bg="#F4F1E5"
    )
    contenido.pack(
        fill="both",
        expand=True
    )

    # =========================
    # MENÚ LATERAL
    # =========================

    menu_lateral = tk.Frame(
        contenido,
        bg="#0645A5",
        width=270
    )
    menu_lateral.pack(
        side="left",
        fill="y"
    )

    menu_lateral.pack_propagate(False)

    # -------- BOTONES DEL MENÚ --------

    def crear_boton_menu(icono, texto, seleccionado=False):

        color = "#3185EE" if seleccionado else "#0645A5"

        boton = tk.Frame(
            menu_lateral,
            bg=color,
            height=80
        )

        boton.pack(
            fill="x",
            padx=10,
            pady=5
        )

        boton.pack_propagate(False)

        tk.Label(
            boton,
            text=icono,
            font=("Arial", 30),
            bg=color,
            fg="white",
            width=3
        ).pack(
            side="left",
            padx=(5, 5)
        )

        tk.Label(
            boton,
            text=texto,
            font=("Arial", 16),
            bg=color,
            fg="white",
            justify="left",
            anchor="w"
        ).pack(
            side="left",
            fill="both",
            expand=True
        )

    crear_boton_menu("⌂", "Inicio", True)
    crear_boton_menu("▣", "Notebooks")
    crear_boton_menu("🔌", "Cargadores")
    crear_boton_menu("👥", "Personas")
    crear_boton_menu("↔", "Préstamos y\ndevoluciones")
    crear_boton_menu("⚙", "Usuario")

    # =========================
    # BOTONES INFERIORES
    # =========================

    espacio = tk.Frame(
        menu_lateral,
        bg="#0645A5"
    )
    espacio.pack(
        fill="both",
        expand=True
    )

    botones_inferiores = tk.Frame(
        menu_lateral,
        bg="#0645A5",
        height=90
    )
    botones_inferiores.pack(
        side="bottom",
        fill="x"
    )

    tk.Button(
        botones_inferiores,
        text="<",
        font=("Arial", 25, "bold"),
        bg="#0866E8",
        fg="white",
        activebackground="#3185EE",
        activeforeground="white",
        relief="raised",
        bd=2,
        width=4
    ).pack(
        side="left",
        padx=(30, 10),
        pady=15
    )

    tk.Button(
        botones_inferiores,
        text=">",
        font=("Arial", 25, "bold"),
        bg="#0866E8",
        fg="white",
        activebackground="#3185EE",
        activeforeground="white",
        relief="raised",
        bd=2,
        width=4
    ).pack(
        side="left",
        padx=10,
        pady=15
    )

    # =========================
    # PANEL DE INICIO
    # =========================

    panel_inicio = tk.Frame(
        contenido,
        bg="#F4F1E5",
        bd=1,
        relief="solid"
    )

    panel_inicio.pack(
        side="left",
        fill="both",
        expand=True,
        padx=20,
        pady=15
    )

    # =========================
    # CABECERA DEL PANEL
    # =========================

    titulo_inicio = tk.Frame(
        panel_inicio,
        bg="#0866E8",
        height=70
    )

    titulo_inicio.pack(
        fill="x"
    )

    titulo_inicio.pack_propagate(False)

    tk.Label(
        titulo_inicio,
        text="⌂",
        font=("Arial", 38, "bold"),
        bg="#0866E8",
        fg="white"
    ).pack(
        side="left",
        padx=(25, 15)
    )

    tk.Label(
        titulo_inicio,
        text="Inicio",
        font=("Arial", 28, "bold"),
        bg="#0866E8",
        fg="white"
    ).pack(
        side="left"
    )

    # =========================
    # ZONA DE BIENVENIDA
    # =========================

    bienvenida = tk.Frame(
        panel_inicio,
        bg="#F4F1E5"
    )

    bienvenida.pack(
        fill="both",
        expand=True
    )

    # Imagen representada con iconos
    imagen = tk.Label(
        bienvenida,
        text="🖥️\n👥",
        font=("Arial", 70),
        bg="#F4F1E5",
        fg="#0866E8",
        justify="center"
    )

    imagen.place(
        relx=0.30,
        rely=0.40,
        anchor="center"
    )

    # Texto de bienvenida
    tk.Label(
        bienvenida,
        text="¡Bienvenido!",
        font=("Arial", 32, "bold"),
        bg="#F4F1E5",
        fg="#0754C5"
    ).place(
        relx=0.63,
        rely=0.30,
        anchor="center"
    )

    tk.Label(
        bienvenida,
        text=(
            "Desde este sistema podés gestionar\n"
            "las notebooks, cargadores, personas\n"
            "y préstamos de la empresa."
        ),
        font=("Arial", 18),
        bg="#F4F1E5",
        fg="#0754C5",
        justify="left"
    ).place(
        relx=0.63,
        rely=0.48,
        anchor="center"
    )

    return frame