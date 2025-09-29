import customtkinter as ctk
from data_base import data_base as db


def mostrar_cinco_mas_prestados(frame,controller):

    prestamos = db.mas_prestados()
    posicion = 0
    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.pack(fill="both", expand=True, padx=20, pady=20)
    lbl_header = ctk.CTkLabel(contenedor,text="TOP 5 LIBROS MAS PRESTADOS",font=("Arial", 35, "bold"))
    lbl_header.pack(fill="both", expand=True, padx=20, pady=20)

    for prestamo in prestamos:
        item_frame = ctk.CTkFrame(contenedor, corner_radius=12, fg_color="#F5EBE0")
        item_frame.pack(pady=8, padx=10, fill="x")
        ctk.CTkLabel(item_frame, text=f"Puesto {posicion+1} {prestamo[0]}, con un total de {prestamo[1]} ejemplares prestados").pack(padx=10, pady=2)
        posicion+=1



