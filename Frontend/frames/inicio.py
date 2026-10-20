import tkinter as tk

# ============================================================
# IMPORTAR LAS VISTAS
# ============================================================

from frames.personas import crear_personas
from frames.notebooks import crear_notebooks
from frames.cargadores import crear_cargadores
from frames.prestamosydevoluciones import prestamosydevoluciones
from frames.usuario import usuario


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
    # LISTA DE BOTONES
    # ========================================================

    botones_menu = []

    # ========================================================
    # HISTORIAL DE NAVEGACIÓN
    # ========================================================

    historial = []
    posicion_historial = [-1]

    # ========================================================
    # LIMPIAR CONTENIDO
    # ========================================================

    def limpiar_contenido():

        for widget in contenido.winfo_children():
            widget.destroy()

    # ========================================================
    # ACTUALIZAR BOTÓN SELECCIONADO
    # ========================================================

    def actualizar_botones(boton_seleccionado):

        for boton in botones_menu:

            if boton == boton_seleccionado:

                boton.config(
                    bg=AZUL_SELECCIONADO
                )

            else:

                boton.config(
                    bg=AZUL_OSCURO
                )

    # ========================================================
    # MOSTRAR UNA VISTA
    # ========================================================

    def mostrar_pagina(funcion, boton=None, guardar_historial=True):

        # Limpiar la vista actual
        limpiar_contenido()

        # Crear la nueva vista
        nueva_vista = funcion(contenido)

        # Mostrarla
        nueva_vista.pack(
            fill="both",
            expand=True
        )

        # Actualizar botón seleccionado
        if boton is not None:
            actualizar_botones(boton)

        # Guardar navegación
        if guardar_historial:

            # Si estamos retrocediendo y luego elegimos
            # una nueva página, eliminamos el historial futuro.
            if posicion_historial[0] < len(historial) - 1:

                del historial[
                    posicion_historial[0] + 1:
                ]

            historial.append(
                (funcion, boton)
            )

            posicion_historial[0] = len(historial) - 1

    # ========================================================
    # VOLVER ATRÁS
    # ========================================================

    def ir_atras():

        if posicion_historial[0] > 0:

            posicion_historial[0] -= 1

            funcion, boton = historial[
                posicion_historial[0]
            ]

            mostrar_pagina(
                funcion,
                boton,
                guardar_historial=False
            )

    # ========================================================
    # IR ADELANTE
    # ========================================================

    def ir_adelante():

        if posicion_historial[0] < len(historial) - 1:

            posicion_historial[0] += 1

            funcion, boton = historial[
                posicion_historial[0]
            ]

            mostrar_pagina(
                funcion,
                boton,
                guardar_historial=False
            )

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
    # CREAR BOTÓN DEL MENÚ
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
        lambda: mostrar_pagina(
            crear_pagina_inicio,
            boton_inicio
        )
    )

    # ========================================================
    # BOTÓN NOTEBOOKS
    # ========================================================

    boton_notebooks = crear_boton_menu(
        "▣",
        "Notebooks",
        lambda: mostrar_pagina(
            crear_pagina_notebooks,
            boton_notebooks
        )
    )

    # ========================================================
    # BOTÓN CARGADORES
    # ========================================================

    boton_cargadores = crear_boton_menu(
        "🔌",
        "Cargadores",
        lambda: mostrar_pagina(
            crear_pagina_cargadores,
            boton_cargadores
        )
    )

    # ========================================================
    # BOTÓN PERSONAS
    # ========================================================

    boton_personas = crear_boton_menu(
        "👥",
        "Personas",
        lambda: mostrar_pagina(
            crear_pagina_personas,
            boton_personas
        )
    )

    # ========================================================
    # BOTÓN PRÉSTAMOS Y DEVOLUCIONES
    # ========================================================

    boton_prestamos = crear_boton_menu(
        "↔",
        "Préstamos y devoluciones",
        lambda: mostrar_pagina(
            crear_pagina_prestamos,
            boton_prestamos
        )
    )

    # ========================================================
    # BOTÓN USUARIO
    # ========================================================

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

    # --------------------------------------------------------
    # BOTÓN ATRÁS
    # --------------------------------------------------------

    tk.Button(
        botones_inferiores,
        text="<",
        command=ir_atras,
        font=("Arial", 22, "bold"),
        bg=AZUL,
        fg="white",
        activebackground=AZUL_SELECCIONADO,
        activeforeground="white",
        relief="raised",
        bd=2,
        width=3,
        cursor="hand2"
    ).pack(
        side="left",
        padx=(35, 8),
        pady=15
    )

    # --------------------------------------------------------
    # BOTÓN ADELANTE
    # --------------------------------------------------------

    tk.Button(
        botones_inferiores,
        text=">",
        command=ir_adelante,
        font=("Arial", 22, "bold"),
        bg=AZUL,
        fg="white",
        activebackground=AZUL_SELECCIONADO,
        activeforeground="white",
        relief="raised",
        bd=2,
        width=3,
        cursor="hand2"
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

        return crear_notebooks(parent)

    # ========================================================
    # PÁGINA CARGADORES
    # ========================================================

    def crear_pagina_cargadores(parent):

        return crear_cargadores(parent)

    # ========================================================
    # PÁGINA PERSONAS
    # ========================================================

    def crear_pagina_personas(parent):

        return crear_personas(parent)

    # ========================================================
    # PÁGINA PRÉSTAMOS Y DEVOLUCIONES
    # ========================================================

    def crear_pagina_prestamos(parent):

        return prestamosydevoluciones(parent)

    # ========================================================
    # PÁGINA USUARIO
    # ========================================================

    def crear_pagina_usuario(parent):

        return usuario(parent)

    # ========================================================
    # MOSTRAR INICIO AL ENTRAR
    # ========================================================

    mostrar_pagina(
        crear_pagina_inicio,
        boton_inicio
    )

    # ========================================================
    # DEVOLVER FRAME PRINCIPAL
    # ========================================================

    return frame

