import customtkinter as ctk

from data_base import data_base as db

estanteriaG = 0
# Configuración de apariencia global
ctk.set_appearance_mode("dark")  # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


def posicion_estanteria(estanterias, codigo):
    valor = -1
    for idx, datos in enumerate(estanterias):
        if int(codigo) == datos['codigo']:
            valor = idx
    return valor


def mostrar_estanterias_disponibles(biblioteca, frame):
    columnas = 0
    filas = 0
    for i, estanteria in enumerate(biblioteca):
        label = ctk.CTkLabel(
            frame,
            text=f"{estanteria['nombre']} - código {estanteria['codigo']}",
            fg_color="lightblue",
            text_color="black",
            corner_radius=8,
            padx=10,
            pady=5
        )
        label.grid(row=filas, column=columnas, padx=5, pady=5, sticky="w")
        columnas += 1
        if columnas == 2:
            columnas = 0
            filas += 1


def abrir_estanteria(frame,controller):

    biblioteca = db.get_estanterias()


    for widget in frame.winfo_children():
        widget.destroy()

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    mostrar_estanterias_disponibles(biblioteca, contenedor)

    caja_texto_ingresar_codigo = ctk.CTkEntry(contenedor, placeholder_text="Código de estantería...")
    caja_texto_ingresar_codigo.grid(row=len(biblioteca)+1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def elegir_estanteria():
        codigo = int(caja_texto_ingresar_codigo.get())
        estanteria = db.get_estanteria_seleccionada(codigo)
        print(estanteria)
        if estanteria != -1:
            controller.estanteria_actual = estanteria
            controller.mostrar_frame("VentanaMostrarEstanteria")
        else:
            print("La estantería no existe")

    boton_ver_estanteria = ctk.CTkButton(contenedor, text="Ver", command=elegir_estanteria)
    boton_ver_estanteria.grid(row=len(biblioteca)+1, column=2, padx=5, pady=5)

    # Crear nueva estantería
    label_nueva_estanteria = ctk.CTkLabel(contenedor, text="Crear nueva estantería")
    label_nueva_estanteria.grid(row=len(biblioteca)+2, column=0, padx=5, pady=5)

    boton_nueva_estanteria = ctk.CTkButton(
        contenedor,
        text="Crear",
        command=lambda: controller.mostrar_frame("VentanaCrearEstanteria")
    )
    boton_nueva_estanteria.grid(row=len(biblioteca)+2, column=1, padx=15, pady=15)


