import customtkinter as ctk

from data_base import data_base as db



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def posicion_estanteria(estanterias, codigo):
    valor = -1
    for idx, datos in enumerate(estanterias):
        if int(codigo) == datos['codigo']:
            valor = idx
    return valor


def mostrar_estanterias_disponibles(biblioteca, frame):

    lista_frame = ctk.CTkFrame(frame, fg_color="transparent")
    lista_frame.pack(fill="both", expand=True, pady=10)

    fila_frame = None
    for i, estanteria in enumerate(biblioteca):

        if i % 2 == 0:
            fila_frame = ctk.CTkFrame(lista_frame, fg_color="transparent")
            fila_frame.pack(fill="x", pady=2)

        label = ctk.CTkLabel(
            fila_frame,
            text=f"{estanteria['nombre']} - código {estanteria['codigo']}",
            fg_color="lightblue",
            text_color="black",
            corner_radius=8,
            padx=10,
            pady=5
        )
        label.pack(side="left", padx=5, pady=5, fill="x", expand=True)


def abrir_estanteria(frame,controller):

    biblioteca = db.get_estanterias()


    for widget in frame.winfo_children():
        widget.destroy()

    header = ctk.CTkFrame(frame, fg_color="transparent",height=10)
    header.pack( padx=5, pady=5)

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_header = ctk.CTkLabel(header, text= "Estanterias",corner_radius=15,font=("Arial",40))
    lbl_header.pack(padx=5, pady=5,expand=True)

    mostrar_estanterias_disponibles(biblioteca, contenedor)

    busqueda_frame = ctk.CTkFrame(frame,fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10,padx=10)


    caja_texto_ingresar_codigo = ctk.CTkEntry(busqueda_frame, placeholder_text="Código de estantería...")
    caja_texto_ingresar_codigo.pack(side="left", fill="x", expand=True, padx=5,pady=5)

    def elegir_estanteria():
        codigo = int(caja_texto_ingresar_codigo.get())
        estanteria = db.get_estanteria_seleccionada(codigo)
        print(estanteria)
        if estanteria != -1:
            controller.estanteria_actual = estanteria
            controller.mostrar_frame("VentanaMostrarEstanteria")
        else:
            print("La estantería no existe")

    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Ver", command=elegir_estanteria)
    boton_ver_estanteria.pack(side="left", padx=5,pady=5)

    nueva_estanteria_frame = ctk.CTkFrame(frame,fg_color="transparent")
    nueva_estanteria_frame.pack(fill="x", pady=10)

    boton_nueva_estanteria = ctk.CTkButton(nueva_estanteria_frame,text="Crear nueva estanteria",command=lambda: controller.mostrar_frame("VentanaCrearEstanteria"),width=250)
    boton_nueva_estanteria.pack(padx=5,pady=5)


