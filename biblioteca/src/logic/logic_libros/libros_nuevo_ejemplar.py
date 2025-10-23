import customtkinter as ctk
from src.data import data_base as db
from CTkMessagebox import CTkMessagebox


def encontrar_estanteria(id_estanteria,biblioteca):
    print(id_estanteria)
    for estanteria in biblioteca:
        print(estanteria['capacidad'])
        if estanteria['codigo'] == int(id_estanteria):
            print(estanteria)
            return estanteria



def cargar_libro_nuevo(isbn,frame,controller):
    biblioteca = db.get_estanterias()

    txt_titulo = ctk.CTkEntry(frame, placeholder_text=f"Ingrese el titulo del libro:")
    txt_titulo.pack(fill="x", expand=True, padx=5, pady=5)

    txt_autor = ctk.CTkEntry(frame, placeholder_text=f"Ingrese el autor")
    txt_autor.pack(fill="x", expand=True, padx=5, pady=5)

    txt_publicacion = ctk.CTkEntry(frame, placeholder_text=f"Ingrese año de publicacion")
    txt_publicacion.pack(fill="x", expand=True, padx=5, pady=5)

    txt_edicion = ctk.CTkEntry(frame, placeholder_text=f"Ingrese edicion")
    txt_edicion.pack(fill="x", expand=True, padx=5, pady=5)

    txt_estanteria = ctk.CTkEntry(frame, placeholder_text=f"Ingrese estanteria donde almacenara los ejemplares")
    txt_estanteria.pack(fill="x", expand=True, padx=5, pady=5)

    lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    def validar_nuevo_libro(frame_siguiente):
        titulo = txt_titulo.get()
        autor = txt_autor.get()
        publicacion = txt_publicacion.get()
        edicion = txt_edicion.get()
        estant = txt_estanteria.get()
        if not titulo and not autor and not publicacion and not edicion and not estant:
            lbl_error.configure(text="Ingrese datos validos")
            return
        try:
            existe = encontrar_estanteria(estant,biblioteca)
            if existe==None:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Estanteria no encontrada")
            return
        db.nuevo_libro(isbn, titulo, autor, publicacion, edicion)
        capacidad = cantidad_disponible(isbn,estant)
        controller.borrar_widget(frame_siguiente)
        controller.borrar_widget(frame)
        cantidad_ejemplares(isbn,capacidad,frame,estant,controller)

    frame_siguiente= ctk.CTkFrame(frame, fg_color="transparent")
    frame_siguiente.pack(fill="x", expand=True, padx=5, pady=5)
    btn_siguiente = ctk.CTkButton(frame_siguiente, text="Siguiente", command=lambda :validar_nuevo_libro(frame_siguiente))
    btn_siguiente.pack(fill="x", padx=5, pady=5)



def cantidad_disponible(isbn,estanteria):
    biblioteca = db.get_estanterias()
    if estanteria==-1:
        estanteria=db.get_ubicacion_ejemplar(isbn)
    print(estanteria)
    libros_en_estanteria = db.contar_ejemplares_por_estanteria(estanteria)
    estanteria_seleccionada = encontrar_estanteria(estanteria,biblioteca)
    capacidad_disponible =  estanteria_seleccionada["capacidad"]-libros_en_estanteria
    return capacidad_disponible

def cantidad_ejemplares(isbn,capacidad,frame,estanteria,controller):
    if estanteria==-1:
        estanteria=db.get_ubicacion_ejemplar(isbn)
    lbl_aviso = ctk.CTkLabel(frame,text=f"Los ejemplares de este titulo seran cargados en la estanteria codigo {estanteria}. \nComo maximo puede cargar {capacidad} de ejemplares. "
                                        f"\nSi desea agregar mas debe antes reubicar los otros ejemplares en otra estanteriacon mayor capacidad")
    lbl_aviso.pack(fill="x", expand=True, padx=5,pady=5)

    lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    txt_cantidad = ctk.CTkEntry(frame, placeholder_text=f"Ingrese la cantidad de ejemplares")
    txt_cantidad.pack(side="left", fill="x", expand=True, padx=5, pady=5)

    def validar_ingreso():
        cantidad = txt_cantidad.get()
        if not cantidad:
            lbl_error.configure(text="Ingrese datos validos")
            return

        try:
            cantidad = int(cantidad)
            if capacidad<cantidad:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Ingrese datos validos")
            return

        CTkMessagebox(title="Éxito",
                      message=f"Ejemplares agregados con exito",
                      icon="check",
                      master=controller)
        for i in range(cantidad):
            db.carga_nuevo_ejemplar(estanteria,isbn)

        controller.mostrar_frame("VentanaPrincipal")




    btn_insertar_ejemplares = ctk.CTkButton(frame, text="guardar", command=validar_ingreso, width=200)
    btn_insertar_ejemplares.pack(side="left",padx=5,pady=5,fill="x",expand=True)

def nuevos_ejemplares(frame,controller):
    controller.borrar_widget(frame)

    lbl_header = ctk.CTkLabel(frame, text="Nuevos ejemplares")
    lbl_header.pack(padx=5, pady=5)

    busqueda_frame = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)

    contenedor = ctk.CTkFrame(frame, fg_color="transparent")
    contenedor.pack(fill="x", pady=10, padx=10)

    scroll_frame = ctk.CTkScrollableFrame(contenedor, fg_color="transparent")
    scroll_frame.pack(pady=20, expand=True, fill="x")

    txt_isbn = ctk.CTkEntry(busqueda_frame, placeholder_text="Isbn del ejemplar, si el libro ya existe puede elegir clickeando abajo...")
    txt_isbn.pack(side="left", fill="x", expand=True, padx=5, pady=5)


    def elegir_libro():
        isbn = txt_isbn.get()
        libro = db.get_libro_por_codigo(isbn)
        contenedor.destroy()

        if libro != None:
            frame_cantidad_ejemplares= ctk.CTkFrame(frame, fg_color="transparent")
            frame_cantidad_ejemplares.pack(fill="x", pady=10, padx=10)
            disponible=cantidad_disponible(isbn,-1)
            cantidad_ejemplares(isbn,disponible,frame_cantidad_ejemplares,-1,controller)
        else:
            frame_nuevo_libro = ctk.CTkFrame(frame, fg_color="transparent")
            frame_nuevo_libro.pack(fill="x", pady=10, padx=10)

            cargar_libro_nuevo(isbn,frame_nuevo_libro,controller)

    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Elegir", command=elegir_libro)
    boton_ver_estanteria.pack(side="left", padx=5,pady=5)


    for libro in controller.libros:
        libro_actual = libro

        def seleccionar_libro(isbn):
            txt_isbn.delete(0, "end")
            txt_isbn.insert(0, isbn)
        contenedor_libro = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=10)
        contenedor_libro.pack(fill="x", pady=5, padx=10,expand=True)

        btn_libro = ctk.CTkButton(
            contenedor_libro,
            text=f"📖 TITULO: {libro_actual['titulo']}  | CODIGO: {libro_actual['codigo']}  | AUTOR: {libro_actual['autor']}",
            text_color="white",
            command=lambda isbn=libro_actual['codigo']: seleccionar_libro(isbn)
        )
        btn_libro.pack(padx=10, pady=5,expand=True,fill="x")


