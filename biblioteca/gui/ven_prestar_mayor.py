import customtkinter as ctk
from prestamos import mostrar_mas_prestado as m



class VentanaMasPrestado(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_top_prestamos = ctk.CTkFrame(self,fg_color="transparent")
        self.frame_top_prestamos.pack(fill="both", expand=True, padx=20, pady=20)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)

    def actualizarMasPrestado(self):
        self.controller.borrar_widget(self.frame_top_prestamos)
        m.mostrar_cinco_mas_prestados(self.frame_top_prestamos,self.controller)