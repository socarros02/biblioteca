import customtkinter as ctk
from src.logic.estanterias import editar_estanteria as e_estanteria


class VentanaEditarEstanteria(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.frame_editar_estanteria = ctk.CTkFrame(self)
        self.frame_editar_estanteria.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)


    def actualizarEditarEstanteria(self):
        for widget in self.frame_editar_estanteria.winfo_children():
            widget.destroy()
        e_estanteria.editar_estanteria(self.frame_editar_estanteria, self.controller)