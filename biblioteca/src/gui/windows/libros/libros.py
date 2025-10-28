import customtkinter as ctk
from src.logic.logic_libros import libros as lib
from src.data import data_base as db



class VentanaLibros(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)



        self.controller = controller

        lbl_header = ctk.CTkLabel(self, text="Libros 📚", font=("Arial", 28, "bold"))
        lbl_header.pack(padx=5, pady=5)

        self.frame_libros = ctk.CTkFrame(self)
        self.frame_libros.pack(padx=5, pady=5,expand=True,fill="both")

        def accion_volver():
            controller.libros=db.get_libros()
            controller.mostrar_frame("VentanaPrincipal")

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: accion_volver(),
            width=100
        )
        boton_volver.pack(padx=5, pady=5)

    def actualizarLibro(self):

        self.controller.borrar_widget(self.frame_libros)
        lib.mostrar_libros(self.frame_libros,self.controller)
