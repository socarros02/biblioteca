import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkLabel
from data_base import data_base as db
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")



def mostrar_prestar_libro(frame,libro,controller,self):

    posicion_fila = 2

    ejemplares = db.get_ejemplares_especificos(libro['codigo'])

    print("Ejemplares especificos: ",ejemplares)

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    contenedor.columnconfigure(0, weight=2)
    contenedor.columnconfigure(1, weight=1)
    contenedor.columnconfigure(2, weight=1)
    contenedor.columnconfigure(3, weight=1)
    contenedor.rowconfigure(0, weight=0)



    lbl_cabecera = CTkLabel(contenedor, corner_radius=15,font=("Arial", 25),text=f"Libro: {libro['titulo']}")
    lbl_cabecera.grid(row=0, column=0, sticky="nsew", padx=5, pady=5,columnspan=4)

    lbl_titulo = CTkLabel(contenedor, text="Ejemplar", corner_radius=8, padx=5, pady=5, fg_color="black",text_color="white")
    lbl_titulo.grid(row=1, column=0, sticky="nsew")

    lbl_estanteria = CTkLabel(contenedor, text="Estanteria",corner_radius=8, padx=5, pady=5, fg_color="black", text_color="white")
    lbl_estanteria.grid(row=1, column=1, columnspan=2, sticky="nsew")

    lbl_estado = CTkLabel(contenedor, text="Estado",corner_radius=8, padx=5, pady=5, fg_color="black", text_color="white")
    lbl_estado.grid(row=1, column=3, sticky="nsew")







