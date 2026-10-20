import tkinter as tk
from tkinter import ttk, messagebox
import requests


# ============================================================
# CONFIGURACIÓN
# ============================================================

API_USUARIO = "http://localhost:3000/usuario"
API_PERSONAS = "http://localhost:3000/personas"


# ============================================================
# COLORES
# ============================================================

AZUL_OSCURO = "#064A9B"
AZUL = "#0875E1"
AZUL_CLARO = "#1976E5"
AZUL_SELECCION = "#167BEA"

AZUL_TITULO = "#0D72DF"
AZUL_SUAVE = "#EAF6FF"

BLANCO = "#FFFFFF"
FONDO = "#F1F9FF"
TEXTO = "#06458F"
BORDE = "#72C5FF"


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def usuario(parent):

    # ========================================================
    # FRAME PRINCIPAL
    # ========================================================

    frame = tk.Frame(
        parent,
        bg=FONDO
    )

    frame.pack(
        fill="both",
        expand=True
    )


    # ========================================================
    # ESTILO DE TABLA
    # ========================================================

    estilo = ttk.Style()

    try:
        estilo.theme_use("clam")
    except:
        pass

    estilo.configure(
        "Usuario.Treeview",
        background=BLANCO,
        foreground=TEXTO,
        fieldbackground=BLANCO,
        rowheight=38,
        font=("Segoe UI", 10),
        borderwidth=0
    )

    estilo.configure(
        "Usuario.Treeview.Heading",
        background="#E1F1FF",
        foreground=TEXTO,
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padding=8
    )

    estilo.map(
        "Usuario.Treeview",
        background=[
            ("selected", "#C8E5FF")
        ],
        foreground=[
            ("selected", TEXTO)
        ]
    )


    # ========================================================
    # SIDEBAR
    # ========================================================

    sidebar = tk.Frame(
        frame,
        bg=AZUL_OSCURO,
        width=275
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)


    # ========================================================
    # LOGO / NOMBRE
    # ========================================================

    logo_frame = tk.Frame(
        sidebar,
        bg=AZUL_OSCURO
    )

    logo_frame.pack(
        fill="x",
        pady=(20, 20)
    )

    tk.Label(
        logo_frame,
        text="⌂",
        font=("Segoe UI Symbol", 34, "bold"),
        fg=BLANCO,
        bg=AZUL_OSCURO
    ).pack(
        side="left",
        padx=(25, 15)
    )

    tk.Label(
        logo_frame,
        text="PROTEC",
        font=("Segoe UI", 17, "bold"),
        fg=BLANCO,
        bg=AZUL_OSCURO
    ).pack(
        side="left"
    )


    # ========================================================
    # BOTONES SIDEBAR
    # ========================================================

    def crear_boton_menu(texto, icono, seleccionado=False):

        boton = tk.Button(
            sidebar,
            text=f"{icono}    {texto}",
            font=("Segoe UI", 11),
            anchor="w",
            padx=20,
            fg=BLANCO,
            bg=AZUL_CLARO if seleccionado else AZUL_OSCURO,
            activebackground=AZUL_SELECCION,
            activeforeground=BLANCO,
            relief="flat",
            bd=0,
            cursor="hand2"
        )

        boton.pack(
            fill="x",
            padx=10,
            pady=2,
            ipady=9
        )

        return boton


    crear_boton_menu(
        "Inicio",
        "⌂"
    )

    crear_boton_menu(
        "Personas",
        "♟"
    )

    crear_boton_menu(
        "Notebooks",
        "▣"
    )

    crear_boton_menu(
        "Préstamos y\ndevoluciones",
        "↔"
    )

    crear_boton_menu(
        "Cargadores",
        "⚡"
    )

    crear_boton_menu(
        "Usuario",
        "⚙",
        True
    )


    # ========================================================
    # ESPACIO DEL SIDEBAR
    # ========================================================

    tk.Frame(
        sidebar,
        bg=AZUL_OSCURO
    ).pack(
        fill="both",
        expand=True
    )


    # ========================================================
    # BOTONES ATRÁS / ADELANTE
    # ========================================================

    separador = tk.Frame(
        sidebar,
        bg=AZUL_OSCURO,
        height=2
    )

    separador.pack(
        fill="x",
        padx=25,
        pady=(0, 15)
    )

    tk.Frame(
        sidebar,
        bg="#2B8CF0",
        height=2
    ).pack(
        fill="x",
        padx=25,
        pady=(0, 15)
    )


    navegacion = tk.Frame(
        sidebar,
        bg=AZUL_OSCURO
    )

    navegacion.pack(
        fill="x",
        pady=(0, 18)
    )


    tk.Button(
        navegacion,
        text="‹",
        font=("Segoe UI", 25, "bold"),
        fg=BLANCO,
        bg=AZUL,
        activebackground=AZUL_CLARO,
        relief="flat",
        bd=0,
        cursor="hand2",
        width=3
    ).pack(
        side="left",
        padx=(35, 8)
    )


    tk.Button(
        navegacion,
        text="›",
        font=("Segoe UI", 25, "bold"),
        fg=BLANCO,
        bg=AZUL,
        activebackground=AZUL_CLARO,
        relief="flat",
        bd=0,
        cursor="hand2",
        width=3
    ).pack(
        side="left"
    )


    # ========================================================
    # CONTENIDO PRINCIPAL
    # ========================================================

    contenido = tk.Frame(
        frame,
        bg=FONDO
    )

    contenido.pack(
        side="left",
        fill="both",
        expand=True,
        padx=15,
        pady=12
    )


    # ========================================================
    # ENCABEZADO
    # ========================================================

    encabezado = tk.Frame(
        contenido,
        bg=AZUL_TITULO
    )

    encabezado.pack(
        fill="x",
        pady=(0, 10)
    )


    tk.Label(
        encabezado,
        text="⚙",
        font=("Segoe UI Symbol", 42),
        fg=BLANCO,
        bg=AZUL_TITULO
    ).pack(
        side="left",
        padx=(25, 18),
        pady=8
    )


    textos_encabezado = tk.Frame(
        encabezado,
        bg=AZUL_TITULO
    )

    textos_encabezado.pack(
        side="left",
        pady=12
    )


    tk.Label(
        textos_encabezado,
        text="Gestión de Usuarios",
        font=("Segoe UI", 23, "bold"),
        fg=BLANCO,
        bg=AZUL_TITULO
    ).pack(
        anchor="w"
    )


    tk.Label(
        textos_encabezado,
        text="Administración de los usuarios del sistema.",
        font=("Segoe UI", 11),
        fg=BLANCO,
        bg=AZUL_TITULO
    ).pack(
        anchor="w"
    )


    # ========================================================
    # PANEL DATOS
    # ========================================================

    panel_datos = tk.Frame(
        contenido,
        bg=BLANCO,
        highlightbackground=BORDE,
        highlightthickness=2
    )

    panel_datos.pack(
        fill="x",
        pady=(0, 10)
    )


    # Título del panel

    tk.Label(
        panel_datos,
        text="Datos del Usuario",
        font=("Segoe UI", 15, "bold"),
        fg=TEXTO,
        bg=AZUL_SUAVE,
        anchor="w"
    ).pack(
        fill="x",
        padx=1,
        pady=1,
        ipady=8
    )


    # ========================================================
    # FORMULARIO
    # ========================================================

    formulario = tk.Frame(
        panel_datos,
        bg=BLANCO
    )

    formulario.pack(
        fill="x",
        padx=22,
        pady=15
    )


    for columna in range(4):

        formulario.columnconfigure(
            columna,
            weight=1
        )


    # ========================================================
    # USUARIO
    # ========================================================

    tk.Label(
        formulario,
        text="Nombre de usuario:",
        font=("Segoe UI", 10, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=5
    )


    entrada_usuario = tk.Entry(
        formulario,
        font=("Segoe UI", 11),
        fg=TEXTO,
        relief="solid",
        bd=1
    )

    entrada_usuario.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=5,
        pady=(5, 12),
        ipady=7
    )


    # ========================================================
    # CONTRASEÑA
    # ========================================================

    tk.Label(
        formulario,
        text="Contraseña:",
        font=("Segoe UI", 10, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=0,
        column=1,
        sticky="w",
        padx=5
    )


    entrada_contrasena = tk.Entry(
        formulario,
        font=("Segoe UI", 11),
        fg=TEXTO,
        relief="solid",
        bd=1,
        show="●"
    )

    entrada_contrasena.grid(
        row=1,
        column=1,
        sticky="ew",
        padx=5,
        pady=(5, 12),
        ipady=7
    )


    # ========================================================
    # ROL
    # ========================================================

    tk.Label(
        formulario,
        text="Rol:",
        font=("Segoe UI", 10, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=0,
        column=2,
        sticky="w",
        padx=5
    )


    combo_rol = ttk.Combobox(
        formulario,
        values=[
            "Administrador",
            "Docente",
            "Estudiante"
        ],
        state="readonly",
        font=("Segoe UI", 10)
    )

    combo_rol.grid(
        row=1,
        column=2,
        sticky="ew",
        padx=5,
        pady=(5, 12),
        ipady=5
    )


    # ========================================================
    # PERSONA
    # ========================================================

    tk.Label(
        formulario,
        text="Persona:",
        font=("Segoe UI", 10, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=0,
        column=3,
        sticky="w",
        padx=5
    )


    combo_persona = ttk.Combobox(
        formulario,
        state="readonly",
        font=("Segoe UI", 10)
    )

    combo_persona.grid(
        row=1,
        column=3,
        sticky="ew",
        padx=5,
        pady=(5, 12),
        ipady=5
    )


    # ========================================================
    # LISTA DE PERSONAS
    # ========================================================

    personas = []


    def cargar_personas():

        nonlocal personas

        try:

            respuesta = requests.get(
                API_PERSONAS,
                timeout=5
            )

            if respuesta.status_code != 200:
                return

            personas = respuesta.json()

            nombres = []

            for persona in personas:

                id_persona = persona.get(
                    "id_persona"
                )

                nombre = persona.get(
                    "nombre",
                    ""
                )

                apellido = persona.get(
                    "apellido",
                    ""
                )

                nombres.append(
                    f"{id_persona} - {nombre} {apellido}"
                )

            combo_persona["values"] = nombres

        except Exception as error:

            print(
                "No se pudieron cargar las personas:",
                error
            )


    # ========================================================
    # OBTENER ID DE PERSONA
    # ========================================================

    def obtener_id_persona():

        valor = combo_persona.get().strip()

        if not valor:
            return None

        try:

            return int(
                valor.split("-")[0].strip()
            )

        except:

            return None


    # ========================================================
    # BOTONES
    # ========================================================

    botones = tk.Frame(
        panel_datos,
        bg=BLANCO
    )

    botones.pack(
        fill="x",
        padx=22,
        pady=(0, 15)
    )


    def crear_boton(
        texto,
        comando
    ):

        return tk.Button(
            botones,
            text=texto,
            command=comando,
            font=("Segoe UI", 10, "bold"),
            fg=BLANCO,
            bg=AZUL,
            activebackground=AZUL_CLARO,
            activeforeground=BLANCO,
            relief="flat",
            bd=0,
            cursor="hand2"
        )


    boton_agregar = crear_boton(
        "＋  Agregar",
        lambda: agregar_usuario()
    )

    boton_agregar.pack(
        side="left",
        fill="x",
        expand=True,
        padx=5,
        ipady=9
    )


    boton_modificar = crear_boton(
        "✎  Modificar",
        lambda: modificar_usuario()
    )

    boton_modificar.pack(
        side="left",
        fill="x",
        expand=True,
        padx=5,
        ipady=9
    )


    boton_eliminar = crear_boton(
        "▣  Eliminar",
        lambda: eliminar_usuario()
    )

    boton_eliminar.pack(
        side="left",
        fill="x",
        expand=True,
        padx=5,
        ipady=9
    )


    boton_limpiar = crear_boton(
        "⟳  Limpiar",
        lambda: limpiar()
    )

    boton_limpiar.pack(
        side="left",
        fill="x",
        expand=True,
        padx=5,
        ipady=9
    )


    # ========================================================
    # PANEL LISTADO
    # ========================================================

    panel_lista = tk.Frame(
        contenido,
        bg=BLANCO,
        highlightbackground=BORDE,
        highlightthickness=2
    )

    panel_lista.pack(
        fill="both",
        expand=True
    )


    tk.Label(
        panel_lista,
        text="Listado de Usuarios",
        font=("Segoe UI", 15, "bold"),
        fg=TEXTO,
        bg=AZUL_SUAVE,
        anchor="w"
    ).pack(
        fill="x",
        padx=1,
        pady=1,
        ipady=8
    )


    # ========================================================
    # TABLA
    # ========================================================

    tabla_frame = tk.Frame(
        panel_lista,
        bg=BLANCO
    )

    tabla_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=12
    )


    columnas = (
        "id",
        "usuario",
        "rol",
        "persona"
    )


    tabla = ttk.Treeview(
        tabla_frame,
        columns=columnas,
        show="headings",
        style="Usuario.Treeview",
        selectmode="browse"
    )


    tabla.heading(
        "id",
        text="ID"
    )

    tabla.heading(
        "usuario",
        text="Usuario"
    )

    tabla.heading(
        "rol",
        text="Rol"
    )

    tabla.heading(
        "persona",
        text="Persona"
    )


    tabla.column(
        "id",
        width=80,
        anchor="center"
    )

    tabla.column(
        "usuario",
        width=250,
        anchor="w"
    )

    tabla.column(
        "rol",
        width=250,
        anchor="w"
    )

    tabla.column(
        "persona",
        width=300,
        anchor="w"
    )


    scrollbar = ttk.Scrollbar(
        tabla_frame,
        orient="vertical",
        command=tabla.yview
    )


    tabla.configure(
        yscrollcommand=scrollbar.set
    )


    tabla.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    # ========================================================
    # TOTAL
    # ========================================================

    total_label = tk.Label(
        panel_lista,
        text="Total de usuarios: 0",
        font=("Segoe UI", 10, "bold"),
        fg=TEXTO,
        bg=AZUL_SUAVE,
        anchor="w"
    )

    total_label.pack(
        fill="x",
        padx=1,
        pady=1,
        ipady=8
    )


    # ========================================================
    # VARIABLES DE DATOS
    # ========================================================

    usuarios = []


    # ========================================================
    # CARGAR USUARIOS
    # ========================================================

    def cargar_usuarios():

        nonlocal usuarios

        try:

            respuesta = requests.get(
                API_USUARIO,
                timeout=5
            )

            if respuesta.status_code != 200:

                messagebox.showerror(
                    "Error",
                    "No se pudieron obtener los usuarios."
                )

                return

            usuarios = respuesta.json()

            mostrar_usuarios()

        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el servidor.\n\n"
                "Verificá que Node.js esté ejecutándose."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # MOSTRAR USUARIOS
    # ========================================================

    def mostrar_usuarios():

        for item in tabla.get_children():

            tabla.delete(item)


        for usuario_data in usuarios:

            id_usuario = usuario_data.get(
                "id_usuario"
            )

            nombre_usuario = usuario_data.get(
                "nombre_usuario",
                ""
            )

            rol = usuario_data.get(
                "rol",
                ""
            )

            id_persona = usuario_data.get(
                "id_persona",
                ""
            )


            nombre_persona = ""

            for persona in personas:

                if str(
                    persona.get("id_persona")
                ) == str(id_persona):

                    nombre_persona = (
                        f"{persona.get('nombre', '')} "
                        f"{persona.get('apellido', '')}"
                    ).strip()

                    break


            if not nombre_persona:

                nombre_persona = f"ID {id_persona}"


            tabla.insert(
                "",
                tk.END,
                iid=str(id_usuario),
                values=(
                    id_usuario,
                    nombre_usuario,
                    rol,
                    nombre_persona
                )
            )


        total_label.config(
            text=f"Total de usuarios: {len(usuarios)}"
        )


    # ========================================================
    # LIMPIAR
    # ========================================================

    def limpiar():

        entrada_usuario.delete(
            0,
            tk.END
        )

        entrada_contrasena.delete(
            0,
            tk.END
        )

        combo_rol.set("")

        combo_persona.set("")

        seleccion = tabla.selection()

        if seleccion:

            tabla.selection_remove(
                seleccion
            )


    # ========================================================
    # AGREGAR
    # ========================================================

    def agregar_usuario():

        nombre_usuario = entrada_usuario.get().strip()
        contrasena = entrada_contrasena.get().strip()
        rol = combo_rol.get().strip()
        id_persona = obtener_id_persona()


        if not nombre_usuario:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingresá el nombre de usuario."
            )

            return


        if not contrasena:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingresá la contraseña."
            )

            return


        if not rol:

            messagebox.showwarning(
                "Datos incompletos",
                "Seleccioná un rol."
            )

            return


        if not id_persona:

            messagebox.showwarning(
                "Datos incompletos",
                "Seleccioná una persona."
            )

            return


        datos = {
            "nombre_usuario": nombre_usuario,
            "contrasena": contrasena,
            "rol": rol,
            "id_persona": id_persona
        }


        try:

            respuesta = requests.post(
                API_USUARIO,
                json=datos,
                timeout=5
            )


            if respuesta.status_code == 201:

                messagebox.showinfo(
                    "Éxito",
                    "Usuario agregado correctamente."
                )

                limpiar()
                cargar_usuarios()

            else:

                try:
                    mensaje = respuesta.json().get(
                        "detalle",
                        respuesta.text
                    )
                except:
                    mensaje = respuesta.text

                messagebox.showerror(
                    "Error",
                    mensaje
                )


        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el servidor."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # MODIFICAR
    # ========================================================

    def modificar_usuario():

        seleccion = tabla.selection()


        if not seleccion:

            messagebox.showwarning(
                "Modificar",
                "Seleccioná un usuario de la tabla."
            )

            return


        id_usuario = seleccion[0]

        nombre_usuario = entrada_usuario.get().strip()
        contrasena = entrada_contrasena.get().strip()
        rol = combo_rol.get().strip()
        id_persona = obtener_id_persona()


        if not nombre_usuario:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingresá el nombre de usuario."
            )

            return


        if not contrasena:

            messagebox.showwarning(
                "Datos incompletos",
                "Ingresá la contraseña."
            )

            return


        if not rol:

            messagebox.showwarning(
                "Datos incompletos",
                "Seleccioná un rol."
            )

            return


        if not id_persona:

            messagebox.showwarning(
                "Datos incompletos",
                "Seleccioná una persona."
            )

            return


        datos = {
            "nombre_usuario": nombre_usuario,
            "contrasena": contrasena,
            "rol": rol,
            "id_persona": id_persona
        }


        try:

            respuesta = requests.put(
                f"{API_USUARIO}/{id_usuario}",
                json=datos,
                timeout=5
            )


            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Éxito",
                    "Usuario actualizado correctamente."
                )

                limpiar()
                cargar_usuarios()

            else:

                try:
                    mensaje = respuesta.json().get(
                        "detalle",
                        respuesta.text
                    )
                except:
                    mensaje = respuesta.text

                messagebox.showerror(
                    "Error",
                    mensaje
                )


        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el servidor."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # ELIMINAR
    # ========================================================

    def eliminar_usuario():

        seleccion = tabla.selection()


        if not seleccion:

            messagebox.showwarning(
                "Eliminar",
                "Seleccioná un usuario de la tabla."
            )

            return


        id_usuario = seleccion[0]


        confirmar = messagebox.askyesno(
            "Eliminar usuario",
            "¿Seguro que querés eliminar este usuario?"
        )


        if not confirmar:

            return


        try:

            respuesta = requests.delete(
                f"{API_USUARIO}/{id_usuario}",
                timeout=5
            )


            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Éxito",
                    "Usuario eliminado correctamente."
                )

                limpiar()
                cargar_usuarios()

            else:

                try:
                    mensaje = respuesta.json().get(
                        "detalle",
                        respuesta.text
                    )
                except:
                    mensaje = respuesta.text

                messagebox.showerror(
                    "Error",
                    mensaje
                )


        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el servidor."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # SELECCIONAR USUARIO DE LA TABLA
    # ========================================================

    def seleccionar_usuario(event):

        seleccion = tabla.selection()


        if not seleccion:
            return


        id_usuario = seleccion[0]


        usuario_seleccionado = None


        for usuario_data in usuarios:

            if str(
                usuario_data.get("id_usuario")
            ) == str(id_usuario):

                usuario_seleccionado = usuario_data
                break


        if not usuario_seleccionado:
            return


        # Usuario

        entrada_usuario.delete(
            0,
            tk.END
        )

        entrada_usuario.insert(
            0,
            usuario_seleccionado.get(
                "nombre_usuario",
                ""
            )
        )


        # Contraseña

        entrada_contrasena.delete(
            0,
            tk.END
        )

        entrada_contrasena.insert(
            0,
            usuario_seleccionado.get(
                "contrasena",
                ""
            )
        )


        # Rol

        combo_rol.set(
            usuario_seleccionado.get(
                "rol",
                ""
            )
        )


        # Persona

        id_persona = usuario_seleccionado.get(
            "id_persona"
        )


        for persona in personas:

            if str(
                persona.get("id_persona")
            ) == str(id_persona):

                nombre = persona.get(
                    "nombre",
                    ""
                )

                apellido = persona.get(
                    "apellido",
                    ""
                )

                combo_persona.set(
                    f"{id_persona} - {nombre} {apellido}"
                )

                break


    tabla.bind(
        "<<TreeviewSelect>>",
        seleccionar_usuario
    )


    # ========================================================
    # CARGA INICIAL
    # ========================================================

    cargar_personas()
    cargar_usuarios()


    # ========================================================
    # RETORNAR FRAME
    # ========================================================

    return frame