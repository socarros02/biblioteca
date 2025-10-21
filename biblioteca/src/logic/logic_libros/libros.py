from src.data import data_base as db
import customtkinter as ctk



def mostrar_libro(libro,controller):
    controller.libro_seleccionado= libro
    controller.mostrar_frame("VentanaMostrarPrestarLibros")


def mostrar_libros(frame,controller):

    controller.libros=db.get_libros()


    busqueda = ctk.CTkFrame(frame,fg_color="transparent")
    busqueda.pack(padx=5, pady=5,expand=True,fill="x")
    controller.borrar_widget(busqueda)

    busqueda_titulo = ctk.CTkFrame(busqueda,fg_color="transparent")
    busqueda_titulo.pack(expand=True,fill="x")
    busqueda_codigo = ctk.CTkFrame(busqueda,fg_color="transparent")
    busqueda_codigo.pack(expand=True,fill="x")
    busqueda_autor = ctk.CTkFrame(busqueda,fg_color="transparent")
    busqueda_autor.pack(expand=True,fill="x")

    scroll_frame = ctk.CTkScrollableFrame(frame)
    scroll_frame.pack(pady=20,expand=True,fill="x")

    for libro in controller.libros:
        libro_actual = libro

        contenedor_libro = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=10)
        contenedor_libro.pack(fill="x", pady=5, padx=10,expand=True)

        btn_libro = ctk.CTkButton(
            contenedor_libro,
            text=f"📖 TITULO: {libro_actual['titulo']}  | CODIGO: {libro_actual['codigo']}  | AUTOR: {libro_actual['autor']}",
            text_color="white",
            command=lambda libroX=libro_actual: mostrar_libro(libroX, controller)
        )
        btn_libro.pack(padx=10, pady=5,expand=True,fill="x")





    def buscar_titulo():
        titulo = txt_buscar_titulo.get()
        libro = db.get_libro_por_titulo(titulo)
        if libro:
            controller.libro_seleccionado= libro
            controller.mostrar_frame("VentanaMostrarPrestarLibros")
        else:
            print("La estantería no existe")

    def buscar_codigo():
        codigo = txt_buscar_codigo.get()
        libro = db.get_libro_por_codigo(codigo)
        if libro:
            controller.libro_seleccionado = libro
            controller.mostrar_frame("VentanaMostrarPrestarLibros")
        else:
            print("No existe ese libro")

    def buscar_autor():
        autor = txt_buscar_autor.get()
        libros_autor = db.get_libros_por_autor(autor)
        if libros_autor:
            controller.autor_seleccionado = libros_autor
            controller.mostrar_frame("VentanaLibrosAutor")

        else:
            print("No existe ese autor")



    txt_buscar_titulo = ctk.CTkEntry(busqueda_titulo, placeholder_text="buscar libro por titulo...")
    txt_buscar_titulo.pack(pady=5,padx=5,side="left",fill="x",expand=True)


    txt_buscar_codigo = ctk.CTkEntry(busqueda_codigo, placeholder_text="buscar libro por codigo...")
    txt_buscar_codigo.pack(pady=5,padx=5,side="left",fill="x",expand=True)

    txt_buscar_autor = ctk.CTkEntry(busqueda_autor, placeholder_text="buscar libro por autor...")
    txt_buscar_autor.pack(pady=5,padx=5,side="left",fill="x",expand=True)

    btn_buscar_titulo = ctk.CTkButton(busqueda_titulo, text="buscar", command=buscar_titulo)
    btn_buscar_titulo.pack(pady=5,padx=5,side="left")

    btn_buscar_codigo = ctk.CTkButton(busqueda_codigo, text="buscar", command=buscar_codigo)
    btn_buscar_codigo.pack(pady=5,padx=5,side="left")

    btn_buscar_autor = ctk.CTkButton(busqueda_autor, text="buscar", command=buscar_autor)
    btn_buscar_autor.pack(pady=5,padx=5,side="left")





