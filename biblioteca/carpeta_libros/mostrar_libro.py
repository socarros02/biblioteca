import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkLabel
import base_datos as db
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")

def posicion_libro( ejemplar,controller,titulo):
    valor = -1
    for idx, estanteria in enumerate(controller.biblioteca):
        for i, fila in enumerate(estanteria['estanteria']):
            for j, columna in enumerate(fila):
                if columna!=0:
                    if columna['ejemplar'] == ejemplar and titulo == columna['libro']['titulo']:
                        return idx, i, j
    return -1, -1, -1



def mostrar_prestar_libro(frame,libro,controller,self):

    posicion_fila = 2

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    contenedor.columnconfigure(0, weight=2)
    contenedor.columnconfigure(1, weight=1)
    contenedor.columnconfigure(2, weight=1)
    contenedor.columnconfigure(3, weight=1)
    contenedor.rowconfigure(0, weight=0)

    controles = ctk.CTkFrame(frame, corner_radius=15)
    controles.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    controles.columnconfigure(0, weight=1)
    controles.columnconfigure(1, weight=1)
    controles.rowconfigure(0, weight=0)
    controles.rowconfigure(1, weight=1)


    titulo = libro['titulo']

    lbl_cabecera = CTkLabel(contenedor, corner_radius=15,font=("Arial", 25),text=f"Libro: {libro['titulo']}")
    lbl_cabecera.grid(row=0, column=0, sticky="nsew", padx=5, pady=5,columnspan=4)

    lbl_titulo = CTkLabel(contenedor, text="Ejemplar", corner_radius=8, padx=5, pady=5, fg_color="black",text_color="white")
    lbl_titulo.grid(row=1, column=0, sticky="nsew")

    lbl_estanteria = CTkLabel(contenedor, text="Estanteria",corner_radius=8, padx=5, pady=5, fg_color="black", text_color="white")
    lbl_estanteria.grid(row=1, column=1, columnspan=2, sticky="nsew")

    lbl_estado = CTkLabel(contenedor, text="Estado",corner_radius=8, padx=5, pady=5, fg_color="black", text_color="white")
    lbl_estado.grid(row=1, column=3, sticky="nsew")


    for estanterias in controller.biblioteca:
        codigo = estanterias['codigo']
        estanteria = estanterias['estanteria']

        for i, fila in enumerate(estanteria):
            for j, columna in enumerate(fila):
                if columna != 0:
                    if columna['libro']['titulo'] == libro['titulo']:
                        lbl_libro = CTkLabel(contenedor, text=columna['ejemplar'])
                        lbl_libro.grid(row=posicion_fila, column=0, sticky="nsew", padx=5, pady=5)

                        lbl_estanteria = CTkLabel(contenedor, text=f"codigo:{codigo} fila:{i + 1} columna:{j + 1}",corner_radius=8)
                        lbl_estanteria.grid(row=posicion_fila, column=1, sticky="nsew", columnspan=2, padx=5, pady=5)
                        if columna['disponible'] == True:
                            lbl_disponible = CTkLabel(contenedor, text="Disponible", fg_color="lightgreen",text_color="black")
                            lbl_disponible.grid(row=posicion_fila, column=3, sticky="nsew", padx=5, pady=5)
                        else:
                            lbl_disponible = CTkLabel(contenedor, text="Prestado", fg_color="red",text_color="black")
                            lbl_disponible.grid(row=posicion_fila, column=3, sticky="nsew", padx=5, pady=5)
                        posicion_fila += 1

    txt_ejemplar_prestamo = ctk.CTkEntry(controles, placeholder_text="Ingrese el ejemplar que se va a prestar....")
    txt_ejemplar_prestamo.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    txt_ejemplar_devolucion = ctk.CTkEntry(controles, placeholder_text="Ingrese el ejemplar que se va a devolver....")
    txt_ejemplar_devolucion.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    def elegir_ejemplar(valor):
        if valor==0:
            ejemplar = int(txt_ejemplar_prestamo.get())
            estanteria,fila,columna = posicion_libro(ejemplar,controller,titulo)
        else:
            ejemplar = int(txt_ejemplar_devolucion.get())
            estanteria, fila, columna = posicion_libro(ejemplar, controller, titulo)

        if estanteria != -1:
            if valor == 0:
                controller.biblioteca[estanteria]['estanteria'][fila][columna]['disponible'] = False
            else:
                controller.biblioteca[estanteria]['estanteria'][fila][columna]['disponible'] = True

            self.actualizarPrestamo()
        else:
            print("La estantería no existe")

    btn_ver_prestamo = ctk.CTkButton(controles, text="Ver", command=lambda :elegir_ejemplar(0))
    btn_ver_prestamo.grid(row=1, column=2, padx=5, pady=5)
    btn_ver_devolucion = ctk.CTkButton(controles, text="Ver", command=lambda: elegir_ejemplar(1))
    btn_ver_devolucion.grid(row=2, column=2, padx=5, pady=5)