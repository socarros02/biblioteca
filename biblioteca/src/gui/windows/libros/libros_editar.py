import customtkinter as ctk
from libros import libros_editar as ed_libro


class VentanaEditarLibros(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_editar_libros = ctk.CTkFrame(self)
        self.frame_editar_libros.pack(fill="both", expand=True)



        btn_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        btn_volver.pack(fill="both", expand=True)

    def actualizarEditarLibro(self):
        self.controller.borrar_widget(self.frame_editar_libros)
        ed_libro.editar_libros(self.frame_editar_libros,self.controller)