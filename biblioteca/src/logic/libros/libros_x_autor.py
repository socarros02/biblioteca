import customtkinter as ctk
from customtkinter import CTkLabel
from src.data import data_base as db

ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")


libro=0


def mostrar_libro_autor(frame,autor,controller):

    controller.libros = db.get_libros()

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    contenedor.columnconfigure(0, weight=2)
    contenedor.columnconfigure(1, weight=1)
    contenedor.columnconfigure(2, weight=1)
    contenedor.rowconfigure(0, weight=0)

    controles = ctk.CTkFrame(frame, corner_radius=15)
    controles.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    controles.columnconfigure(0, weight=1)
    controles.columnconfigure(1, weight=1)
    controles.rowconfigure(0, weight=0)
    controles.rowconfigure(1, weight=1)




    lbl_cabecera = CTkLabel(contenedor, corner_radius=15,font=("Arial", 25),text=f"Autor: {autor}")
    lbl_cabecera.grid(row=0, column=0, sticky="nsew", padx=5, pady=5,columnspan=4)

    lbl_Titulo = CTkLabel(contenedor, text="Titulo",padx=5, pady=5, text_color="#333333",fg_color="#F5EBE0")
    lbl_Titulo.grid(row=1, column=0, sticky="nsew",padx=5, pady=5)

    lbl_Codigo = CTkLabel(contenedor, text="Codigo", padx=5, pady=5, text_color="#333333",fg_color="#F5EBE0")
    lbl_Codigo.grid(row=1, column=1, sticky="nsew",padx=5, pady=5)

    lbl_Lanzamiento = CTkLabel(contenedor, text="Año de publicacion", padx=5, pady=5, text_color="#333333",fg_color="#F5EBE0")
    lbl_Lanzamiento.grid(row=1, column=2, sticky="nsew",padx=5, pady=5)

    fila = 2
    for i in controller.libros:
        if i['autor']==autor:
            lbl_titulo = ctk.CTkLabel(contenedor,text=i['titulo'])
            lbl_titulo.grid(row=fila, column=0, sticky="nsew")

            lbl_codigo = ctk.CTkLabel(contenedor, text=i['codigo'])
            lbl_codigo.grid(row=fila, column=1, sticky="nsew")

            lbl_lanazamiento = ctk.CTkLabel(contenedor, text=i['fecha'])
            lbl_lanazamiento.grid(row=fila, column=2, sticky="nsew")

            fila +=1

    def buscar_titulo():
        libro = None
        existe = -1

        titulo = txt_buscar_titulo.get()
        for i in range(len(controller.libros)):
            if titulo == controller.libros[i]['titulo']:
                libro = controller.libros[i]
                existe = i


        if existe != -1:
            controller.libro_seleccionado = libro
            controller.mostrar_frame("VentanaMostrarPrestarLibros")
        else:
            print("La estantería no existe")

    def buscar_codigo():
        libro = None
        existe = -1
        codigo = txt_buscar_codigo.get()
        for i in range(len(controller.libros)):
            if codigo == controller.libros[i]['codigo']:
                libro = controller.libros[i]
                existe = i

        if existe != -1:
            controller.libro_seleccionado = libro
            controller.mostrar_frame("VentanaMostrarPrestarLibros")
        else:
            print("La estantería no existe")




    txt_buscar_titulo = ctk.CTkEntry(controles, placeholder_text="buscar libro por titulo...")
    txt_buscar_titulo.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    txt_buscar_codigo = ctk.CTkEntry(controles, placeholder_text="buscar libro por codigo...")
    txt_buscar_codigo.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    btn_buscar_titulo = ctk.CTkButton(controles, text="buscar", command=buscar_titulo)
    btn_buscar_titulo.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

    btn_buscar_codigo = ctk.CTkButton(controles, text="buscar", command=buscar_codigo)
    btn_buscar_codigo.grid(row=2, column=3, padx=5, pady=5, sticky="ew")


