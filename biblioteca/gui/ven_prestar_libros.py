import customtkinter as ctk
from prestamos import prestamo_prestar as p



class VentanaPrestarLibro(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_prestar_libro = ctk.CTkFrame(self,fg_color="transparent")
        self.frame_prestar_libro.pack(fill="both", expand=True, padx=20, pady=20)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)

    def actualizarPrestarLibro(self):
        self.controller.borrar_widget(self.frame_prestar_libro)
        p.prestar_libro(self.frame_prestar_libro,self.controller)