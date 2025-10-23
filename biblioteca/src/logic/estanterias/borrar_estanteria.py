import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data import data_base as db

biblioteca = db.get_estanterias()

def borrar_estanteria(frame,controller):
    for widget in frame.winfo_children():
        widget.destroy()
    lbl_header = ctk.CTkLabel(frame, text="Borrar Estanteria")
    lbl_header.pack(padx=5, pady=5)

    busqueda_frame = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)

    contenedor=ctk.CTkFrame(frame, fg_color="transparent")
    contenedor.pack(fill="x", pady=10, padx=10)

    lbl_error = ctk.CTkLabel(busqueda_frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    txt = ctk.CTkEntry(busqueda_frame, placeholder_text="Código de estantería...")
    txt.pack(side="left", fill="x", expand=True, padx=5, pady=5)



    def elegir_estanteria():
        codigo = int(txt.get())
        estanteria = db.get_estanteria_seleccionada(codigo)
        if estanteria != -1:
            ejemplares = db.contar_ejemplares_por_estanteria(codigo)
            if ejemplares!=0:
                lbl_error.configure(text="La estanteria debe estar vacia para ser eliminada")
            else:
                msg = CTkMessagebox(title="Confirmar Eliminacion",
                                    message=f"¿Confirmas que deseas borrar esta estanteria? Esta acción no se puede revertir. ",
                                    icon="question",
                                    option_1="Sí",
                                    option_2="No",
                                    master=controller)

                if msg.get() == "Sí":
                    CTkMessagebox(title="Éxito",
                                  message=f"Edicion finalizada.",
                                  icon="check",
                                  master=controller)
                    db.eliminar_estanteria(codigo)

        else:
            lbl_error.configure(text="no existe estanteria con ese codigo")


    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Elegir", command=elegir_estanteria)
    boton_ver_estanteria.pack(side="left", padx=5,pady=5)

    scroll_frame = ctk.CTkScrollableFrame(contenedor)
    scroll_frame.pack(expand=True, fill="x")
    controller.borrar_widget(scroll_frame)
    biblioteca = db.get_estanterias()

    for estanteria in biblioteca:
        def seleccionar_estanteria(estanteria):
            txt.delete(0, "end")
            txt.insert(0, estanteria)

        fila_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=5)
        fila_frame.pack(fill="x", pady=2)
        estanteria_actual = estanteria
        disponible = estanteria_actual['capacidad'] - db.contar_ejemplares_por_estanteria(
            estanteria_actual["codigo"])

        btn_ver = ctk.CTkButton(
            fila_frame,
            text=f"🗄️{estanteria_actual['nombre']}   -   código {estanteria_actual['codigo']}  -   capacidad {estanteria_actual['capacidad']}  -  espacios disponibles {disponible}",
            text_color="white",
            command=lambda estanteriaX=estanteria_actual['codigo']: seleccionar_estanteria(estanteriaX),
            width=25
        )
        btn_ver.pack(pady=5, padx=15, expand=True, fill="x")