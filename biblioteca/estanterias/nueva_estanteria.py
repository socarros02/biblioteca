import numpy as np
import customtkinter as ctk
from data_base import data_base as db

# Configuración de apariencia
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"




def crear_estanteria(frame,controller):

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    lbl_header = ctk.CTkLabel(frame,text="Nueva Estanteria",fg_color="transparent",font=("Ariel",50,"bold"))
    lbl_header.grid(row=0, column=0, sticky="nsew")



    contenedor = ctk.CTkFrame(frame,fg_color="transparent")
    contenedor.grid(row=1, column=0, sticky="nsew")

    contenedor.columnconfigure(0, weight=1)


    txt_nombre_estanteria = ctk.CTkEntry(contenedor, placeholder_text="Ingresar nombre de estaneria nueva.....")
    txt_nombre_estanteria.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    txt_capacidad_maxima = ctk.CTkEntry(contenedor, placeholder_text="Ingresar capacidad, maximo 150 libros.....")
    txt_capacidad_maxima.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    lbl_error = ctk.CTkLabel(contenedor, text="", text_color="red")
    lbl_error.grid(row=2, column=0, pady=5, sticky="ew")

    def validar_ingreso():
        nombre = txt_nombre_estanteria.get()
        capacidad_maxima = txt_capacidad_maxima.get()
        if not nombre or not capacidad_maxima:
            lbl_error.configure(text="Error: complete todos los campos")
            return

        try:
            capacidad = int(capacidad_maxima)
            if capacidad <= 0 or capacidad > 150:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Error: complete todos los campos")
            return

        db.nueva_estanteria(nombre, capacidad)
        controller.mostrar_frame("VentanaPrincipal")

    btn_crear_estanteria = ctk.CTkButton(contenedor, text="crear", command=validar_ingreso,width=200)
    btn_crear_estanteria.grid(row=3, column=0, padx=5, pady=5)


