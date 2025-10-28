from src.data import data_base as db
import customtkinter as ctk



def mostrar_libro(libro,controller):
    controller.libro_seleccionado= libro
    controller.libros = db.get_libros()
    controller.mostrar_frame("VentanaMostrarPrestarLibros")
def lista_libros(scroll_frame, controller):

    controller.borrar_widget(scroll_frame)

    for libro in controller.libros:
        contenedor_libro = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=10)
        contenedor_libro.pack(fill="x", pady=5, padx=10, expand=True)

        btn_libro = ctk.CTkButton(
            contenedor_libro,
            text=f"📖 TITULO: {libro['titulo']}  | CODIGO: {libro['codigo']}  | AUTOR: {libro['autor']}",
            text_color="white",
            anchor="w",
            command=lambda libroX=libro: mostrar_libro(libroX, controller)
        )
        btn_libro.pack(padx=10, pady=5, expand=True, fill="x")


def mostrar_libros(frame, controller):

    busqueda = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda.pack(padx=5, pady=5, fill="x")


    txt_buscar = ctk.CTkEntry(busqueda, placeholder_text="Buscar libro por código, título o autor...")
    txt_buscar.pack(pady=5, padx=5, side="left", fill="x", expand=True)


    scroll_frame = ctk.CTkScrollableFrame(frame,fg_color="transparent")
    scroll_frame.pack(pady=20, expand=True, fill="both")


    def buscar_libro():
        termino = txt_buscar.get()
        libros = db.buscar_libros(termino)
        if libros:
            controller.libros = libros

        else:
            controller.libros = []
            print("No existe ese libro")
        lista_libros(scroll_frame, controller)


    btn_buscar = ctk.CTkButton(busqueda, text="Buscar", command=buscar_libro)
    btn_buscar.pack(pady=5, padx=5, side="left")

    lista_libros(scroll_frame, controller)


