import customtkinter as ctk
import os
from PIL import Image
theme_path = os.path.join(os.path.dirname(__file__), "themes", "coffee.json")
imagen = Image.open("themes/biblioteca.jpg")
class VentanaPrincipal(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        content = ctk.CTkFrame(self)
        content.pack(expand=True,fill="both")
        ctk_imagen = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(300, 500))
        lbl_imagen = ctk.CTkLabel(content, image=ctk_imagen,text="")
        lbl_imagen.pack(side="left")

        titulo = ctk.CTkLabel(content, text="Biblioteca 🏫", font=("Arial", 45, "bold"))
        titulo.pack(pady=20)
        def mostrar_eleccion_estanteria(choice):
            if choice == "Ver Estanterias":
                controller.mostrar_frame("VentanaEstanterias")
            elif choice == "Editar Estanterias":
                controller.mostrar_frame("VentanaEditarEstanteria")
            elif choice == "Nueva estanteria":
                controller.mostrar_frame("VentanaCrearEstanteria")
            elif choice == "Borrar Estanteria":
                controller.mostrar_frame("VentanaBorrarEstanteria")

        opciones_estanterias=[
            "Ver Estanterias","Editar Estanterias","Nueva estanteria","Borrar Estanteria"
        ]
        estanterias = ctk.CTkOptionMenu(content, values=opciones_estanterias, command=mostrar_eleccion_estanteria,width=250)
        estanterias.pack(pady=20)

        estanterias.set("Estanterias")

        def mostrar_eleccion_libros(choice):
            if choice == "Ver Libros":
                controller.mostrar_frame("VentanaLibros")
            elif choice == "Editar Libros":
                controller.mostrar_frame("VentanaEditarLibros")
            elif choice == "Nuevos Ejemplares":
                controller.mostrar_frame("VentanaNuevosEjemplares")
            elif choice == "Borrar Libro":
                controller.mostrar_frame("VentanaBorrarLibro")


        opciones_libro=[
            "Ver Libros","Editar Libros","Nuevos Ejemplares","Borrar Libro"
        ]
        libros = ctk.CTkOptionMenu(content, values=opciones_libro, command=mostrar_eleccion_libros,width=250)
        libros.pack(pady=20)


        libros.set("Libros")

        def mostrar_eleccion_prestamos(choice):
            if choice == "Nuevo Prestamos":
                controller.mostrar_frame("VentanaLibros")
            elif choice == "Devolver Libro":
                controller.mostrar_frame("VentanaDevolverLibro")
            elif choice == "Libros mas prestados":
                controller.mostrar_frame("VentanaMasPrestado")

        opciones_prestamos=[
            "Nuevo Prestamos","Devolver Libro","Libros mas prestados"
        ]
        prestamos = ctk.CTkOptionMenu(content, values=opciones_prestamos, command=mostrar_eleccion_prestamos,width=250)
        prestamos.pack(pady=20)


        prestamos.set("Prestamos")

        btn_organizar= ctk.CTkButton(content, text="Cambiar ejemplares de estanteria", command=lambda: controller.mostrar_frame("VentanaOrganizar"))

        btn_organizar.pack(pady=20)


