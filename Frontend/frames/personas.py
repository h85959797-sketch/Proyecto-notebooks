import tkinter as tk
from tkinter import ttk, messagebox
import requests


# =========================================================
# CONFIGURACIÓN DE LA API
# =========================================================

API_URL = "http://localhost:3000/personas"


# =========================================================
# CREAR INTERFAZ PERSONAS
# =========================================================

def crear_personas(parent):

    # =====================================================
    # FRAME PRINCIPAL
    # =====================================================

    frame = tk.Frame(
        parent,
        bg="#eef6ff"
    )

    frame.pack(
        fill="both",
        expand=True
    )


    # =====================================================
    # ENCABEZADO
    # =====================================================

    encabezado = tk.Frame(
        frame,
        bg="#eef6ff",
        height=70
    )

    encabezado.pack(
        fill="x",
        padx=15,
        pady=(10, 5)
    )

    encabezado.pack_propagate(False)


    # Icono
    icono = tk.Label(
        encabezado,
        text="👥",
        font=("Segoe UI", 25),
        bg="#1674d1",
        fg="white",
        width=3
    )

    icono.pack(
        side="left",
        padx=(0, 12)
    )


    # Título
    textos = tk.Frame(
        encabezado,
        bg="#eef6ff"
    )

    textos.pack(
        side="left",
        fill="y"
    )

    titulo = tk.Label(
        textos,
        text="Gestión de Personas",
        font=("Segoe UI", 16, "bold"),
        fg="#0057b8",
        bg="#eef6ff"
    )

    titulo.pack(
        anchor="w"
    )


    subtitulo = tk.Label(
        textos,
        text="Registro y administración de las personas.",
        font=("Segoe UI", 9),
        fg="#0066cc",
        bg="#eef6ff"
    )

    subtitulo.pack(
        anchor="w"
    )


    # =====================================================
    # VARIABLES
    # =====================================================

    id_seleccionado = tk.StringVar()

    nombre_var = tk.StringVar()
    apellido_var = tk.StringVar()
    dni_var = tk.StringVar()
    tipo_var = tk.StringVar()
    email_var = tk.StringVar()
    curso_var = tk.StringVar()


    # =====================================================
    # FRAME FORMULARIO
    # =====================================================

    formulario = tk.LabelFrame(
        frame,
        text="Datos de la persona",
        font=("Segoe UI", 9, "bold"),
        fg="#0057b8",
        bg="#eef6ff",
        bd=1,
        relief="solid"
    )

    formulario.pack(
        fill="x",
        padx=15,
        pady=5
    )


    # =====================================================
    # ESTILO DE LABELS
    # =====================================================

    estilo_label = {
        "font": ("Segoe UI", 8, "bold"),
        "fg": "#003b73",
        "bg": "#eef6ff"
    }


    # =====================================================
    # NOMBRE
    # =====================================================

    tk.Label(
        formulario,
        text="Nombre:",
        **estilo_label
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=10,
        pady=(8, 2)
    )

    entrada_nombre = tk.Entry(
        formulario,
        textvariable=nombre_var,
        font=("Segoe UI", 9),
        relief="solid",
        bd=1
    )

    entrada_nombre.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=10,
        pady=(0, 8)
    )


    # =====================================================
    # APELLIDO
    # =====================================================

    tk.Label(
        formulario,
        text="Apellido:",
        **estilo_label
    ).grid(
        row=0,
        column=1,
        sticky="w",
        padx=10,
        pady=(8, 2)
    )

    entrada_apellido = tk.Entry(
        formulario,
        textvariable=apellido_var,
        font=("Segoe UI", 9),
        relief="solid",
        bd=1
    )

    entrada_apellido.grid(
        row=1,
        column=1,
        sticky="ew",
        padx=10,
        pady=(0, 8)
    )


    # =====================================================
    # DNI
    # =====================================================

    tk.Label(
        formulario,
        text="DNI:",
        **estilo_label
    ).grid(
        row=0,
        column=2,
        sticky="w",
        padx=10,
        pady=(8, 2)
    )

    entrada_dni = tk.Entry(
        formulario,
        textvariable=dni_var,
        font=("Segoe UI", 9),
        relief="solid",
        bd=1
    )

    entrada_dni.grid(
        row=1,
        column=2,
        sticky="ew",
        padx=10,
        pady=(0, 8)
    )


    # =====================================================
    # TIPO
    # =====================================================

    tk.Label(
        formulario,
        text="Tipo:",
        **estilo_label
    ).grid(
        row=0,
        column=3,
        sticky="w",
        padx=10,
        pady=(8, 2)
    )

    combo_tipo = ttk.Combobox(
        formulario,
        textvariable=tipo_var,
        values=[
            "Estudiante",
            "Docente"
        ],
        state="readonly",
        font=("Segoe UI", 9)
    )

    combo_tipo.grid(
        row=1,
        column=3,
        sticky="ew",
        padx=10,
        pady=(0, 8)
    )


    # =====================================================
    # EMAIL
    # =====================================================

    tk.Label(
        formulario,
        text="Email:",
        **estilo_label
    ).grid(
        row=2,
        column=0,
        columnspan=2,
        sticky="w",
        padx=10,
        pady=(2, 2)
    )

    entrada_email = tk.Entry(
        formulario,
        textvariable=email_var,
        font=("Segoe UI", 9),
        relief="solid",
        bd=1
    )

    entrada_email.grid(
        row=3,
        column=0,
        columnspan=2,
        sticky="ew",
        padx=10,
        pady=(0, 8)
    )


    # =====================================================
    # CURSO
    # =====================================================

    tk.Label(
        formulario,
        text="Curso:",
        **estilo_label
    ).grid(
        row=2,
        column=2,
        columnspan=2,
        sticky="w",
        padx=10,
        pady=(2, 2)
    )

    combo_curso = ttk.Combobox(
        formulario,
        textvariable=curso_var,
        values=[
            "Programación",
            "Redes",
            "Base de Datos",
            "Sistemas"
        ],
        state="readonly",
        font=("Segoe UI", 9)
    )

    combo_curso.grid(
        row=3,
        column=2,
        columnspan=2,
        sticky="ew",
        padx=10,
        pady=(0, 8)
    )


    # Hacer que las columnas se expandan
    for columna in range(4):
        formulario.grid_columnconfigure(
            columna,
            weight=1
        )


    # =====================================================
    # FRAME BOTONES
    # =====================================================

    botones = tk.Frame(
        formulario,
        bg="#eef6ff"
    )

    botones.grid(
        row=4,
        column=0,
        columnspan=4,
        sticky="ew",
        padx=10,
        pady=(0, 10)
    )


    # =====================================================
    # FUNCIÓN LIMPIAR
    # =====================================================

    def limpiar():

        id_seleccionado.set("")

        nombre_var.set("")
        apellido_var.set("")
        dni_var.set("")
        tipo_var.set("")
        email_var.set("")
        curso_var.set("")

        tabla.selection_remove(
            tabla.selection()
        )


    # =====================================================
    # FUNCIÓN LISTAR PERSONAS
    # =====================================================

    def listar_personas():

        try:

            respuesta = requests.get(
                API_URL,
                timeout=5
            )

            if respuesta.status_code == 200:

                personas = respuesta.json()

                # Limpiar tabla
                for item in tabla.get_children():
                    tabla.delete(item)

                # Agregar datos
                for persona in personas:

                    tabla.insert(
                        "",
                        "end",
                        values=(
                            persona["id_persona"],
                            persona["nombre"],
                            persona["apellido"],
                            persona["dni"],
                            persona["tipo"],
                            persona["email"],
                            persona["curso"]
                        )
                    )

                total_personas.config(
                    text=f"Total de personas: {len(personas)}"
                )

            else:

                messagebox.showerror(
                    "Error",
                    "No se pudieron obtener las personas."
                )

        except requests.exceptions.RequestException as error:

            messagebox.showerror(
                "Error de conexión",
                f"No se pudo conectar con el servidor.\n\n{error}"
            )


    # =====================================================
    # FUNCIÓN AGREGAR
    # =====================================================

    def agregar_persona():

        if not nombre_var.get():
            messagebox.showwarning(
                "Campos incompletos",
                "Ingrese el nombre."
            )
            return

        if not apellido_var.get():
            messagebox.showwarning(
                "Campos incompletos",
                "Ingrese el apellido."
            )
            return

        if not dni_var.get():
            messagebox.showwarning(
                "Campos incompletos",
                "Ingrese el DNI."
            )
            return

        if not tipo_var.get():
            messagebox.showwarning(
                "Campos incompletos",
                "Seleccione el tipo."
            )
            return

        if not email_var.get():
            messagebox.showwarning(
                "Campos incompletos",
                "Ingrese el email."
            )
            return

        if not curso_var.get():
            messagebox.showwarning(
                "Campos incompletos",
                "Seleccione el curso."
            )
            return


        datos = {
            "nombre": nombre_var.get(),
            "apellido": apellido_var.get(),
            "dni": dni_var.get(),
            "tipo": tipo_var.get(),
            "email": email_var.get(),
            "curso": curso_var.get()
        }


        try:

            respuesta = requests.post(
                API_URL,
                json=datos,
                timeout=5
            )

            if respuesta.status_code == 201:

                messagebox.showinfo(
                    "Éxito",
                    "Persona agregada correctamente."
                )

                limpiar()
                listar_personas()

            else:

                datos_error = respuesta.json()

                messagebox.showerror(
                    "Error",
                    datos_error.get(
                        "error",
                        "No se pudo agregar la persona."
                    )
                )

        except requests.exceptions.RequestException as error:

            messagebox.showerror(
                "Error de conexión",
                f"No se pudo conectar con el servidor.\n\n{error}"
            )


    # =====================================================
    # FUNCIÓN SELECCIONAR PERSONA
    # =====================================================

    def seleccionar_persona(event):

        seleccion = tabla.selection()

        if not seleccion:
            return

        item = tabla.item(
            seleccion[0]
        )

        valores = item["values"]

        if not valores:
            return

        # ID
        id_seleccionado.set(
            str(valores[0])
        )

        # Campos
        nombre_var.set(
            valores[1]
        )

        apellido_var.set(
            valores[2]
        )

        dni_var.set(
            valores[3]
        )

        tipo_var.set(
            valores[4]
        )

        email_var.set(
            valores[5]
        )

        curso_var.set(
            valores[6]
        )


    # =====================================================
    # FUNCIÓN MODIFICAR
    # =====================================================

    def modificar_persona():

        if not id_seleccionado.get():

            messagebox.showwarning(
                "Seleccionar persona",
                "Seleccione una persona de la tabla para modificar."
            )

            return


        datos = {
            "nombre": nombre_var.get(),
            "apellido": apellido_var.get(),
            "dni": dni_var.get(),
            "tipo": tipo_var.get(),
            "email": email_var.get(),
            "curso": curso_var.get()
        }


        try:

            respuesta = requests.put(
                f"{API_URL}/{id_seleccionado.get()}",
                json=datos,
                timeout=5
            )

            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Éxito",
                    "Persona actualizada correctamente."
                )

                limpiar()
                listar_personas()

            else:

                datos_error = respuesta.json()

                messagebox.showerror(
                    "Error",
                    datos_error.get(
                        "error",
                        "No se pudo actualizar la persona."
                    )
                )

        except requests.exceptions.RequestException as error:

            messagebox.showerror(
                "Error de conexión",
                f"No se pudo conectar con el servidor.\n\n{error}"
            )


    # =====================================================
    # FUNCIÓN ELIMINAR
    # =====================================================

    def eliminar_persona():

        if not id_seleccionado.get():

            messagebox.showwarning(
                "Seleccionar persona",
                "Seleccione una persona de la tabla para eliminar."
            )

            return


        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de que desea eliminar esta persona?"
        )

        if not confirmar:
            return


        try:

            respuesta = requests.delete(
                f"{API_URL}/{id_seleccionado.get()}",
                timeout=5
            )

            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Éxito",
                    "Persona eliminada correctamente."
                )

                limpiar()
                listar_personas()

            else:

                datos_error = respuesta.json()

                messagebox.showerror(
                    "Error",
                    datos_error.get(
                        "error",
                        "No se pudo eliminar la persona."
                    )
                )

        except requests.exceptions.RequestException as error:

            messagebox.showerror(
                "Error de conexión",
                f"No se pudo conectar con el servidor.\n\n{error}"
            )


    # =====================================================
    # BOTÓN AGREGAR
    # =====================================================

    boton_agregar = tk.Button(
        botones,
        text="＋  Agregar",
        command=agregar_persona,
        bg="#0969d8",
        fg="white",
        activebackground="#075bb8",
        activeforeground="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat",
        cursor="hand2",
        width=18
    )

    boton_agregar.pack(
        side="left"
    )


    # =====================================================
    # BOTÓN MODIFICAR
    # =====================================================

    boton_modificar = tk.Button(
        botones,
        text="✎  Modificar",
        command=modificar_persona,
        bg="#0969d8",
        fg="white",
        activebackground="#075bb8",
        activeforeground="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat",
        cursor="hand2",
        width=14
    )

    boton_modificar.pack(
        side="right",
        padx=(5, 0)
    )


    # =====================================================
    # BOTÓN ELIMINAR
    # =====================================================

    boton_eliminar = tk.Button(
        botones,
        text="▣  Eliminar",
        command=eliminar_persona,
        bg="#0969d8",
        fg="white",
        activebackground="#075bb8",
        activeforeground="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat",
        cursor="hand2",
        width=14
    )

    boton_eliminar.pack(
        side="right",
        padx=5
    )


    # =====================================================
    # BOTÓN LIMPIAR
    # =====================================================

    boton_limpiar = tk.Button(
        botones,
        text="⟳  Limpiar",
        command=limpiar,
        bg="#0969d8",
        fg="white",
        activebackground="#075bb8",
        activeforeground="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat",
        cursor="hand2",
        width=14
    )

    boton_limpiar.pack(
        side="right",
        padx=5
    )


    # =====================================================
    # LISTADO
    # =====================================================

    listado = tk.LabelFrame(
        frame,
        text="Listado de Personas",
        font=("Segoe UI", 9, "bold"),
        fg="#0057b8",
        bg="#eef6ff",
        bd=1,
        relief="solid"
    )

    listado.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=5
    )


    # =====================================================
    # FRAME TABLA
    # =====================================================

    frame_tabla = tk.Frame(
        listado,
        bg="#eef6ff"
    )

    frame_tabla.pack(
        fill="both",
        expand=True,
        padx=8,
        pady=8
    )


    # =====================================================
    # COLUMNAS
    # =====================================================

    columnas = (
        "id",
        "nombre",
        "apellido",
        "dni",
        "tipo",
        "email",
        "curso"
    )


    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        selectmode="browse"
    )


    # =====================================================
    # ENCABEZADOS
    # =====================================================

    tabla.heading(
        "id",
        text="ID"
    )

    tabla.heading(
        "nombre",
        text="Nombre"
    )

    tabla.heading(
        "apellido",
        text="Apellido"
    )

    tabla.heading(
        "dni",
        text="DNI"
    )

    tabla.heading(
        "tipo",
        text="Tipo"
    )

    tabla.heading(
        "email",
        text="Email"
    )

    tabla.heading(
        "curso",
        text="Curso"
    )


    # =====================================================
    # ANCHOS
    # =====================================================

    tabla.column(
        "id",
        width=45,
        anchor="center"
    )

    tabla.column(
        "nombre",
        width=100,
        anchor="w"
    )

    tabla.column(
        "apellido",
        width=110,
        anchor="w"
    )

    tabla.column(
        "dni",
        width=90,
        anchor="center"
    )

    tabla.column(
        "tipo",
        width=100,
        anchor="w"
    )

    tabla.column(
        "email",
        width=180,
        anchor="w"
    )

    tabla.column(
        "curso",
        width=130,
        anchor="w"
    )


    # =====================================================
    # SCROLLBAR
    # =====================================================

    scrollbar = ttk.Scrollbar(
        frame_tabla,
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


    # =====================================================
    # ESTILO TABLA
    # =====================================================

    estilo = ttk.Style()

    try:
        estilo.theme_use("clam")
    except:
        pass


    estilo.configure(
        "Treeview",
        background="white",
        foreground="#123456",
        rowheight=28,
        fieldbackground="white",
        font=("Segoe UI", 8)
    )


    estilo.configure(
        "Treeview.Heading",
        background="#e5f2ff",
        foreground="#003b73",
        font=("Segoe UI", 8, "bold")
    )


    estilo.map(
        "Treeview",
        background=[
            ("selected", "#1674d1")
        ],
        foreground=[
            ("selected", "white")
        ]
    )


    # =====================================================
    # SELECCIONAR FILA
    # =====================================================

    tabla.bind(
        "<<TreeviewSelect>>",
        seleccionar_persona
    )


    # =====================================================
    # TOTAL DE PERSONAS
    # =====================================================

    total_personas = tk.Label(
        listado,
        text="Total de personas: 0",
        font=("Segoe UI", 8),
        fg="#0057b8",
        bg="#eef6ff"
    )

    total_personas.pack(
        anchor="w",
        padx=10,
        pady=(0, 8)
    )


    # =====================================================
    # CARGAR PERSONAS AL ABRIR LA INTERFAZ
    # =====================================================

    listar_personas()


    # =====================================================
    # RETORNAR FRAME
    # =====================================================

    return frame