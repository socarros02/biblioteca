import tkinter as tk
import customtkinter as ctk

from carpeta_libros.libros_nuevo_ejemplar import cantidad_ejemplares
from data_base import data_base as db
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")



def mostrar_prestar_libro(frame,libro,controller,self):

    ejemplares = db.get_ejemplares_especificos(libro['codigo'])

    print(ejemplares)
    cantidad =0
    estanteria = "Todos los ejemplares estan prestados"
    if ejemplares != None:
        cantidad = ejemplares[0]['cantidad']
        estanteria = ejemplares[0]['estanteria']


    contenedor = ctk.CTkFrame(frame, corner_radius=15,fg_color="#F5EBE0")
    contenedor.pack(pady=5,expand=True,fill="x",padx=15)





    lbl_cabecera = ctk.CTkLabel(contenedor, corner_radius=15,font=("Arial", 25),text=f"Libro: {libro['titulo']}",text_color="#333333")
    lbl_cabecera.pack(pady=5,expand=True,fill="x",padx=15)

    lbl_titulo = ctk.CTkLabel(contenedor, text="Cantidad de Ejemplares disponibles", corner_radius=8, padx=5, pady=5, fg_color="black",text_color="white")
    lbl_titulo.pack(pady=5,expand=True,fill="x",padx=15)
    lbl_cantindad = ctk.CTkLabel(contenedor,text=f"{cantidad}")
    lbl_cantindad.pack(pady=5,expand=True,fill="x",padx=15)


    lbl_estanteria = ctk.CTkLabel(contenedor, text="Estanteria",corner_radius=8, padx=5, pady=5, fg_color="black", text_color="white")
    lbl_estanteria.pack(pady=5,expand=True,fill="x",padx=15)
    lbl_estanteria_id = ctk.CTkLabel(contenedor, text=f"{estanteria}")
    lbl_estanteria_id.pack(pady=5, expand=True, fill="x", padx=15)

    if cantidad != 0:

        contenedor_prestamos= ctk.CTkFrame(frame, corner_radius=15,fg_color="#F5EBE0")
        contenedor_prestamos.pack(pady=5,expand=True,fill="x",padx=15)

        lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
        lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

        txt_nombre = ctk.CTkEntry(contenedor_prestamos, corner_radius=15, placeholder_text="Prestar ejemplar, Ingrese nombre de persona que retira el ejemplar")
        txt_nombre.pack(pady=5,expand=True,fill="x",padx=15,side="left")

        def prestar_ejemplar():
            ejemplar = db.get_id_ejemplar(libro['codigo'])
            nombre = txt_nombre.get()
            if not nombre:
                lbl_error.configure(text="Ingrese datos validos")
                return
            db.prestar_libro(ejemplar,nombre)
            controller.mostrar_frame("VentanaPrincipal")



        btn_prestar = ctk.CTkButton(contenedor_prestamos, corner_radius=15,command=prestar_ejemplar,text="Prestar")
        btn_prestar.pack(pady=5,expand=True,fill="x",padx=15)







