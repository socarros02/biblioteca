import customtkinter as ctk
from organizador import editar_posiciones as e



class VentanaOrganizar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_organizar = ctk.CTkFrame(self,fg_color="transparent")
        self.frame_organizar.pack(fill="both", expand=True, padx=20, pady=20)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)

    def actualizarOrganizar(self):
        self.controller.borrar_widget(self.frame_organizar)
        e.cambiar_estanterias(self.frame_organizar,self.controller)