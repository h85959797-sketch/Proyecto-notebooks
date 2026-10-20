import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import requests


# ============================================================
# CONFIGURACIÓN
# ============================================================

API_PRESTAMOS = "http://localhost:3000/api/prestamosydevoluciones"
API_PERSONAS = "http://localhost:3000/api/personas"
API_NOTEBOOKS = "http://localhost:3000/api/notebooks"


# ============================================================
# COLORES - MISMO ESTILO DEL SISTEMA
# ============================================================

AZUL_OSCURO = "#064A9B"
AZUL = "#0875E1"
AZUL_CLARO = "#2F8CF4"
AZUL_MUY_CLARO = "#DCEEFF"

BLANCO = "#FFFFFF"
FONDO = "#EEF7FF"

TEXTO = "#123B72"
BORDE = "#9CCBFA"

VERDE = "#BDEFCB"
VERDE_TEXTO = "#147A38"

AMARILLO = "#FFE5A8"
AMARILLO_TEXTO = "#9A6500"


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def prestamosydevoluciones(parent):

    # ========================================================
    # FRAME PRINCIPAL
    # ========================================================

    frame = tk.Frame(
        parent,
        bg=FONDO
    )

    # ========================================================
    # ESTILOS
    # ========================================================

    style = ttk.Style()

    try:
        style.theme_use("clam")
    except:
        pass

    style.configure(
        "Treeview",
        background=BLANCO,
        foreground=TEXTO,
        rowheight=35,
        fieldbackground=BLANCO,
        font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        background=AZUL_MUY_CLARO,
        foreground=TEXTO,
        font=("Segoe UI", 10, "bold"),
        padding=7
    )

    style.map(
        "Treeview",
        background=[
            ("selected", "#B9DCFF")
        ],
        foreground=[
            ("selected", TEXTO)
        ]
    )


    # ========================================================
    # VARIABLES
    # ========================================================

    prestamos = []
    personas = []
    notebooks = []


    # ========================================================
    # CONTENIDO
    # ========================================================

    contenido = tk.Frame(
        frame,
        bg=FONDO
    )

    contenido.pack(
        side="left",
        fill="both",
        expand=True,
        padx=12,
        pady=12
    )


    # ========================================================
    # ENCABEZADO
    # ========================================================

    encabezado = tk.Frame(
        contenido,
        bg=AZUL
    )

    encabezado.pack(
        fill="x",
        pady=(0, 10)
    )

    tk.Label(
        encabezado,
        text="↔",
        font=("Segoe UI", 35, "bold"),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        side="left",
        padx=(18, 12),
        pady=8
    )

    titulo_frame = tk.Frame(
        encabezado,
        bg=AZUL
    )

    titulo_frame.pack(
        side="left",
        pady=10
    )

    tk.Label(
        titulo_frame,
        text="Préstamos y Devoluciones",
        font=("Segoe UI", 20, "bold"),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        anchor="w"
    )

    tk.Label(
        titulo_frame,
        text="Control de entrega y devolución de notebooks.",
        font=("Segoe UI", 9),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        anchor="w"
    )


    # ========================================================
    # PANEL DE FILTROS
    # ========================================================

    panel_filtros = tk.Frame(
        contenido,
        bg=BLANCO,
        highlightbackground=BORDE,
        highlightthickness=1
    )

    panel_filtros.pack(
        fill="x",
        pady=(0, 10)
    )


    tk.Label(
        panel_filtros,
        text="Filtros de búsqueda",
        font=("Segoe UI", 11, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).pack(
        anchor="w",
        padx=12,
        pady=(8, 5)
    )


    filtros = tk.Frame(
        panel_filtros,
        bg=BLANCO
    )

    filtros.pack(
        fill="x",
        padx=12,
        pady=(0, 10)
    )


    filtros.columnconfigure(0, weight=1)
    filtros.columnconfigure(1, weight=1)
    filtros.columnconfigure(2, weight=1)
    filtros.columnconfigure(3, weight=1)


    # ========================================================
    # FILTRO PERSONA
    # ========================================================

    tk.Label(
        filtros,
        text="Persona:",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=5
    )

    combo_persona = ttk.Combobox(
        filtros,
        state="readonly",
        font=("Segoe UI", 9)
    )

    combo_persona.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=5,
        pady=3
    )


    # ========================================================
    # FILTRO NOTEBOOK
    # ========================================================

    tk.Label(
        filtros,
        text="Notebook:",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=0,
        column=1,
        sticky="w",
        padx=5
    )

    combo_notebook = ttk.Combobox(
        filtros,
        state="readonly",
        font=("Segoe UI", 9)
    )

    combo_notebook.grid(
        row=1,
        column=1,
        sticky="ew",
        padx=5,
        pady=3
    )


    # ========================================================
    # FILTRO ESTADO
    # ========================================================

    tk.Label(
        filtros,
        text="Estado:",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=0,
        column=2,
        sticky="w",
        padx=5
    )

    combo_estado = ttk.Combobox(
        filtros,
        values=[
            "Todos",
            "En préstamo",
            "Devuelto"
        ],
        state="readonly",
        font=("Segoe UI", 9)
    )

    combo_estado.set("Todos")

    combo_estado.grid(
        row=1,
        column=2,
        sticky="ew",
        padx=5,
        pady=3
    )


    # ========================================================
    # BOTÓN BUSCAR
    # ========================================================

    boton_buscar = tk.Button(
        filtros,
        text="🔍  Buscar",
        font=("Segoe UI", 9, "bold"),
        fg=BLANCO,
        bg=AZUL,
        activebackground=AZUL_CLARO,
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    boton_buscar.grid(
        row=1,
        column=3,
        sticky="ew",
        padx=5,
        pady=3
    )


    # ========================================================
    # FECHAS
    # ========================================================

    tk.Label(
        filtros,
        text="Fecha desde:",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=2,
        column=0,
        sticky="w",
        padx=5,
        pady=(8, 0)
    )

    entry_desde = tk.Entry(
        filtros,
        font=("Segoe UI", 9),
        relief="solid",
        bd=1
    )

    entry_desde.grid(
        row=3,
        column=0,
        sticky="ew",
        padx=5
    )


    tk.Label(
        filtros,
        text="Fecha hasta:",
        font=("Segoe UI", 9, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).grid(
        row=2,
        column=1,
        sticky="w",
        padx=5,
        pady=(8, 0)
    )

    entry_hasta = tk.Entry(
        filtros,
        font=("Segoe UI", 9),
        relief="solid",
        bd=1
    )

    entry_hasta.grid(
        row=3,
        column=1,
        sticky="ew",
        padx=5
    )


    # ========================================================
    # LISTADO
    # ========================================================

    panel_lista = tk.Frame(
        contenido,
        bg=BLANCO,
        highlightbackground=BORDE,
        highlightthickness=1
    )

    panel_lista.pack(
        fill="both",
        expand=True
    )


    tk.Label(
        panel_lista,
        text="Listado de Préstamos y Devoluciones",
        font=("Segoe UI", 11, "bold"),
        fg=TEXTO,
        bg=BLANCO
    ).pack(
        anchor="w",
        padx=12,
        pady=(8, 5)
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
        padx=12
    )


    columnas = (
        "id",
        "fecha_prestamo",
        "fecha_devolucion",
        "persona",
        "notebook",
        "estado"
    )

    tree = ttk.Treeview(
        tabla_frame,
        columns=columnas,
        show="headings",
        selectmode="browse"
    )


    tree.heading(
        "id",
        text="ID"
    )

    tree.heading(
        "fecha_prestamo",
        text="Fecha préstamo"
    )

    tree.heading(
        "fecha_devolucion",
        text="Fecha devolución"
    )

    tree.heading(
        "persona",
        text="Persona"
    )

    tree.heading(
        "notebook",
        text="Notebook"
    )

    tree.heading(
        "estado",
        text="Estado"
    )


    tree.column(
        "id",
        width=45,
        anchor="center"
    )

    tree.column(
        "fecha_prestamo",
        width=130
    )

    tree.column(
        "fecha_devolucion",
        width=130
    )

    tree.column(
        "persona",
        width=140
    )

    tree.column(
        "notebook",
        width=130
    )

    tree.column(
        "estado",
        width=110
    )


    scrollbar = ttk.Scrollbar(
        tabla_frame,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar.set
    )


    tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )


    # ========================================================
    # FUNCIONES
    # ========================================================

    def obtener_nombre_persona(id_persona):

        for persona in personas:

            if str(persona.get("id_persona")) == str(id_persona):

                nombre = persona.get("nombre", "")
                apellido = persona.get("apellido", "")

                return f"{nombre} {apellido}".strip()

        return f"ID {id_persona}"


    def obtener_nombre_notebook(id_notebook):

        for notebook in notebooks:

            if str(notebook.get("id_notebook")) == str(id_notebook):

                marca = notebook.get("marca", "")
                serie = notebook.get("num_serie", "")

                return f"{marca} - {serie}"

        return f"ID {id_notebook}"


    def obtener_id_persona(texto):

        for persona in personas:

            nombre = persona.get("nombre", "")
            apellido = persona.get("apellido", "")

            nombre_completo = f"{nombre} {apellido}".strip()

            if nombre_completo == texto:
                return persona.get("id_persona")

        return None


    def obtener_id_notebook(texto):

        for notebook in notebooks:

            marca = notebook.get("marca", "")
            serie = notebook.get("num_serie", "")

            nombre = f"{marca} - {serie}"

            if nombre == texto:
                return notebook.get("id_notebook")

        return None


    def cargar_personas():

        nonlocal personas

        try:

            respuesta = requests.get(
                API_PERSONAS,
                timeout=5
            )

            if respuesta.status_code == 200:

                personas = respuesta.json()

                lista = ["Todos"]

                for persona in personas:

                    nombre = persona.get(
                        "nombre",
                        ""
                    )

                    apellido = persona.get(
                        "apellido",
                        ""
                    )

                    lista.append(
                        f"{nombre} {apellido}".strip()
                    )

                combo_persona["values"] = lista
                combo_persona.set("Todos")

        except Exception as error:

            print(
                "No se pudieron cargar las personas:",
                error
            )


    def cargar_notebooks():

        nonlocal notebooks

        try:

            respuesta = requests.get(
                API_NOTEBOOKS,
                timeout=5
            )

            if respuesta.status_code == 200:

                notebooks = respuesta.json()

                lista = ["Todos"]

                for notebook in notebooks:

                    marca = notebook.get(
                        "marca",
                        ""
                    )

                    serie = notebook.get(
                        "num_serie",
                        ""
                    )

                    lista.append(
                        f"{marca} - {serie}"
                    )

                combo_notebook["values"] = lista
                combo_notebook.set("Todos")

        except Exception as error:

            print(
                "No se pudieron cargar las notebooks:",
                error
            )


    # ========================================================
    # CARGAR TABLA
    # ========================================================

    def cargar_prestamos():

        nonlocal prestamos

        try:

            respuesta = requests.get(
                API_PRESTAMOS,
                timeout=5
            )

            if respuesta.status_code != 200:

                raise Exception(
                    f"Error HTTP {respuesta.status_code}"
                )

            prestamos = respuesta.json()

            mostrar_prestamos(prestamos)

        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el backend.\n\n"
                "Verificá que Node.js esté ejecutándose."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudieron cargar los préstamos.\n\n{error}"
            )


    # ========================================================
    # MOSTRAR PRESTAMOS
    # ========================================================

    def mostrar_prestamos(lista):

        for item in tree.get_children():

            tree.delete(item)


        for prestamo in lista:

            id_prestamo = prestamo.get(
                "id_prestamo"
            )

            dia = prestamo.get(
                "dia",
                ""
            )

            hora_prestamo = prestamo.get(
                "hora_prestamo",
                ""
            )

            hora_devolucion = prestamo.get(
                "hora_devolucion",
                ""
            )


            # -----------------------------------------------
            # FORMATEAR FECHA
            # -----------------------------------------------

            fecha_prestamo = str(
                hora_prestamo or dia
            )

            fecha_devolucion = str(
                hora_devolucion or "-"
            )


            if " " in fecha_prestamo:

                fecha_prestamo = fecha_prestamo[:16]


            if " " in fecha_devolucion:

                fecha_devolucion = fecha_devolucion[:16]


            # -----------------------------------------------
            # ESTADO
            # -----------------------------------------------

            estado = prestamo.get(
                "estado_devolucion"
            )

            if not estado:

                estado = "En préstamo"


            persona = obtener_nombre_persona(
                prestamo.get("id_persona")
            )

            notebook = obtener_nombre_notebook(
                prestamo.get("id_notebook")
            )


            item = tree.insert(
                "",
                tk.END,
                iid=str(id_prestamo),
                values=(
                    id_prestamo,
                    fecha_prestamo,
                    fecha_devolucion,
                    persona,
                    notebook,
                    estado
                )
            )


            # -----------------------------------------------
            # COLORES SEGÚN ESTADO
            # -----------------------------------------------

            if estado.lower() == "devuelto":

                tree.item(
                    item,
                    tags=("devuelto",)
                )

            else:

                tree.item(
                    item,
                    tags=("prestamo",)
                )


        tree.tag_configure(
            "devuelto",
            foreground=VERDE_TEXTO
        )

        tree.tag_configure(
            "prestamo",
            foreground="#1265B0"
        )


        label_total.config(
            text=f"Total de préstamos: {len(lista)}"
        )


    # ========================================================
    # FILTRAR
    # ========================================================

    def buscar():

        persona_filtro = combo_persona.get()
        notebook_filtro = combo_notebook.get()
        estado_filtro = combo_estado.get()

        desde = entry_desde.get().strip()
        hasta = entry_hasta.get().strip()


        resultado = []


        for prestamo in prestamos:

            # -----------------------------------------------
            # PERSONA
            # -----------------------------------------------

            persona = obtener_nombre_persona(
                prestamo.get("id_persona")
            )

            if (
                persona_filtro != "Todos"
                and persona != persona_filtro
            ):
                continue


            # -----------------------------------------------
            # NOTEBOOK
            # -----------------------------------------------

            notebook = obtener_nombre_notebook(
                prestamo.get("id_notebook")
            )

            if (
                notebook_filtro != "Todos"
                and notebook != notebook_filtro
            ):
                continue


            # -----------------------------------------------
            # ESTADO
            # -----------------------------------------------

            estado = prestamo.get(
                "estado_devolucion"
            )

            if not estado:

                estado = "En préstamo"


            if (
                estado_filtro != "Todos"
                and estado != estado_filtro
            ):
                continue


            # -----------------------------------------------
            # FECHA
            # -----------------------------------------------

            dia = str(
                prestamo.get("dia", "")
            )[:10]


            if desde and dia < desde:

                continue


            if hasta and dia > hasta:

                continue


            resultado.append(
                prestamo
            )


        mostrar_prestamos(
            resultado
        )


    boton_buscar.config(
        command=buscar
    )


    # ========================================================
    # REGISTRAR PRÉSTAMO
    # ========================================================

    def registrar_prestamo():

        ventana = tk.Toplevel(
            frame
        )

        ventana.title(
            "Registrar préstamo"
        )

        ventana.geometry(
            "500x430"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg=FONDO
        )


        # ----------------------------------------------------
        # TÍTULO
        # ----------------------------------------------------

        tk.Label(
            ventana,
            text="Registrar Préstamo",
            font=("Segoe UI", 17, "bold"),
            fg=BLANCO,
            bg=AZUL
        ).pack(
            fill="x",
            ipady=12
        )


        formulario = tk.Frame(
            ventana,
            bg=BLANCO
        )

        formulario.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )


        # ----------------------------------------------------
        # PERSONA
        # ----------------------------------------------------

        tk.Label(
            formulario,
            text="Persona:",
            font=("Segoe UI", 10, "bold"),
            fg=TEXTO,
            bg=BLANCO
        ).pack(
            anchor="w"
        )

        persona_combo = ttk.Combobox(
            formulario,
            values=combo_persona["values"][1:],
            state="readonly"
        )

        persona_combo.pack(
            fill="x",
            pady=(4, 12)
        )


        # ----------------------------------------------------
        # NOTEBOOK
        # ----------------------------------------------------

        tk.Label(
            formulario,
            text="Notebook:",
            font=("Segoe UI", 10, "bold"),
            fg=TEXTO,
            bg=BLANCO
        ).pack(
            anchor="w"
        )

        notebook_combo = ttk.Combobox(
            formulario,
            values=combo_notebook["values"][1:],
            state="readonly"
        )

        notebook_combo.pack(
            fill="x",
            pady=(4, 12)
        )


        # ----------------------------------------------------
        # MATERIA
        # ----------------------------------------------------

        tk.Label(
            formulario,
            text="Materia:",
            font=("Segoe UI", 10, "bold"),
            fg=TEXTO,
            bg=BLANCO
        ).pack(
            anchor="w"
        )

        materia_entry = tk.Entry(
            formulario
        )

        materia_entry.pack(
            fill="x",
            pady=(4, 12)
        )


        # ----------------------------------------------------
        # OBSERVACIÓN
        # ----------------------------------------------------

        tk.Label(
            formulario,
            text="Observación:",
            font=("Segoe UI", 10, "bold"),
            fg=TEXTO,
            bg=BLANCO
        ).pack(
            anchor="w"
        )

        observacion_entry = tk.Entry(
            formulario
        )

        observacion_entry.pack(
            fill="x",
            pady=(4, 15)
        )


        # ----------------------------------------------------
        # GUARDAR
        # ----------------------------------------------------

        def guardar():

            persona = persona_combo.get()
            notebook = notebook_combo.get()
            materia = materia_entry.get().strip()
            observacion = observacion_entry.get().strip()


            id_persona = obtener_id_persona(
                persona
            )

            id_notebook = obtener_id_notebook(
                notebook
            )


            if not id_persona or not id_notebook:

                messagebox.showwarning(
                    "Datos incompletos",
                    "Seleccioná una persona y una notebook.",
                    parent=ventana
                )

                return


            ahora = datetime.now()

            datos = {

                "dia": ahora.strftime(
                    "%Y-%m-%d"
                ),

                "hora_prestamo": ahora.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "hora_devolucion": None,

                "estado_devolucion": "En préstamo",

                "materia": materia,

                "observacion": observacion,

                "id_persona": id_persona,

                "id_notebook": id_notebook
            }


            try:

                respuesta = requests.post(
                    API_PRESTAMOS,
                    json=datos,
                    timeout=5
                )


                if respuesta.status_code == 201:

                    messagebox.showinfo(
                        "Éxito",
                        "Préstamo registrado correctamente.",
                        parent=ventana
                    )

                    ventana.destroy()

                    cargar_prestamos()

                else:

                    messagebox.showerror(
                        "Error",
                        respuesta.text,
                        parent=ventana
                    )

            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )


        tk.Button(
            formulario,
            text="＋  Registrar préstamo",
            command=guardar,
            font=("Segoe UI", 10, "bold"),
            fg=BLANCO,
            bg=AZUL,
            activebackground=AZUL_CLARO,
            relief="flat",
            bd=0,
            cursor="hand2"
        ).pack(
            fill="x",
            ipady=9
        )


    # ========================================================
    # REGISTRAR DEVOLUCIÓN
    # ========================================================

    def registrar_devolucion():

        seleccion = tree.selection()


        if not seleccion:

            messagebox.showwarning(
                "Seleccionar préstamo",
                "Seleccioná un préstamo de la tabla."
            )

            return


        id_prestamo = seleccion[0]


        confirmar = messagebox.askyesno(
            "Registrar devolución",
            "¿Querés registrar la devolución de esta notebook?"
        )


        if not confirmar:

            return


        try:

            # -----------------------------------------------
            # OBTENER REGISTRO
            # -----------------------------------------------

            respuesta = requests.get(
                f"{API_PRESTAMOS}/{id_prestamo}",
                timeout=5
            )


            if respuesta.status_code != 200:

                messagebox.showerror(
                    "Error",
                    "No se pudo obtener el préstamo."
                )

                return


            prestamo = respuesta.json()


            # -----------------------------------------------
            # FECHA ACTUAL
            # -----------------------------------------------

            ahora = datetime.now()


            datos = {

                "dia": prestamo.get(
                    "dia"
                ),

                "hora_prestamo": prestamo.get(
                    "hora_prestamo"
                ),

                "hora_devolucion": ahora.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "estado_devolucion": "Devuelto",

                "materia": prestamo.get(
                    "materia"
                ),

                "observacion": prestamo.get(
                    "observacion"
                ),

                "id_persona": prestamo.get(
                    "id_persona"
                ),

                "id_notebook": prestamo.get(
                    "id_notebook"
                )
            }


            # -----------------------------------------------
            # ACTUALIZAR
            # -----------------------------------------------

            respuesta = requests.put(
                f"{API_PRESTAMOS}/{id_prestamo}",
                json=datos,
                timeout=5
            )


            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Éxito",
                    "Devolución registrada correctamente."
                )

                cargar_prestamos()

            else:

                messagebox.showerror(
                    "Error",
                    respuesta.text
                )


        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # VER DETALLES
    # ========================================================

    def ver_detalles():

        seleccion = tree.selection()


        if not seleccion:

            messagebox.showwarning(
                "Seleccionar préstamo",
                "Seleccioná un préstamo de la tabla."
            )

            return


        id_prestamo = seleccion[0]


        try:

            respuesta = requests.get(
                f"{API_PRESTAMOS}/{id_prestamo}",
                timeout=5
            )


            if respuesta.status_code != 200:

                raise Exception(
                    "No se pudo obtener el préstamo."
                )


            prestamo = respuesta.json()


            ventana = tk.Toplevel(
                frame
            )

            ventana.title(
                "Detalles del préstamo"
            )

            ventana.geometry(
                "500x430"
            )

            ventana.resizable(
                False,
                False
            )

            ventana.configure(
                bg=FONDO
            )


            tk.Label(
                ventana,
                text="Detalles del Préstamo",
                font=("Segoe UI", 17, "bold"),
                fg=BLANCO,
                bg=AZUL
            ).pack(
                fill="x",
                ipady=12
            )


            datos_frame = tk.Frame(
                ventana,
                bg=BLANCO
            )

            datos_frame.pack(
                fill="both",
                expand=True,
                padx=20,
                pady=20
            )


            detalles = [

                (
                    "ID:",
                    prestamo.get(
                        "id_prestamo"
                    )
                ),

                (
                    "Persona:",
                    obtener_nombre_persona(
                        prestamo.get(
                            "id_persona"
                        )
                    )
                ),

                (
                    "Notebook:",
                    obtener_nombre_notebook(
                        prestamo.get(
                            "id_notebook"
                        )
                    )
                ),

                (
                    "Materia:",
                    prestamo.get(
                        "materia"
                    )
                ),

                (
                    "Observación:",
                    prestamo.get(
                        "observacion"
                    )
                ),

                (
                    "Préstamo:",
                    prestamo.get(
                        "hora_prestamo"
                    )
                ),

                (
                    "Devolución:",
                    prestamo.get(
                        "hora_devolucion"
                    ) or "-"
                ),

                (
                    "Estado:",
                    prestamo.get(
                        "estado_devolucion"
                    ) or "En préstamo"
                )
            ]


            for nombre, valor in detalles:

                fila = tk.Frame(
                    datos_frame,
                    bg=BLANCO
                )

                fila.pack(
                    fill="x",
                    pady=5
                )


                tk.Label(
                    fila,
                    text=nombre,
                    font=("Segoe UI", 10, "bold"),
                    fg=TEXTO,
                    bg=BLANCO,
                    width=15,
                    anchor="w"
                ).pack(
                    side="left"
                )


                tk.Label(
                    fila,
                    text=str(valor),
                    font=("Segoe UI", 10),
                    fg=TEXTO,
                    bg=BLANCO,
                    anchor="w"
                ).pack(
                    side="left"
                )


        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


    # ========================================================
    # BOTONES INFERIORES
    # ========================================================

    botones = tk.Frame(
        panel_lista,
        bg=BLANCO
    )

    botones.pack(
        fill="x",
        padx=12,
        pady=10
    )


    tk.Button(
        botones,
        text="＋  Registrar Préstamo",
        command=registrar_prestamo,
        font=("Segoe UI", 9, "bold"),
        fg=BLANCO,
        bg=AZUL,
        activebackground=AZUL_CLARO,
        relief="flat",
        bd=0,
        cursor="hand2"
    ).pack(
        side="left",
        expand=True,
        fill="x",
        padx=4,
        ipady=8
    )


    tk.Button(
        botones,
        text="↶  Registrar Devolución",
        command=registrar_devolucion,
        font=("Segoe UI", 9, "bold"),
        fg=BLANCO,
        bg=AZUL,
        activebackground=AZUL_CLARO,
        relief="flat",
        bd=0,
        cursor="hand2"
    ).pack(
        side="left",
        expand=True,
        fill="x",
        padx=4,
        ipady=8
    )


    tk.Button(
        botones,
        text="▣  Ver Detalles",
        command=ver_detalles,
        font=("Segoe UI", 9, "bold"),
        fg=BLANCO,
        bg=AZUL,
        activebackground=AZUL_CLARO,
        relief="flat",
        bd=0,
        cursor="hand2"
    ).pack(
        side="left",
        expand=True,
        fill="x",
        padx=4,
        ipady=8
    )


    # ========================================================
    # TOTAL
    # ========================================================

    label_total = tk.Label(
        panel_lista,
        text="Total de préstamos: 0",
        font=("Segoe UI", 9),
        fg=TEXTO,
        bg=AZUL_MUY_CLARO,
        anchor="w"
    )

    label_total.pack(
        fill="x",
        padx=12,
        pady=(0, 10),
        ipady=5
    )


    # ========================================================
    # CARGAR DATOS
    # ========================================================

    cargar_personas()
    cargar_notebooks()
    cargar_prestamos()


    # ========================================================
    # RETORNAR FRAME
    # ========================================================

    return frame