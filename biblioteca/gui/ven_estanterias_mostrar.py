import customtkinter as ctk
from estanterias import mostrar_estanteria as m_estanteria

class VentanaMostrarEstanteria(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.frame_estanteria = ctk.CTkFrame(self)
        self.frame_estanteria.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)

    def actualizarMostrarEstanteria(self):
        for widget in self.frame_estanteria.winfo_children():
            widget.destroy()
        estanteria = self.controller.estanteria_actual
        m_estanteria.abrir_mostrar_estanteria(self.frame_estanteria, estanteria, self.controller)