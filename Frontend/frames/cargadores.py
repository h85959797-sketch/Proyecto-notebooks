import tkinter as tk
from tkinter import ttk, messagebox
import requests


# =========================================================
# CONFIGURACIÓN
# =========================================================

API_URL = "http://localhost:3000/cargadores"


# =========================================================
# FUNCIÓN PRINCIPAL
# =========================================================

def crear_cargadores(parent):

    # =====================================================
    # FRAME PRINCIPAL
    # =====================================================

    frame = tk.Frame(
        parent,
        bg="#eef1f5"
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
        bg="#0878df",
        height=55
    )

    encabezado.pack(
        fill="x"
    )

    encabezado.pack_propagate(False)


    titulo = tk.Label(
        encabezado,
        text="🔌  Gestión de Cargadores",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#0878df"
    )

    titulo.pack(
        side="left",
        padx=20,
        pady=10
    )


    # =====================================================
    # CONTENEDOR GENERAL
    # =====================================================

    contenido = tk.Frame(
        frame,
        bg="#eef1f5"
    )

    contenido.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=10
    )


    # =====================================================
    # FILTROS
    # =====================================================

    filtros = tk.LabelFrame(
        contenido,
        text="Filtros de búsqueda",
        font=("Arial", 10, "bold"),
        fg="#075ca8",
        bg="#eef1f5",
        bd=1,
        relief="solid"
    )

    filtros.pack(
        fill="x",
        pady=(0, 10)
    )


    # -----------------------------------------------------
    # ESTADO
    # -----------------------------------------------------

    tk.Label(
        filtros,
        text="Estado:",
        font=("Arial", 9, "bold"),
        bg="#eef1f5",
        fg="#174d80"
    ).grid(
        row=0,
        column=0,
        padx=(10, 5),
        pady=(8, 2),
        sticky="w"
    )


    estado_var = tk.StringVar(
        value="Todos"
    )

    estado_combo = ttk.Combobox(
        filtros,
        textvariable=estado_var,
        state="readonly",
        width=17,
        values=[
            "Todos",
            "Disponible",
            "En uso",
            "Dañado",
            "Reparación"
        ]
    )

    estado_combo.grid(
        row=1,
        column=0,
        padx=(10, 15),
        pady=(0, 10)
    )


    # -----------------------------------------------------
    # NOTEBOOK
    # -----------------------------------------------------

    tk.Label(
        filtros,
        text="Notebook:",
        font=("Arial", 9, "bold"),
        bg="#eef1f5",
        fg="#174d80"
    ).grid(
        row=0,
        column=1,
        padx=5,
        pady=(8, 2),
        sticky="w"
    )


    notebook_var = tk.StringVar(
        value="Todas"
    )

    notebook_combo = ttk.Combobox(
        filtros,
        textvariable=notebook_var,
        state="readonly",
        width=20
    )

    notebook_combo.grid(
        row=1,
        column=1,
        padx=5,
        pady=(0, 10)
    )


    # -----------------------------------------------------
    # TIPO
    # -----------------------------------------------------

    tk.Label(
        filtros,
        text="Tipo:",
        font=("Arial", 9, "bold"),
        bg="#eef1f5",
        fg="#174d80"
    ).grid(
        row=0,
        column=2,
        padx=5,
        pady=(8, 2),
        sticky="w"
    )


    tipo_var = tk.StringVar(
        value="Todos"
    )

    tipo_combo = ttk.Combobox(
        filtros,
        textvariable=tipo_var,
        state="readonly",
        width=17,
        values=[
            "Todos",
            "Original",
            "Genérico"
        ]
    )

    tipo_combo.grid(
        row=1,
        column=2,
        padx=5,
        pady=(0, 10)
    )


    # -----------------------------------------------------
    # BOTÓN BUSCAR
    # -----------------------------------------------------

    boton_buscar = tk.Button(
        filtros,
        text="🔍  Buscar",
        font=("Arial", 10, "bold"),
        fg="white",
        bg="#0878df",
        activebackground="#0564bc",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=5
    )

    boton_buscar.grid(
        row=1,
        column=3,
        padx=(20, 10),
        pady=(0, 10)
    )


    # =====================================================
    # LISTADO
    # =====================================================

    listado = tk.LabelFrame(
        contenido,
        text="Listado de Cargadores",
        font=("Arial", 10, "bold"),
        fg="#075ca8",
        bg="#eef1f5",
        bd=1,
        relief="solid"
    )

    listado.pack(
        fill="both",
        expand=True
    )


    # =====================================================
    # TABLA
    # =====================================================

    columnas = (
        "id",
        "num",
        "estado",
        "notebook",
        "observaciones"
    )


    tabla = ttk.Treeview(
        listado,
        columns=columnas,
        show="headings",
        height=12
    )


    tabla.heading(
        "id",
        text="ID"
    )

    tabla.heading(
        "num",
        text="Número"
    )

    tabla.heading(
        "estado",
        text="Estado"
    )

    tabla.heading(
        "notebook",
        text="Notebook asignada"
    )

    tabla.heading(
        "observaciones",
        text="Observaciones"
    )


    tabla.column(
        "id",
        width=50,
        anchor="center"
    )

    tabla.column(
        "num",
        width=80,
        anchor="center"
    )

    tabla.column(
        "estado",
        width=120,
        anchor="center"
    )

    tabla.column(
        "notebook",
        width=150,
        anchor="center"
    )

    tabla.column(
        "observaciones",
        width=180,
        anchor="center"
    )


    tabla.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(10, 0),
        pady=10
    )


    # =====================================================
    # SCROLLBAR
    # =====================================================

    scrollbar = ttk.Scrollbar(
        listado,
        orient="vertical",
        command=tabla.yview
    )

    scrollbar.pack(
        side="right",
        fill="y",
        padx=(0, 10),
        pady=10
    )

    tabla.configure(
        yscrollcommand=scrollbar.set
    )


    # =====================================================
    # BOTONES INFERIORES
    # =====================================================

    botones = tk.Frame(
        contenido,
        bg="#eef1f5"
    )

    botones.pack(
        fill="x",
        pady=(8, 0)
    )


    total_label = tk.Label(
        botones,
        text="Total de cargadores: 0",
        font=("Arial", 10, "bold"),
        bg="#eef1f5",
        fg="#175b91"
    )

    total_label.pack(
        side="left"
    )


    boton_eliminar = tk.Button(
        botones,
        text="🗑 Eliminar",
        font=("Arial", 10, "bold"),
        bg="#dc3545",
        fg="white",
        activebackground="#b02a37",
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=7
    )

    boton_eliminar.pack(
        side="right",
        padx=(5, 0)
    )


    boton_editar = tk.Button(
        botones,
        text="✏ Editar",
        font=("Arial", 10, "bold"),
        bg="#f0ad4e",
        fg="white",
        activebackground="#ec971f",
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=7
    )

    boton_editar.pack(
        side="right",
        padx=5
    )


    boton_agregar = tk.Button(
        botones,
        text="＋ Agregar cargador",
        font=("Arial", 10, "bold"),
        bg="#0878df",
        fg="white",
        activebackground="#0564bc",
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=7
    )

    boton_agregar.pack(
        side="right"
    )


    # =====================================================
    # FUNCIONES
    # =====================================================

    cargadores = []


    # -----------------------------------------------------
    # CARGAR NOTEBOOKS
    # -----------------------------------------------------

    def cargar_notebooks():

        try:

            respuesta = requests.get(
                "http://localhost:3000/notebooks",
                timeout=5
            )

            if respuesta.status_code == 200:

                notebooks = respuesta.json()

                valores = ["Todas"]

                for notebook in notebooks:

                    id_notebook = notebook.get(
                        "id_notebook"
                    )

                    valores.append(
                        f"NB-{id_notebook:03d}"
                    )

                notebook_combo["values"] = valores

                notebook_combo.set("Todas")

        except requests.exceptions.RequestException:

            notebook_combo["values"] = [
                "Todas"
            ]

            notebook_combo.set("Todas")


    # -----------------------------------------------------
    # MOSTRAR DATOS EN TABLA
    # -----------------------------------------------------

    def mostrar_tabla(datos):

        # Limpiar tabla

        for item in tabla.get_children():

            tabla.delete(item)


        # Guardar datos

        cargadores.clear()

        cargadores.extend(datos)


        # Mostrar registros

        for cargador in datos:

            id_cargador = cargador.get(
                "id_cargador",
                ""
            )

            numero = cargador.get(
                "num",
                ""
            )

            estado = cargador.get(
                "estado",
                ""
            )

            id_notebook = cargador.get(
                "id_notebook"
            )

            observaciones = cargador.get(
                "observaciones",
                ""
            )


            if id_notebook:

                notebook = f"NB-{int(id_notebook):03d}"

            else:

                notebook = "-"


            tabla.insert(
                "",
                "end",
                values=(
                    id_cargador,
                    numero,
                    estado,
                    notebook,
                    observaciones
                )
            )


        total_label.config(
            text=f"Total de cargadores: {len(datos)}"
        )


    # -----------------------------------------------------
    # OBTENER CARGADORES
    # -----------------------------------------------------

    def cargar_cargadores():

        try:

            respuesta = requests.get(
                API_URL,
                timeout=5
            )


            if respuesta.status_code == 200:

                datos = respuesta.json()

                mostrar_tabla(datos)

            else:

                messagebox.showerror(
                    "Error",
                    "No se pudieron obtener los cargadores."
                )

        except requests.exceptions.RequestException as error:

            messagebox.showerror(
                "Error de conexión",
                f"No se pudo conectar con el servidor.\n\n{error}"
            )


    # -----------------------------------------------------
    # BUSCAR
    # -----------------------------------------------------

    def buscar():

        estado = estado_var.get()
        notebook = notebook_var.get()
        tipo = tipo_var.get()


        try:

            respuesta = requests.get(
                API_URL,
                timeout=5
            )


            if respuesta.status_code != 200:

                messagebox.showerror(
                    "Error",
                    "No se pudieron obtener los cargadores."
                )

                return


            datos = respuesta.json()


            filtrados = []


            for cargador in datos:

                estado_bd = cargador.get(
                    "estado",
                    ""
                )


                id_notebook = cargador.get(
                    "id_notebook"
                )


                if id_notebook:

                    notebook_bd = f"NB-{int(id_notebook):03d}"

                else:

                    notebook_bd = "-"


                # Filtro estado

                if estado != "Todos":

                    if estado_bd != estado:

                        continue


                # Filtro notebook

                if notebook != "Todas":

                    if notebook_bd != notebook:

                        continue


                # ------------------------------------------------
                # TIPO
                #
                # Tu tabla actual NO tiene un campo "tipo".
                # Por eso no podemos filtrarlo realmente todavía.
                # ------------------------------------------------

                filtrados.append(cargador)


            mostrar_tabla(filtrados)


        except requests.exceptions.RequestException as error:

            messagebox.showerror(
                "Error de conexión",
                f"No se pudo conectar con el servidor.\n\n{error}"
            )


    # -----------------------------------------------------
    # OBTENER ID SELECCIONADO
    # -----------------------------------------------------

    def obtener_seleccion():

        seleccion = tabla.selection()


        if not seleccion:

            messagebox.showwarning(
                "Seleccionar cargador",
                "Seleccioná un cargador de la tabla."
            )

            return None


        valores = tabla.item(
            seleccion[0],
            "values"
        )


        return valores


    # -----------------------------------------------------
    # AGREGAR CARGADOR
    # -----------------------------------------------------

    def agregar_cargador():

        ventana = tk.Toplevel(frame)

        ventana.title(
            "Agregar cargador"
        )

        ventana.geometry(
            "420x380"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg="#eef1f5"
        )


        tk.Label(
            ventana,
            text="Agregar cargador",
            font=("Arial", 16, "bold"),
            bg="#eef1f5",
            fg="#075ca8"
        ).pack(
            pady=15
        )


        # Número

        tk.Label(
            ventana,
            text="Número:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        num_entry = tk.Entry(
            ventana,
            width=40
        )

        num_entry.pack(
            padx=30,
            pady=(5, 15)
        )


        # Estado

        tk.Label(
            ventana,
            text="Estado:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        estado_entry = ttk.Combobox(
            ventana,
            state="readonly",
            values=[
                "Disponible",
                "En uso",
                "Dañado",
                "Reparación"
            ],
            width=37
        )

        estado_entry.set(
            "Disponible"
        )

        estado_entry.pack(
            padx=30,
            pady=(5, 15)
        )


        # Notebook

        tk.Label(
            ventana,
            text="Notebook:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        notebook_entry = ttk.Combobox(
            ventana,
            state="readonly",
            width=37
        )

        notebook_entry["values"] = [
            "Sin asignar"
        ]

        notebook_entry.set(
            "Sin asignar"
        )

        notebook_entry.pack(
            padx=30,
            pady=(5, 15)
        )


        # Observaciones

        tk.Label(
            ventana,
            text="Observaciones:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        observaciones_entry = tk.Entry(
            ventana,
            width=40
        )

        observaciones_entry.pack(
            padx=30,
            pady=(5, 20)
        )


        # -------------------------------------------------
        # GUARDAR
        # -------------------------------------------------

        def guardar():

            try:

                numero = int(
                    num_entry.get()
                )

            except ValueError:

                messagebox.showwarning(
                    "Dato incorrecto",
                    "El número debe ser un valor numérico."
                )

                return


            estado = estado_entry.get()
            observaciones = observaciones_entry.get()


            # Obtener notebook

            notebook_texto = notebook_entry.get()


            if notebook_texto == "Sin asignar":

                id_notebook = None

            else:

                try:

                    id_notebook = int(
                        notebook_texto.replace(
                            "NB-",
                            ""
                        )
                    )

                except ValueError:

                    id_notebook = None


            datos = {
                "num": numero,
                "estado": estado,
                "observaciones": observaciones,
                "id_notebook": id_notebook
            }


            try:

                respuesta = requests.post(
                    API_URL,
                    json=datos,
                    timeout=5
                )


                if respuesta.status_code == 201:

                    messagebox.showinfo(
                        "Correcto",
                        "Cargador agregado correctamente."
                    )

                    ventana.destroy()

                    cargar_cargadores()

                else:

                    messagebox.showerror(
                        "Error",
                        respuesta.text
                    )


            except requests.exceptions.RequestException as error:

                messagebox.showerror(
                    "Error de conexión",
                    str(error)
                )


        tk.Button(
            ventana,
            text="Guardar",
            command=guardar,
            bg="#0878df",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=20,
            pady=7,
            cursor="hand2"
        ).pack()


    # -----------------------------------------------------
    # EDITAR CARGADOR
    # -----------------------------------------------------

    def editar_cargador():

        seleccionado = obtener_seleccion()


        if seleccionado is None:

            return


        id_cargador = seleccionado[0]
        numero_actual = seleccionado[1]
        estado_actual = seleccionado[2]
        notebook_actual = seleccionado[3]
        observaciones_actual = seleccionado[4]


        ventana = tk.Toplevel(frame)

        ventana.title(
            "Editar cargador"
        )

        ventana.geometry(
            "420x380"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg="#eef1f5"
        )


        tk.Label(
            ventana,
            text="Editar cargador",
            font=("Arial", 16, "bold"),
            bg="#eef1f5",
            fg="#075ca8"
        ).pack(
            pady=15
        )


        # Número

        tk.Label(
            ventana,
            text="Número:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        num_entry = tk.Entry(
            ventana,
            width=40
        )

        num_entry.insert(
            0,
            numero_actual
        )

        num_entry.pack(
            padx=30,
            pady=(5, 15)
        )


        # Estado

        tk.Label(
            ventana,
            text="Estado:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        estado_entry = ttk.Combobox(
            ventana,
            state="readonly",
            values=[
                "Disponible",
                "En uso",
                "Dañado",
                "Reparación"
            ],
            width=37
        )

        estado_entry.set(
            estado_actual
        )

        estado_entry.pack(
            padx=30,
            pady=(5, 15)
        )


        # Notebook

        tk.Label(
            ventana,
            text="Notebook:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        notebook_entry = ttk.Combobox(
            ventana,
            state="readonly",
            width=37
        )

        notebook_entry["values"] = [
            "Sin asignar",
            notebook_actual
        ]

        notebook_entry.set(
            notebook_actual
        )

        notebook_entry.pack(
            padx=30,
            pady=(5, 15)
        )


        # Observaciones

        tk.Label(
            ventana,
            text="Observaciones:",
            bg="#eef1f5",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w",
            padx=30
        )


        observaciones_entry = tk.Entry(
            ventana,
            width=40
        )

        observaciones_entry.insert(
            0,
            observaciones_actual
        )

        observaciones_entry.pack(
            padx=30,
            pady=(5, 20)
        )


        # -------------------------------------------------
        # ACTUALIZAR
        # -------------------------------------------------

        def actualizar():

            try:

                numero = int(
                    num_entry.get()
                )

            except ValueError:

                messagebox.showwarning(
                    "Dato incorrecto",
                    "El número debe ser numérico."
                )

                return


            estado = estado_entry.get()
            observaciones = observaciones_entry.get()


            notebook_texto = notebook_entry.get()


            if notebook_texto == "Sin asignar":

                id_notebook = None

            elif notebook_texto.startswith("NB-"):

                id_notebook = int(
                    notebook_texto.replace(
                        "NB-",
                        ""
                    )
                )

            else:

                id_notebook = None


            datos = {
                "num": numero,
                "estado": estado,
                "observaciones": observaciones,
                "id_notebook": id_notebook
            }


            try:

                respuesta = requests.put(
                    f"{API_URL}/{id_cargador}",
                    json=datos,
                    timeout=5
                )


                if respuesta.status_code == 200:

                    messagebox.showinfo(
                        "Correcto",
                        "Cargador actualizado correctamente."
                    )

                    ventana.destroy()

                    cargar_cargadores()

                else:

                    messagebox.showerror(
                        "Error",
                        respuesta.text
                    )


            except requests.exceptions.RequestException as error:

                messagebox.showerror(
                    "Error de conexión",
                    str(error)
                )


        tk.Button(
            ventana,
            text="Actualizar",
            command=actualizar,
            bg="#0878df",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            padx=20,
            pady=7,
            cursor="hand2"
        ).pack()


    # -----------------------------------------------------
    # ELIMINAR CARGADOR
    # -----------------------------------------------------

    def eliminar_cargador():

        seleccionado = obtener_seleccion()


        if seleccionado is None:

            return


        id_cargador = seleccionado[0]


        confirmar = messagebox.askyesno(
            "Eliminar cargador",
            "¿Estás seguro de que querés eliminar este cargador?"
        )


        if not confirmar:

            return


        try:

            respuesta = requests.delete(
                f"{API_URL}/{id_cargador}",
                timeout=5
            )


            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Correcto",
                    "Cargador eliminado correctamente."
                )

                cargar_cargadores()

            else:

                messagebox.showerror(
                    "Error",
                    respuesta.text
                )


        except requests.exceptions.RequestException as error:

            messagebox.showerror(
                "Error de conexión",
                str(error)
            )


    # =====================================================
    # CONECTAR BOTONES
    # =====================================================

    boton_buscar.config(
        command=buscar
    )

    boton_agregar.config(
        command=agregar_cargador
    )

    boton_editar.config(
        command=editar_cargador
    )

    boton_eliminar.config(
        command=eliminar_cargador
    )


    # =====================================================
    # CARGA INICIAL
    # =====================================================

    cargar_notebooks()

    cargar_cargadores()


    return frame