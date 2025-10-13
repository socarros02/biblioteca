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

    lbl_error = ctk.CTkLabel(busqueda_frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    caja_texto_ingresar_codigo = ctk.CTkEntry(busqueda_frame, placeholder_text="Código de estantería...")
    caja_texto_ingresar_codigo.pack(side="left", fill="x", expand=True, padx=5, pady=5)



    def elegir_estanteria():
        codigo = int(caja_texto_ingresar_codigo.get())
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