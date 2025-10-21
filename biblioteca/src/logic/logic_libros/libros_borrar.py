import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.data import data_base as db

libros = db.get_libros()


def borrar_libro(frame, controller):
    for widget in frame.winfo_children():
        widget.destroy()
    lbl_header = ctk.CTkLabel(frame, text="Borrar Libro")
    lbl_header.pack(padx=5, pady=5)

    busqueda_frame = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)

    lbl_error = ctk.CTkLabel(busqueda_frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    caja_texto_ingresar_codigo = ctk.CTkEntry(busqueda_frame, placeholder_text="Isbn del libro que desea borrar.....")
    caja_texto_ingresar_codigo.pack(side="left", fill="x", expand=True, padx=5, pady=5)

    def elegir_estanteria():
        codigo = caja_texto_ingresar_codigo.get()
        libro = db.get_libro_por_codigo(codigo)
        if libro != -1:
            prestamos = db.buscar_libro_prestados(codigo)
            if prestamos != None:
                lbl_error.configure(text="No puede haber prestamos sin finalizar para borrar el libro")
            else:
                msg = CTkMessagebox(title="Confirmar Eliminacion",
                                    message=f"¿Confirmas que deseas borrar este libro? Esta acción no se puede revertir. ",
                                    icon="question",
                                    option_1="Sí",
                                    option_2="No",
                                    master=controller)

                if msg.get() == "Sí":
                    CTkMessagebox(title="Éxito",
                                  message=f"Eliminacion finalizada.",
                                  icon="check",
                                  master=controller)
                    db.borrar_libros_prestamos(codigo)
                    db.borrar_libro_ejemplares(codigo)
                    db.borrar_libro(codigo)
                    controller.mostrar_frame("VentanaPrincipal")

        else:
            lbl_error.configure(text="no existe libro con ese codigo")

    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Elegir", command=elegir_estanteria)
    boton_ver_estanteria.pack(side="left", padx=5, pady=5)