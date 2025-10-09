import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from data_base import data_base as db

biblioteca = db.get_estanterias()

def cambiar_valores(codigo,frame_valores,controller):

    libros_en_estanteria = db.contar_ejemplares_por_estanteria(codigo)


    txt_nombre_estanteria = ctk.CTkEntry(frame_valores, placeholder_text="Ingresar nombre de estaneria nueva.....")
    txt_nombre_estanteria.pack(fill="x", expand=True, padx=5,pady=5)

    txt_capacidad_maxima = ctk.CTkEntry(frame_valores, placeholder_text=f"Ingresar nueva capacidad, maximo 150 libros, minimo{libros_en_estanteria} .....")
    txt_capacidad_maxima.pack(fill="x", expand=True, padx=5,pady=5)

    lbl_error = ctk.CTkLabel(frame_valores, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5,pady=5)

    def validar_ingreso():
        nombre = txt_nombre_estanteria.get()
        capacidad_maxima = txt_capacidad_maxima.get()
        if not nombre or not capacidad_maxima:
            lbl_error.configure(text="Ingrese datos validos")
            return

        try:
            capacidad = int(capacidad_maxima)
            if capacidad <= libros_en_estanteria or capacidad > 150:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Ingrese datos validos")
            return
        print(nombre,capacidad)
        msg = CTkMessagebox(title="Confirmar edicion",
                            message=f"¿Confirmas que deseas editar esta estanteria? Esta acción no se puede revertir. ",
                            icon="question",
                            option_1="Sí",
                            option_2="No",
                            master=controller)

        if msg.get() == "Sí":
            CTkMessagebox(title="Éxito",
                          message=f"Edicion finalizada.",
                          icon="check",
                          master=controller)
            db.editar_estaneria(codigo,nombre,capacidad)
            controller.mostrar_frame("VentanaPrincipal")

    btn_crear_estanteria = ctk.CTkButton(frame_valores, text="editar", command=validar_ingreso, width=200)
    btn_crear_estanteria.pack(side="left",padx=5,pady=5,fill="x",expand=True)


def editar_estanteria(frame,controller):
    for widget in frame.winfo_children():
        widget.destroy()
    lbl_header = ctk.CTkLabel(frame, text="Editar estanteria")
    lbl_header.pack(padx=5, pady=5)

    busqueda_frame = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)

    caja_texto_ingresar_codigo = ctk.CTkEntry(busqueda_frame, placeholder_text="Código de estantería...")
    caja_texto_ingresar_codigo.pack(side="left", fill="x", expand=True, padx=5, pady=5)
    def elegir_estanteria():
        codigo = int(caja_texto_ingresar_codigo.get())
        estanteria = db.get_estanteria_seleccionada(codigo)
        if estanteria != -1:
            frame_nuevos_valores= ctk.CTkFrame(frame, fg_color="transparent")
            frame_nuevos_valores.pack(fill="x", pady=10, padx=10)
            cambiar_valores(estanteria,frame_nuevos_valores,controller)
        else:
            print("La estantería no existe")

    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Elegir", command=elegir_estanteria)
    boton_ver_estanteria.pack(side="left", padx=5,pady=5)