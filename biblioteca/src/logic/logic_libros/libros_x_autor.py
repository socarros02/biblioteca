import customtkinter as ctk
from customtkinter import CTkLabel
from src.data import data_base as db

ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")



def mostrar_libro(libro,controller):
    controller.libro_seleccionado= libro
    controller.mostrar_frame("VentanaMostrarPrestarLibros")

def mostrar_libro_autor(frame,autor,controller):

    controller.libros = db.get_libros()

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.pack(expand=True,fill="both")

    controles = ctk.CTkFrame(frame, corner_radius=15)
    controles.pack(expand=True,fill="x")

    scroll_frame = ctk.CTkScrollableFrame(frame)
    scroll_frame.pack(pady=20, expand=True, fill="x")




    lbl_cabecera = CTkLabel(contenedor, corner_radius=15,font=("Arial", 25),text=f"Autor: {autor}")
    lbl_cabecera.pack(pady=20, expand=True, fill="x")




    for libro in controller.libros:
        if libro['autor']==autor:
            contenedor_libro = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=10)
            contenedor_libro.pack(fill="x", pady=5, padx=10, expand=True)
            btn_libro = ctk.CTkButton(contenedor_libro,
                                      text=f"{libro['titulo']} -- codigo: {libro['codigo']} -- año de publicacion: {libro['fecha']} ",
                                      command=lambda libroX=libro: mostrar_libro(libroX, controller))
            btn_libro.pack(pady=5, expand=True, fill="x")



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


    txt_buscar_titulo = ctk.CTkEntry(controles, placeholder_text="buscar libro por titulo...")
    txt_buscar_titulo.pack(pady=5, expand=True, fill="x", side="left")


    btn_buscar_titulo = ctk.CTkButton(controles, text="buscar", command=buscar_titulo)
    btn_buscar_titulo.pack(pady=5, side="left")




