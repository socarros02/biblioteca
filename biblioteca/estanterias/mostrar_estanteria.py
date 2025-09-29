
import customtkinter as ctk
from data_base import data_base as db
libro = 0
# Configuración inicial de apariencia
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # opciones: "blue", "green", "dark-blue"






def abrir_mostrar_estanteria(frame,estanteria,controller):
    controller.borrar_widget(frame)

    global libro
    libro = 0
    libros = db.get_estanteria_completa(estanteria)

    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.pack(fill="x", expand=True, padx=5, pady=5)

    if len(libros)>5:
        controles= ctk.CTkFrame(frame, corner_radius=15)
        controles.pack(fill="x", expand=True, padx=5, pady=5)


    def mostrar_siguiente():
        global libro
        posicion=0

        for widget in contenedor.winfo_children():
            widget.destroy()

        while posicion!=5 and libro<len(libros):
            libro_actual = libros[libro]


            lbl_libro = ctk.CTkLabel(
                contenedor,
                text=f"{libro_actual['titulo']} - cantidad de ejemplares: {libro_actual['cantidad']}",
                corner_radius=10,
                text_color="#333333",
                fg_color="#F5EBE0",
                anchor="center"
            )
            lbl_libro.pack(fill="x", expand=True, padx=5, pady=5)


            libro+=1
            posicion+=1
        if len(libros)>5:
            btn_siguiente = ctk.CTkButton(
                controles,
                text="siguiente",
                corner_radius=8,
                command=mostrar_siguiente
            )
            btn_siguiente.pack( padx=5, pady=5,side="right")
            if libro > len(libros) - 1:
                controller.borrar_widget(controles)
            if libro > 5:
                btn_anterior = ctk.CTkButton(
                    controles,
                    text="anterior",
                    corner_radius=8,
                    command=mostrar_anterior
                )
                btn_anterior.pack( padx=5, pady=5,side="left")


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

    contenedor_prestamos = ctk.CTkFrame(frame, corner_radius=15, fg_color="#F5EBE0")
    contenedor_prestamos.pack(pady=5, expand=True, fill="x", padx=15)

    txt_libro = ctk.CTkEntry(contenedor_prestamos, corner_radius=15,placeholder_text="Libro que desea prestar")
    txt_libro.pack(pady=5,expand=True,fill="x",padx=15)

    lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    txt_nombre = ctk.CTkEntry(contenedor_prestamos, corner_radius=15,placeholder_text="Prestar ejemplar, Ingrese nombre de persona que retira el ejemplar")
    txt_nombre.pack(pady=5, expand=True, fill="x", padx=15, side="left")

    def prestar_ejemplar():
        titulo = txt_libro.get()
        nombre = txt_nombre.get()
        if not nombre and not titulo:
            lbl_error.configure(text="Ingrese datos validos")
            return
        try:
            existe = db.get_libro_por_titulo(titulo)
            if existe == None:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Estanteria no encontrada")
            return
        ejemplar = db.get_id_ejemplar(existe['codigo'])
        db.prestar_libro(ejemplar, nombre)
        controller.mostrar_frame("VentanaPrincipal")

    btn_prestar = ctk.CTkButton(contenedor_prestamos, corner_radius=15,command=prestar_ejemplar)
    btn_prestar.pack(pady=5, expand=True, fill="x", padx=15)

    mostrar_siguiente()

