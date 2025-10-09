import customtkinter as ctk
from carpeta_libros import libros_borrar as b_libros


class VentanaBorrarLibro(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.frame_borrar_libro = ctk.CTkFrame(self)
        self.frame_borrar_libro.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)
    def actualizarBorrarLibro(self):
        self.controller.borrar_widget(self.frame_borrar_libro)
        b_libros.borrar_libro(self.frame_borrar_libro,self.controller)
