import customtkinter as ctk
from data_base import data_base as db

def prestar_libro(frame,controller):

    contenedor = ctk.CTkFrame(frame,corner_radius=15)
    contenedor.pack(fill="both", expand=True, padx=20, pady=20)



    def prestar_titulo():
        controller.borrar_widget(frame)

        contenedor_prestamos = ctk.CTkFrame(frame, corner_radius=15, fg_color="#F5EBE0")
        contenedor_prestamos.pack(pady=5, expand=True, fill="x", padx=15)

        lbl_titulo = ctk.CTkLabel(contenedor_prestamos, text="PRESTANDO LIBRO POR TITULO", font=("Arial", 25, "bold"))
        lbl_titulo.pack(pady=5, expand=True, fill="x", padx=15)

        txt_libro = ctk.CTkEntry(contenedor_prestamos, corner_radius=15, placeholder_text="Libro que desea prestar")
        txt_libro.pack(pady=5, expand=True, fill="x", padx=15)

        lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
        lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

        txt_nombre = ctk.CTkEntry(contenedor_prestamos, corner_radius=15,placeholder_text="Ingrese nombre de persona que retira el ejemplar")
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
            if ejemplar == None:
                lbl_error.configure(text="No hay ejemplares disponibles")
                return
            db.prestar_libro(ejemplar, nombre)
            controller.mostrar_frame("VentanaPrincipal")

        btn_prestar = ctk.CTkButton(contenedor_prestamos, corner_radius=15, command=prestar_ejemplar,text="Prestar")
        btn_prestar.pack(pady=5, expand=True, fill="x", padx=15)
    def prestar_codigo():
        controller.borrar_widget(frame)
        contenedor_prestamos = ctk.CTkFrame(frame, corner_radius=15, fg_color="#F5EBE0")
        contenedor_prestamos.pack(pady=5, expand=True, fill="x", padx=15)

        lbl_titulo = ctk.CTkLabel(contenedor_prestamos, text="PRESTANDO LIBRO POR CODIGO",font=("Arial", 25, "bold"))
        lbl_titulo.pack(pady=5, expand=True, fill="x", padx=15)

        txt_libro = ctk.CTkEntry(contenedor_prestamos, corner_radius=15, placeholder_text="Libro que desea prestar")
        txt_libro.pack(pady=5, expand=True, fill="x", padx=15)


        txt_nombre = ctk.CTkEntry(contenedor_prestamos, corner_radius=15,placeholder_text="Prestar ejemplar, Ingrese nombre de persona que retira el ejemplar")
        txt_nombre.pack(pady=5, expand=True, fill="x", padx=15, side="left")

        lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
        lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

        def prestar_ejemplar():

            isbn = txt_libro.get()
            nombre = txt_nombre.get()
            if not nombre and not isbn:
                lbl_error.configure(text="Ingrese datos validos")
                return
            ejemplar = db.get_id_ejemplar(isbn)
            if ejemplar == None:
                lbl_error.configure(text="No hay ejemplares disponibles")
                return

            db.prestar_libro(ejemplar, nombre)
            controller.mostrar_frame("VentanaPrincipal")

        btn_prestar = ctk.CTkButton(contenedor_prestamos, corner_radius=15,command=prestar_ejemplar,text="Prestar")
        btn_prestar.pack(pady=5, expand=True, fill="x", padx=15)


    btn_titulo = ctk.CTkButton(contenedor,text="Elegir libro por titulo",command=prestar_titulo)
    btn_titulo.pack(fill="both", expand=True, padx=20, pady=20)

    btn_isbn = ctk.CTkButton(contenedor,text="Elegir libro por ISBN", command=prestar_codigo)
    btn_isbn.pack(fill="both", expand=True, padx=20, pady=20)
