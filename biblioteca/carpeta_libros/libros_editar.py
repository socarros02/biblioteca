import customtkinter as ctk
from data_base import data_base as db
from CTkMessagebox import CTkMessagebox

biblioteca = db.get_estanterias()
def encontrar_estanteria(id_estanteria):
    print(id_estanteria)
    for estanteria in biblioteca:
        print(estanteria['capacidad'])
        if estanteria['codigo'] == int(id_estanteria):
            print(estanteria)
            return estanteria



def editar_libro(isbn,frame,controller,busqueda_frame,libro):

    busqueda_frame.destroy()

    lbl_isbn_viejo= ctk.CTkLabel(frame,text=f"Libro que esta editando\n{libro['titulo']} - autor {libro['autor']} - codigo {libro['codigo']}",font=("Arial", 20, "bold"))
    lbl_isbn_viejo.pack(pady=5,expand=True,fill="x")

    txt_titulo = ctk.CTkEntry(frame, placeholder_text=f"Ingrese el titulo del libro:")
    txt_titulo.pack(fill="x", expand=True, padx=5, pady=5)

    txt_autor = ctk.CTkEntry(frame, placeholder_text=f"Ingrese el autor")
    txt_autor.pack(fill="x", expand=True, padx=5, pady=5)

    txt_publicacion = ctk.CTkEntry(frame, placeholder_text=f"Ingrese año de publicacion")
    txt_publicacion.pack(fill="x", expand=True, padx=5, pady=5)

    txt_edicion = ctk.CTkEntry(frame, placeholder_text=f"Ingrese edicion")
    txt_edicion.pack(fill="x", expand=True, padx=5, pady=5)

    txt_isbn = ctk.CTkEntry(frame, placeholder_text=f"Ingrese isbn")
    txt_isbn.pack(fill="x", expand=True, padx=5, pady=5)

    lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    def validar_nuevo_libro():

        titulo = txt_titulo.get()
        autor = txt_autor.get()
        publicacion = txt_publicacion.get()
        edicion = txt_edicion.get()
        isbn_nuevo = txt_isbn.get()
        if not titulo and not autor and not publicacion and not edicion and not isbn_nuevo:
            lbl_error.configure(text="Ingrese datos validos")
            return
        try:
            existe = db.get_libro_por_codigo(isbn_nuevo)
            if existe!=None and isbn_nuevo != isbn:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Estanteria no encontrada")
            return
        msg = CTkMessagebox(title="Confirmar edicion",
                            message=f"¿Confirmas que deseas editar este libro? Esta acción no se puede revertir. ",
                            icon="question",
                            option_1="Sí",
                            option_2="No",
                            master=controller)

        if msg.get() == "Sí":
            CTkMessagebox(title="Éxito",
                          message=f"Edicion finalizada.",
                          icon="check",
                          master=controller)
            db.editar_libro(isbn_nuevo, titulo, autor, publicacion, edicion,isbn)
            controller.mostrar_frame("VentanaPrincipal")

    frame_siguiente= ctk.CTkFrame(frame, fg_color="transparent")
    frame_siguiente.pack(fill="x", expand=True, padx=5, pady=5)
    btn_siguiente = ctk.CTkButton(frame_siguiente, text="Siguiente", command=validar_nuevo_libro)
    btn_siguiente.pack(fill="x", padx=5, pady=5)




def editar_libros(frame,controller):
    controller.borrar_widget(frame)

    lbl_header = ctk.CTkLabel(frame, text="Editar Libros",font=("Arial", 45, "bold"))
    lbl_header.pack(padx=5, pady=5)

    busqueda_frame = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)

    txt_isbn = ctk.CTkEntry(busqueda_frame, placeholder_text="Isbn del libro...")
    txt_isbn.pack(side="left", fill="x", expand=True, padx=5, pady=5)


    def elegir_libro():
        isbn = txt_isbn.get()
        libro = db.get_libro_por_codigo(isbn)
        lbl_error = ctk.CTkLabel(busqueda_frame, text="", text_color="red")
        lbl_error.pack(side="bottom",fill="x", expand=True, padx=5, pady=5)

        if libro == None:
            lbl_error.configure(text="Ingrese datos validos")
            return
        else:
            frame_editar_libro = ctk.CTkFrame(frame, fg_color="transparent")
            frame_editar_libro.pack(fill="x", pady=10, padx=10)
            editar_libro(isbn,frame_editar_libro,controller,busqueda_frame,libro)

    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Elegir", command=elegir_libro)
    boton_ver_estanteria.pack(side="left", padx=5,pady=5)


