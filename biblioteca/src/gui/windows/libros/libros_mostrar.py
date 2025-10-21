import customtkinter as ctk
from src.logic.logic_libros import mostrar_libro as p_libro


class VentanaMostrarPrestarLibros(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller


        self.frame_libros = ctk.CTkFrame(self,fg_color="#F5EBE0")
        self.frame_libros.pack(pady=5,expand=True,fill="x",padx=15)



        btn_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaLibros")
        )
        btn_volver.pack(pady=5,expand=True,fill="x",padx=15)


    def actualizarPrestamo(self):
        self.controller.borrar_widget(self.frame_libros)
        libro = self.controller.libro_seleccionado
        p_libro.mostrar_prestar_libro(self.frame_libros, libro,self.controller,self)