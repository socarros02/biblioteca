import customtkinter as ctk
from estanterias import interfaz_estanteria as iu_estanteria


class VentanaEstanterias(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_estanterias = ctk.CTkFrame(self,fg_color="transparent")
        self.frame_estanterias.pack(fill="both", expand=True, padx=20, pady=20)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)

    def actualizarEstanteria(self):
        self.controller.borrar_widget(self.frame_estanterias)
        iu_estanteria.abrir_estanteria(self.frame_estanterias, self.controller)