import customtkinter as ctk
from carpeta_libros import libros_nuevo_ejemplar as e_libro

class VentanaNuevosEjemplares(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_ejemplares = ctk.CTkFrame(self)
        self.frame_ejemplares.pack(fill="both", expand=True)



        btn_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        btn_volver.pack(fill="both", expand=True)

    def actualizarEjemplares(self):
        self.controller.borrar_widget(self.frame_ejemplares)
        e_libro.nuevos_ejemplares(self.frame_ejemplares,self.controller)