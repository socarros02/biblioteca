from pickle import GLOBAL

import numpy as np
import customtkinter as ctk
from data_base import data_base as db
libro = 0
# Configuración inicial de apariencia
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # opciones: "blue", "green", "dark-blue"






def abrir_mostrar_estanteria(frame,estanteria,controller,self):
    for widget in frame.winfo_children():
        widget.destroy()
    global libro
    libro = 0
    libros = db.get_estanteria_completa(estanteria)

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.grid(row=0, column=0, sticky="nsew", padx=5, pady=20)

    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    contenedor.columnconfigure(0, weight=1)
    for i in range(5):
        contenedor.rowconfigure(i, weight=1)



    if len(libros)>5:
        controles= ctk.CTkFrame(frame, corner_radius=15)
        controles.grid(row=1, column=0, sticky="nsew", padx=5, pady=20)
        controles.rowconfigure(1, weight=1)
        controles.columnconfigure(0, weight=1)
        controles.columnconfigure(1, weight=1)
        controles.columnconfigure(2, weight=1)
        controles.columnconfigure(3, weight=1)


    busqueda = ctk.CTkFrame(frame, corner_radius=15)
    busqueda.grid(row=2, column=0, sticky="nsew", padx=5, pady=20)
    busqueda.rowconfigure(2, weight=1)
    busqueda.columnconfigure(0, weight=3)
    busqueda.columnconfigure(1, weight=1)


    def prestar():
        abrir_mostrar_estanteria(frame, estanteria, controller, self)

    btn_prestar_libro = ctk.CTkButton(busqueda, text="Prestar", command=lambda: prestar())
    btn_prestar_libro.grid(row=1, column=1, padx=5, pady=5,sticky="nsew")


    def mostrar_siguiente():
        global libro
        posicion=0

        for widget in contenedor.winfo_children():
            widget.destroy()

        while posicion!=5 and libro<len(libros):
            libro_actual = libros[libro]


            lbl_libro = ctk.CTkLabel(
                contenedor,
                text=f"{libro_actual['titulo']} - ejemplar:{libro_actual['ejemplar']}",
                corner_radius=10,
                fg_color="lightblue",
                text_color="black",
                anchor="center"
            )
            lbl_libro.grid(row=posicion, column=0, padx=5, pady=5, sticky="nsew")


            libro+=1
            posicion+=1
        if len(libros)>5:
            btn_siguiente = ctk.CTkButton(
                controles,
                text="siguiente",
                fg_color="white",
                text_color="black",
                corner_radius=8,
                command=mostrar_siguiente
            )
            btn_siguiente.grid(row=0, column=3, padx=5, pady=5,sticky="nsew")
            if libro > len(libros) - 1:
                for widget in controles.winfo_children():
                    widget.destroy()
            if libro > 5:
                btn_anterior = ctk.CTkButton(
                    controles,
                    text="anterior",
                    fg_color="white",
                    text_color="black",
                    corner_radius=8,
                    command=mostrar_anterior
                )
                btn_anterior.grid(row=0, column=0, padx=5, pady=5,sticky="nsew")


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
            for widget in controles.winfo_children():
                widget.destroy()
        mostrar_siguiente()

    mostrar_siguiente()

