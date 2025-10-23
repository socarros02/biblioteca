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

    txt_isbn = ctk.CTkEntry(busqueda_frame, placeholder_text="Isbn del libro que desea borrar.....")
    txt_isbn.pack(side="left", fill="x", expand=True, padx=5, pady=5)

    def elegir_estanteria():
        codigo = txt_isbn.get()
        libro = db.get_libro_por_codigo(codigo)
        prestado = 0
        if libro != -1:
            prestamos = db.buscar_libro_prestados(codigo)
            if prestamos != None:
                for prestamo in prestamos:

                    if prestamo[0] == 0:
                        prestado = 1

            if prestado == 1:
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

    scroll_frame = ctk.CTkScrollableFrame(frame, fg_color="transparent")
    scroll_frame.pack(pady=20, expand=True, fill="x")

    for libro in controller.libros:
        libro_actual = libro

        def seleccionar_libro(isbn):
            txt_isbn.delete(0, "end")
            txt_isbn.insert(0, isbn)

        contenedor_libro = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=10)
        contenedor_libro.pack(fill="x", pady=5, padx=10, expand=True)

        btn_libro = ctk.CTkButton(
            contenedor_libro,
            text=f"📖 TITULO: {libro_actual['titulo']}  | CODIGO: {libro_actual['codigo']}  | AUTOR: {libro_actual['autor']}",
            text_color="white",
            command=lambda isbn=libro_actual['codigo']: seleccionar_libro(isbn)
        )
        btn_libro.pack(padx=10, pady=5, expand=True, fill="x")