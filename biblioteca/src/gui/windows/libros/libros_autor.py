import customtkinter as ctk
from libros import libros_x_autor as a_libro


class VentanaLibrosAutor(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.frame_libros_autor = ctk.CTkFrame(self)
        self.frame_libros_autor.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.frame_libros_autor.rowconfigure(0, weight=1)
        self.frame_libros_autor.columnconfigure(0, weight=1)

        btn_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaLibros")
        )
        btn_volver.grid(row=2, column=0, pady=10, sticky="ew", columnspan=3)

    def actualizarAutor(self):
        for widget in self.frame_libros_autor.winfo_children():
            widget.destroy()
        autor = self.controller.autor_seleccionado
        a_libro.mostrar_libro_autor(self.frame_libros_autor, autor, self.controller)