import numpy as np
import customtkinter as ctk
import interfaz_estanteria as iu_estanteria
import base_datos as db

# Configuración de apariencia
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"




def crear_estanteria(frame,controller,biblioteca):

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    lbl_titulo = ctk.CTkLabel(
        contenedor,
        text="Ingrese la nueva estantería (máximo 10x10)",
        fg_color="blue",
        text_color="white",
        corner_radius=10,
        padx=10,
        pady=5
    )
    lbl_titulo.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=10)


    lbl_filas = ctk.CTkLabel(frame, text="Cantidad de filas:")
    lbl_filas.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    txt_filas = ctk.CTkEntry(frame, placeholder_text="Ej: 5")
    txt_filas.grid(row=1, column=1, padx=5, pady=5)

    lbl_columnas = ctk.CTkLabel(frame, text="Cantidad de columnas:")
    lbl_columnas.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    txt_columnas = ctk.CTkEntry(frame, placeholder_text="Ej: 7")
    txt_columnas.grid(row=2, column=1, padx=5, pady=5)


    def generar_estanteria():
        try:
            filas = int(txt_filas.get())
            columnas = int(txt_columnas.get())

            if filas <= 0 or columnas <= 0 or filas > 10 or columnas > 10:
                lbl_error = ctk.CTkLabel(
                    frame,
                    text="Número inválido. Ingrese un valor mayor a 0 y menor o igual a 10",
                    fg_color="red",
                    text_color="white",
                    corner_radius=8,
                    padx=10,
                    pady=5
                )

                lbl_error.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=5)
                return

            estanteria = np.zeros((filas, columnas), dtype=object)
            codigo_estanteria = len(biblioteca)+1

            controller.biblioteca.append({
                "codigo": codigo_estanteria,
                "estanteria": estanteria,
                "filas": filas,
                "columnas": columnas
            })
            controller.mostrar_frame("VentanaPrincipal")

        except ValueError:
            print("Debes ingresar números válidos")


    boton_crear = ctk.CTkButton(frame, text="Crear estantería", command=generar_estanteria)
    boton_crear.grid(row=3, column=0, columnspan=2, pady=15)


