import customtkinter as ctk
import borrar_estanteria as b_estanteria


class VentanaBorrarEstanteria(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.frame_borrar_estanteria = ctk.CTkFrame(self)
        self.frame_borrar_estanteria.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)
    def actualizarBorrarEstanteria(self):
        self.controller.borrar_widget(self.frame_borrar_estanteria)
        b_estanteria.borrar_estanteria(self.frame_borrar_estanteria,self.controller)
