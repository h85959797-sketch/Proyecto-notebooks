import tkinter as tk
from tkinter import ttk, messagebox
import requests


# ============================================================
# CONFIGURACIÓN
# ============================================================

API_URL = "http://localhost:3000/notebooks"


# ============================================================
# COLORES
# ============================================================

AZUL_OSCURO = "#064A9B"
AZUL = "#0875E1"
AZUL_CLARO = "#2F8CF4"
AZUL_MUY_CLARO = "#DCEEFF"

BLANCO = "#FFFFFF"
FONDO = "#EEF7FF"
BORDE = "#9CCBFA"


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def crear_notebooks(parent):

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
        foreground="#123B72",
        rowheight=48,
        fieldbackground=BLANCO,
        font=("Segoe UI", 11),
        borderwidth=0
    )

    style.configure(
        "Treeview.Heading",
        background=AZUL_MUY_CLARO,
        foreground="#123B72",
        font=("Segoe UI", 11, "bold"),
        padding=10
    )

    style.map(
        "Treeview",
        background=[
            ("selected", "#B9DCFF")
        ],
        foreground=[
            ("selected", "#123B72")
        ]
    )

    # ========================================================
    # CONTENIDO PRINCIPAL
    # ========================================================

    contenido = tk.Frame(
        frame,
        bg=FONDO
    )

    contenido.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # ========================================================
    # FUNCIONES
    # ========================================================

    def limpiar_formulario():

        combo_marca.set("")
        combo_empresa.set("")

        entry_serie.delete(
            0,
            tk.END
        )

        combo_estado.set("")

        tree.selection_remove(
            tree.selection()
        )

    # --------------------------------------------------------
    # CARGAR NOTEBOOKS
    # --------------------------------------------------------

    def cargar_notebooks():

        for item in tree.get_children():
            tree.delete(item)

        try:

            respuesta = requests.get(
                API_URL,
                timeout=5
            )

            if respuesta.status_code != 200:

                raise Exception(
                    f"Error HTTP {respuesta.status_code}"
                )

            notebooks = respuesta.json()

            for notebook in notebooks:

                tree.insert(
                    "",
                    tk.END,
                    iid=str(
                        notebook["id_notebook"]
                    ),
                    values=(
                        notebook["marca"],
                        notebook["empresa"],
                        notebook["num_serie"],
                        notebook["estado"]
                    )
                )

            label_total.config(
                text=f"Total de notebooks: {len(notebooks)}"
            )

        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el backend.\n\n"
                "Verificá que tu servidor Node.js esté ejecutándose."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                f"No se pudieron cargar las notebooks.\n\n{error}"
            )

    # --------------------------------------------------------
    # SELECCIONAR NOTEBOOK
    # --------------------------------------------------------

    def seleccionar_notebook(event=None):

        seleccion = tree.selection()

        if not seleccion:
            return

        item_id = seleccion[0]

        valores = tree.item(
            item_id,
            "values"
        )

        if not valores:
            return

        combo_marca.set(
            valores[0]
        )

        combo_empresa.set(
            valores[1]
        )

        entry_serie.delete(
            0,
            tk.END
        )

        entry_serie.insert(
            0,
            valores[2]
        )

        combo_estado.set(
            valores[3]
        )

    # --------------------------------------------------------
    # AGREGAR
    # --------------------------------------------------------

    def agregar_notebook():

        marca = combo_marca.get().strip()
        empresa = combo_empresa.get().strip()
        num_serie = entry_serie.get().strip()
        estado = combo_estado.get().strip()

        if (
            not marca
            or not empresa
            or not num_serie
            or not estado
        ):

            messagebox.showwarning(
                "Datos incompletos",
                "Completá todos los campos antes de agregar."
            )

            return

        datos = {
            "marca": marca,
            "empresa": empresa,
            "num_serie": num_serie,
            "estado": estado
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
                    "Notebook agregada correctamente."
                )

                limpiar_formulario()
                cargar_notebooks()

            else:

                try:

                    mensaje = respuesta.json().get(
                        "error",
                        "No se pudo agregar la notebook."
                    )

                except:

                    mensaje = (
                        "No se pudo agregar la notebook."
                    )

                messagebox.showerror(
                    "Error",
                    mensaje
                )

        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el backend."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # --------------------------------------------------------
    # MODIFICAR
    # --------------------------------------------------------

    def modificar_notebook():

        seleccion = tree.selection()

        if not seleccion:

            messagebox.showwarning(
                "Seleccionar notebook",
                "Seleccioná una notebook de la tabla para modificar."
            )

            return

        id_notebook = seleccion[0]

        marca = combo_marca.get().strip()
        empresa = combo_empresa.get().strip()
        num_serie = entry_serie.get().strip()
        estado = combo_estado.get().strip()

        if (
            not marca
            or not empresa
            or not num_serie
            or not estado
        ):

            messagebox.showwarning(
                "Datos incompletos",
                "Completá todos los campos."
            )

            return

        datos = {
            "marca": marca,
            "empresa": empresa,
            "num_serie": num_serie,
            "estado": estado
        }

        try:

            respuesta = requests.put(
                f"{API_URL}/{id_notebook}",
                json=datos,
                timeout=5
            )

            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Éxito",
                    "Notebook modificada correctamente."
                )

                limpiar_formulario()
                cargar_notebooks()

            else:

                try:

                    mensaje = respuesta.json().get(
                        "error",
                        "No se pudo modificar la notebook."
                    )

                except:

                    mensaje = (
                        "No se pudo modificar la notebook."
                    )

                messagebox.showerror(
                    "Error",
                    mensaje
                )

        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el backend."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # --------------------------------------------------------
    # ELIMINAR
    # --------------------------------------------------------

    def eliminar_notebook():

        seleccion = tree.selection()

        if not seleccion:

            messagebox.showwarning(
                "Seleccionar notebook",
                "Seleccioná una notebook de la tabla para eliminar."
            )

            return

        id_notebook = seleccion[0]

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Estás seguro de que querés eliminar esta notebook?"
        )

        if not confirmar:
            return

        try:

            respuesta = requests.delete(
                f"{API_URL}/{id_notebook}",
                timeout=5
            )

            if respuesta.status_code == 200:

                messagebox.showinfo(
                    "Éxito",
                    "Notebook eliminada correctamente."
                )

                limpiar_formulario()
                cargar_notebooks()

            else:

                try:

                    mensaje = respuesta.json().get(
                        "error",
                        "No se pudo eliminar la notebook."
                    )

                except:

                    mensaje = (
                        "No se pudo eliminar la notebook."
                    )

                messagebox.showerror(
                    "Error",
                    mensaje
                )

        except requests.exceptions.ConnectionError:

            messagebox.showerror(
                "Error de conexión",
                "No se pudo conectar con el backend."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
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
        pady=(0, 20)
    )

    tk.Label(
        encabezado,
        text="▣",
        font=("Segoe UI", 42),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        side="left",
        padx=(25, 15),
        pady=15
    )

    titulo_frame = tk.Frame(
        encabezado,
        bg=AZUL
    )

    titulo_frame.pack(
        side="left",
        pady=20
    )

    tk.Label(
        titulo_frame,
        text="Gestión de Notebooks",
        font=("Segoe UI", 25, "bold"),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        anchor="w"
    )

    tk.Label(
        titulo_frame,
        text="Administrá los datos de las notebooks de la empresa.",
        font=("Segoe UI", 12),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        anchor="w"
    )

    # ========================================================
    # PANEL DE DATOS
    # ========================================================

    panel_datos = tk.Frame(
        contenido,
        bg=BLANCO,
        highlightbackground=BORDE,
        highlightthickness=1
    )

    panel_datos.pack(
        fill="x",
        pady=(0, 20)
    )

    # --------------------------------------------------------
    # TÍTULO
    # --------------------------------------------------------

    tk.Label(
        panel_datos,
        text="Datos de la Notebook",
        font=("Segoe UI", 15, "bold"),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        fill="x",
        ipady=10
    )

    # --------------------------------------------------------
    # FORMULARIO
    # --------------------------------------------------------

    formulario = tk.Frame(
        panel_datos,
        bg=BLANCO
    )

    formulario.pack(
        fill="x",
        padx=18,
        pady=15
    )

    formulario.columnconfigure(
        0,
        weight=1
    )

    formulario.columnconfigure(
        1,
        weight=1
    )

    formulario.columnconfigure(
        2,
        weight=1
    )

    formulario.columnconfigure(
        3,
        weight=1
    )

    # ========================================================
    # MARCA
    # ========================================================

    tk.Label(
        formulario,
        text="Marca:",
        font=("Segoe UI", 11, "bold"),
        fg="#123B72",
        bg=BLANCO
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=5
    )

    combo_marca = ttk.Combobox(
        formulario,
        values=[
            "Lenovo",
            "HP",
            "Dell",
            "Asus",
            "Acer",
            "Toshiba"
        ],
        state="readonly",
        font=("Segoe UI", 11)
    )

    combo_marca.grid(
        row=1,
        column=0,
        sticky="ew",
        padx=5,
        pady=(5, 15)
    )

    # ========================================================
    # EMPRESA
    # ========================================================

    tk.Label(
        formulario,
        text="Empresa:",
        font=("Segoe UI", 11, "bold"),
        fg="#123B72",
        bg=BLANCO
    ).grid(
        row=0,
        column=1,
        sticky="w",
        padx=5
    )

    combo_empresa = ttk.Combobox(
        formulario,
        values=[
            "TechSolutions",
            "Innovatech",
            "GlobalSoft",
            "NextWave",
            "DataCorp",
            "Soluciones IT"
        ],
        state="readonly",
        font=("Segoe UI", 11)
    )

    combo_empresa.grid(
        row=1,
        column=1,
        sticky="ew",
        padx=5,
        pady=(5, 15)
    )

    # ========================================================
    # NÚMERO DE SERIE
    # ========================================================

    tk.Label(
        formulario,
        text="Número de Serie:",
        font=("Segoe UI", 11, "bold"),
        fg="#123B72",
        bg=BLANCO
    ).grid(
        row=0,
        column=2,
        sticky="w",
        padx=5
    )

    entry_serie = tk.Entry(
        formulario,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1,
        fg="#123B72"
    )

    entry_serie.grid(
        row=1,
        column=2,
        sticky="ew",
        padx=5,
        pady=(5, 15),
        ipady=8
    )

    # ========================================================
    # ESTADO
    # ========================================================

    tk.Label(
        formulario,
        text="Estado:",
        font=("Segoe UI", 11, "bold"),
        fg="#123B72",
        bg=BLANCO
    ).grid(
        row=0,
        column=3,
        sticky="w",
        padx=5
    )

    combo_estado = ttk.Combobox(
        formulario,
        values=[
            "En buen estado",
            "En reparación",
            "Dado de baja"
        ],
        state="readonly",
        font=("Segoe UI", 11)
    )

    combo_estado.grid(
        row=1,
        column=3,
        sticky="ew",
        padx=5,
        pady=(5, 15)
    )

    # ========================================================
    # BOTONES
    # ========================================================

    botones = tk.Frame(
        formulario,
        bg=BLANCO
    )

    botones.grid(
        row=2,
        column=0,
        columnspan=4,
        sticky="ew"
    )

    for columna in range(4):

        botones.columnconfigure(
            columna,
            weight=1
        )

    def boton_accion(texto, comando):

        return tk.Button(
            botones,
            text=texto,
            command=comando,
            font=("Segoe UI", 11, "bold"),
            fg=BLANCO,
            bg=AZUL,
            activebackground=AZUL_CLARO,
            activeforeground=BLANCO,
            relief="flat",
            bd=0,
            cursor="hand2"
        )

    boton_accion(
        "＋  Agregar",
        agregar_notebook
    ).grid(
        row=0,
        column=0,
        sticky="ew",
        padx=5,
        ipady=10
    )

    boton_accion(
        "✎  Modificar",
        modificar_notebook
    ).grid(
        row=0,
        column=1,
        sticky="ew",
        padx=5,
        ipady=10
    )

    boton_accion(
        "▣  Eliminar",
        eliminar_notebook
    ).grid(
        row=0,
        column=2,
        sticky="ew",
        padx=5,
        ipady=10
    )

    boton_accion(
        "⟳  Limpiar",
        limpiar_formulario
    ).grid(
        row=0,
        column=3,
        sticky="ew",
        padx=5,
        ipady=10
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

    # --------------------------------------------------------
    # TÍTULO LISTADO
    # --------------------------------------------------------

    tk.Label(
        panel_lista,
        text="Listado de Notebooks",
        font=("Segoe UI", 15, "bold"),
        fg=BLANCO,
        bg=AZUL
    ).pack(
        fill="x",
        ipady=10
    )

    # --------------------------------------------------------
    # TABLA
    # --------------------------------------------------------

    tabla_frame = tk.Frame(
        panel_lista,
        bg=BLANCO
    )

    tabla_frame.pack(
        fill="both",
        expand=True,
        padx=18,
        pady=15
    )

    columnas = (
        "marca",
        "empresa",
        "serie",
        "estado"
    )

    tree = ttk.Treeview(
        tabla_frame,
        columns=columnas,
        show="headings",
        selectmode="browse"
    )

    tree.heading(
        "marca",
        text="Marca"
    )

    tree.heading(
        "empresa",
        text="Empresa"
    )

    tree.heading(
        "serie",
        text="Número de Serie"
    )

    tree.heading(
        "estado",
        text="Estado"
    )

    tree.column(
        "marca",
        width=180,
        anchor="w"
    )

    tree.column(
        "empresa",
        width=220,
        anchor="w"
    )

    tree.column(
        "serie",
        width=220,
        anchor="w"
    )

    tree.column(
        "estado",
        width=200,
        anchor="w"
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

    tree.bind(
        "<<TreeviewSelect>>",
        seleccionar_notebook
    )

    # ========================================================
    # PIE
    # ========================================================

    pie = tk.Frame(
        panel_lista,
        bg=AZUL_MUY_CLARO
    )

    pie.pack(
        fill="x",
        padx=18,
        pady=(0, 15)
    )

    label_total = tk.Label(
        pie,
        text="Total de notebooks: 0",
        font=("Segoe UI", 10),
        fg="#064A9B",
        bg=AZUL_MUY_CLARO
    )

    label_total.pack(
        side="left",
        padx=15,
        pady=10
    )

    # ========================================================
    # CARGAR DATOS
    # ========================================================

    cargar_notebooks()

    # ========================================================
    # RETORNAR FRAME
    # ========================================================

    return frame