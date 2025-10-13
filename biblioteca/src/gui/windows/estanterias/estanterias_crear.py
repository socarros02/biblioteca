import customtkinter as ctk
import nueva_estanteria as n_estanteria


class VentanaCrearEstanteria(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        frame_crear_estanteria = ctk.CTkFrame(self)
        frame_crear_estanteria.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)
        n_estanteria.crear_estanteria(frame_crear_estanteria,controller)