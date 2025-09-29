import customtkinter as ctk
from estanterias import  editar_estanteria as e_estanteria


class VentanaEditarEstanteria(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        frame_editar_estanteria = ctk.CTkFrame(self)
        frame_editar_estanteria.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)
        e_estanteria.editar_estanteria(frame_editar_estanteria,controller)