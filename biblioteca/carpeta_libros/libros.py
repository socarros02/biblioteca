from functools import cmp_to_key
from data_base import data_base as db
import customtkinter as ctk


libro = 0

def mostrar_libros(frame,controller):

    def mostrar_anterior():
        global libro
        contador=10
        while libro%5!=0:
            libro-=1
            contador-=1
        if contador!=10:
            libro-=5
        else:
            libro-=10
        if libro<5:
            controller.borrar_widget(controles)
        mostrar_siguiente()

    controller.libros=db.get_libros()

    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=2)
    frame.rowconfigure(2, weight=1)

    contenedor = ctk.CTkFrame(frame,fg_color="transparent")
    contenedor.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    contenedor.columnconfigure(0, weight=1)
    for i in range(5):
        contenedor.rowconfigure(i, weight=1)

    controles = ctk.CTkFrame(frame,fg_color="transparent")
    controles.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
    controles.columnconfigure(0, weight=1)
    controles.columnconfigure(1, weight=1)
    controles.columnconfigure(2, weight=1)


    busqueda_y_carga = ctk.CTkFrame(frame,fg_color="transparent")
    busqueda_y_carga.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
    busqueda_y_carga.columnconfigure(1, weight=1)
    busqueda_y_carga.columnconfigure(2, weight=1)
    busqueda_y_carga.columnconfigure(2, weight=1)


    def mostrar_siguiente():
        global libro
        posicion=0
        controller.borrar_widget(contenedor)


        while posicion!=5 and libro<len(controller.libros):
            libro_actual = controller.libros[libro]
            lbl_libros = ctk.CTkLabel(
                contenedor,
                text=f"📖 TITULO: {libro_actual['titulo']}\t\t| CODIGO: {libro_actual['codigo']}\t| AUTOR: {libro_actual['autor']}",
                text_color="#333333",
                fg_color="#F5EBE0",
                corner_radius=8,
                padx=10,
                pady=5
            )
            lbl_libros.grid(row=posicion, column=0,columnspan=3, padx=5, pady=5, sticky="nsew")
            libro+=1
            posicion+=1

        btn_siguiente = ctk.CTkButton(
            controles,
            text="siguiente",
            corner_radius=8,
            command=mostrar_siguiente
        )
        btn_siguiente.grid(row=0, column=2, padx=5, pady=5,sticky="nsew")
        if libro > len(controller.libros) - 1:
            controller.borrar_widget(controles)
            libro = libro-posicion
        if libro > 5:
            btn_anterior = ctk.CTkButton(
                controles,
                text="anterior",
                corner_radius=8,
                command=mostrar_anterior
            )
            btn_anterior.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")


    mostrar_siguiente()




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

    controller.borrar_widget(busqueda_y_carga)

    txt_buscar_titulo = ctk.CTkEntry(busqueda_y_carga, placeholder_text="buscar libro por titulo...")
    txt_buscar_titulo.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="ew")


    txt_buscar_codigo = ctk.CTkEntry(busqueda_y_carga, placeholder_text="buscar libro por codigo...")
    txt_buscar_codigo.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

    txt_buscar_autor = ctk.CTkEntry(busqueda_y_carga, placeholder_text="buscar libro por autor...")
    txt_buscar_autor.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

    btn_buscar_titulo = ctk.CTkButton(busqueda_y_carga, text="buscar", command=buscar_titulo)
    btn_buscar_titulo.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    btn_buscar_codigo = ctk.CTkButton(busqueda_y_carga, text="buscar", command=buscar_codigo)
    btn_buscar_codigo.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

    btn_buscar_autor = ctk.CTkButton(busqueda_y_carga, text="buscar", command=buscar_autor)
    btn_buscar_autor.grid(row=3, column=3, padx=5, pady=5, sticky="ew")





