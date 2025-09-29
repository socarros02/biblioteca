import customtkinter as ctk
from carpeta_libros import libros as lib


class VentanaLibros(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.controller = controller

        lbl_header = ctk.CTkLabel(self, text="Libros 📚", font=("Arial", 28, "bold"))
        lbl_header.grid(row=0, column=0, sticky="ew",padx=5, pady=5)

        self.frame_libros = ctk.CTkFrame(self)
        self.frame_libros.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

        self.frame_libros.rowconfigure(0, weight=1)
        self.frame_libros.columnconfigure(0, weight=1)


        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal"),
            width=100
        )
        boton_volver.grid(row=2, column=0, pady=10,columnspan=3)

    def actualizarLibro(self):
        self.controller.borrar_widget(self.frame_libros)
        lib.mostrar_libros(self.frame_libros,self.controller)