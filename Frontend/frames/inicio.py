import tkinter as tk
from frames.personas import crear_personas


# ============================================================
# COLORES
# ============================================================

AZUL = "#0866E8"
AZUL_OSCURO = "#0645A5"
AZUL_SELECCIONADO = "#3185EE"
FONDO = "#F4F1E5"


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def crear_inicio(parent):

    # ========================================================
    # FRAME PRINCIPAL
    # ========================================================

    frame = tk.Frame(
        parent,
        bg=FONDO
    )

    def abrir_personas():
        vent = tk.Toplevel(frame)
        vent.geometry("1000x650")
        frame_personas=crear_personas(vent)
        frame_personas.pack(
            fill="both",
            expand=True
        )
    abrir_personas()

    # ========================================================
    # CONTENEDOR DE LA APLICACIÓN
    # ========================================================

    aplicacion = tk.Frame(
        frame,
        bg=FONDO
    )

    aplicacion.pack(
        fill="both",
        expand=True
    )

    # ========================================================
    # MENÚ LATERAL
    # ========================================================

    menu_lateral = tk.Frame(
        aplicacion,
        bg=AZUL_OSCURO,
        width=270
    )

    menu_lateral.pack(
        side="left",
        fill="y"
    )

    menu_lateral.pack_propagate(False)

    # ========================================================
    # CONTENEDOR DEL CONTENIDO
    # ========================================================

    contenido = tk.Frame(
        aplicacion,
        bg=FONDO
    )

    contenido.pack(
        side="left",
        fill="both",
        expand=True
    )

    # ========================================================
    # FUNCIONES DE NAVEGACIÓN
    # ========================================================

    def limpiar_contenido():

        for widget in contenido.winfo_children():
            widget.destroy()

    def actualizar_botones(boton_seleccionado):

        for boton in botones_menu:
            boton.config(
                bg=AZUL_SELECCIONADO
                if boton == boton_seleccionado
                else AZUL_OSCURO
            )

    def mostrar_pagina(funcion, boton=None):

        limpiar_contenido()

        nuevo_frame = funcion(contenido)

        nuevo_frame.pack(
            fill="both",
            expand=True
        )

        if boton is not None:
            actualizar_botones(boton)

    # ========================================================
    # ENCABEZADO DEL MENÚ
    # ========================================================

    encabezado_menu = tk.Frame(
        menu_lateral,
        bg=AZUL_OSCURO,
        height=130
    )

    encabezado_menu.pack(
        fill="x"
    )

    encabezado_menu.pack_propagate(False)

    tk.Label(
        encabezado_menu,
        text="⌂",
        font=("Arial", 42, "bold"),
        bg=AZUL_OSCURO,
        fg="white"
    ).pack(
        pady=(10, 0)
    )

    tk.Label(
        encabezado_menu,
        text="PROTEC",
        font=("Arial", 21, "bold"),
        bg=AZUL_OSCURO,
        fg="white"
    ).pack()

    # ========================================================
    # LISTA DE BOTONES
    # ========================================================

    botones_menu = []

    # ========================================================
    # CREAR BOTÓN
    # ========================================================

    def crear_boton_menu(icono, texto, comando):

        boton = tk.Button(
            menu_lateral,
            text=f"{icono}   {texto}",
            command=comando,
            font=("Arial", 14, "bold"),
            bg=AZUL_OSCURO,
            fg="white",
            activebackground=AZUL_SELECCIONADO,
            activeforeground="white",
            relief="flat",
            bd=0,
            anchor="w",
            padx=18,
            cursor="hand2"
        )

        boton.pack(
            fill="x",
            padx=10,
            pady=4,
            ipady=12
        )

        botones_menu.append(boton)

        return boton

    # ========================================================
    # BOTÓN INICIO
    # ========================================================

    boton_inicio = crear_boton_menu(
        "⌂",
        "Inicio",
        lambda: mostrar_pagina(crear_pagina_inicio, boton_inicio)
    )

    # ========================================================
    # BOTÓN NOTEBOOKS
    # ========================================================

    boton_notebooks = crear_boton_menu(
        "▣",
        "Notebooks",
        lambda: mostrar_pagina(crear_pagina_notebooks, boton_notebooks)
    )

    # ========================================================
    # BOTONES PROVISORIOS
    # ========================================================

    boton_cargadores = crear_boton_menu(
        "🔌",
        "Cargadores",
        lambda: mostrar_pagina(
            crear_pagina_cargadores,
            boton_cargadores
        )
    )

    boton_personas = crear_boton_menu(
        "👥",
        "Personas",
        lambda: mostrar_pagina(
            crear_pagina_personas,
            boton_personas
        )
    )

    boton_prestamos = crear_boton_menu(
        "↔",
        "Préstamos y devoluciones",
        lambda: mostrar_pagina(
            crear_pagina_prestamos,
            boton_prestamos
        )
    )

    boton_usuario = crear_boton_menu(
        "⚙",
        "Usuario",
        lambda: mostrar_pagina(
            crear_pagina_usuario,
            boton_usuario
        )
    )

    # ========================================================
    # ESPACIO INFERIOR
    # ========================================================

    espacio = tk.Frame(
        menu_lateral,
        bg=AZUL_OSCURO
    )

    espacio.pack(
        fill="both",
        expand=True
    )

    # ========================================================
    # BOTONES INFERIORES
    # ========================================================

    botones_inferiores = tk.Frame(
        menu_lateral,
        bg=AZUL_OSCURO,
        height=80
    )

    botones_inferiores.pack(
        side="bottom",
        fill="x"
    )

    botones_inferiores.pack_propagate(False)

    tk.Button(
        botones_inferiores,
        text="<",
        font=("Arial", 22, "bold"),
        bg=AZUL,
        fg="white",
        activebackground=AZUL_SELECCIONADO,
        activeforeground="white",
        relief="raised",
        bd=2,
        width=3
    ).pack(
        side="left",
        padx=(35, 8),
        pady=15
    )

    tk.Button(
        botones_inferiores,
        text=">",
        font=("Arial", 22, "bold"),
        bg=AZUL,
        fg="white",
        activebackground=AZUL_SELECCIONADO,
        activeforeground="white",
        relief="raised",
        bd=2,
        width=3
    ).pack(
        side="left",
        padx=8,
        pady=15
    )

    # ========================================================
    # PÁGINA DE INICIO
    # ========================================================

    def crear_pagina_inicio(parent):

        panel = tk.Frame(
            parent,
            bg=FONDO
        )

        # ----------------------------------------------------
        # ENCABEZADO
        # ----------------------------------------------------

        encabezado = tk.Frame(
            panel,
            bg=AZUL,
            height=70
        )

        encabezado.pack(
            fill="x"
        )

        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="⌂",
            font=("Arial", 38, "bold"),
            bg=AZUL,
            fg="white"
        ).pack(
            side="left",
            padx=(25, 15)
        )

        tk.Label(
            encabezado,
            text="Menú principal",
            font=("Arial", 24, "bold"),
            bg=AZUL,
            fg="white"
        ).pack(
            side="left"
        )

        # ----------------------------------------------------
        # PANEL CENTRAL
        # ----------------------------------------------------

        panel_inicio = tk.Frame(
            panel,
            bg=FONDO,
            bd=1,
            relief="solid"
        )

        panel_inicio.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # ----------------------------------------------------
        # CABECERA
        # ----------------------------------------------------

        titulo_inicio = tk.Frame(
            panel_inicio,
            bg=AZUL,
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
            bg=AZUL,
            fg="white"
        ).pack(
            side="left",
            padx=(25, 15)
        )

        tk.Label(
            titulo_inicio,
            text="Inicio",
            font=("Arial", 28, "bold"),
            bg=AZUL,
            fg="white"
        ).pack(
            side="left"
        )

        # ----------------------------------------------------
        # BIENVENIDA
        # ----------------------------------------------------

        bienvenida = tk.Frame(
            panel_inicio,
            bg=FONDO
        )

        bienvenida.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            bienvenida,
            text="🖥️\n👥",
            font=("Arial", 65),
            bg=FONDO,
            fg=AZUL,
            justify="center"
        ).place(
            relx=0.30,
            rely=0.40,
            anchor="center"
        )

        tk.Label(
            bienvenida,
            text="¡Bienvenido!",
            font=("Arial", 32, "bold"),
            bg=FONDO,
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
            font=("Arial", 17),
            bg=FONDO,
            fg="#0754C5",
            justify="left"
        ).place(
            relx=0.63,
            rely=0.48,
            anchor="center"
        )

        return panel

    # ========================================================
    # PÁGINA NOTEBOOKS
    # ========================================================

    def crear_pagina_notebooks(parent):

        from frames.notebooks import crear_notebooks

        return crear_notebooks(parent)

    # ========================================================
    # PÁGINAS PROVISORIAS
    # ========================================================

    def crear_pagina_cargadores(parent):

        return crear_pagina_provisoria(
            parent,
            "🔌",
            "Cargadores"
        )

    def crear_pagina_personas(parent):

        return crear_pagina_provisoria(
            parent,
            "👥",
            "Personas"
        )

    def crear_pagina_prestamos(parent):

        return crear_pagina_provisoria(
            parent,
            "↔",
            "Préstamos y devoluciones"
        )

    def crear_pagina_usuario(parent):

        return crear_pagina_provisoria(
            parent,
            "⚙",
            "Usuario"
        )

    def crear_pagina_provisoria(parent, icono, titulo):

        pagina = tk.Frame(
            parent,
            bg=FONDO
        )

        encabezado = tk.Frame(
            pagina,
            bg=AZUL,
            height=70
        )

        encabezado.pack(
            fill="x"
        )

        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text=icono,
            font=("Arial", 35),
            bg=AZUL,
            fg="white"
        ).pack(
            side="left",
            padx=25
        )

        tk.Label(
            encabezado,
            text=titulo,
            font=("Arial", 24, "bold"),
            bg=AZUL,
            fg="white"
        ).pack(
            side="left"
        )

        tk.Label(
            pagina,
            text=f"{titulo}\n\nPágina en construcción",
            font=("Arial", 25, "bold"),
            bg=FONDO,
            fg="#0754C5",
            justify="center"
        ).pack(
            expand=True
        )

        return pagina

    # ========================================================
    # MOSTRAR INICIO AL ENTRAR
    # ========================================================

    mostrar_pagina(
        crear_pagina_inicio,
        boton_inicio
    )

    return frame