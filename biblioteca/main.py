import os
import customtkinter as ctk
from PIL import Image
from data_base import data_base as db


from gui.ven_principal import VentanaPrincipal
from gui.ven_estanterias import VentanaEstanterias
from gui.ven_estanterias_mostrar import VentanaMostrarEstanteria
from gui.ven_estanterias_crear import VentanaCrearEstanteria
from gui.ven_estanterias_editar import VentanaEditarEstanteria
from gui.ven_libros import VentanaLibros
from gui.ven_libros_mostrar import VentanaMostrarPrestarLibros
from gui.ven_libros_autor import VentanaLibrosAutor
from gui.ven_libros_nuevos_ejemplares import VentanaNuevosEjemplares
from gui.ven_libros_editar import VentanaEditarLibros
from gui.ven_prestar_libros import VentanaPrestarLibro
from gui.ven_devolver_libros import VentanaDevolverLibro
from gui.ven_prestar_mayor import VentanaMasPrestado
from gui.ven_organizar import VentanaOrganizar

theme_path = os.path.join(os.path.dirname(__file__), "themes", "coffee.json")
imagen = Image.open("themes/biblioteca.jpg")



class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.biblioteca = db.get_estanterias()
        self.libros = db.get_libros()
        self.estanteria_actual = None
        self.libro_seleccionado =None
        self.autor_seleccionado =None

        self.geometry("700x500")
        self.title("Biblioteca")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme(theme_path)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames = {}

        frames = [VentanaPrincipal,
                  VentanaEstanterias,
                  VentanaLibros,
                  VentanaMostrarEstanteria,
                  VentanaCrearEstanteria,
                  VentanaMostrarPrestarLibros,
                  VentanaLibrosAutor,
                  VentanaEditarEstanteria,
                  VentanaNuevosEjemplares,
                  VentanaEditarLibros,
                  VentanaPrestarLibro,
                  VentanaDevolverLibro,
                  VentanaMasPrestado,
                  VentanaOrganizar]

        for F in (frames):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.mostrar_frame("VentanaPrincipal")

    def mostrar_frame(self, nombre):
        frame = self.frames[nombre]
        if nombre == "VentanaMostrarEstanteria":
            frame.actualizarMostrarEstanteria()
        elif nombre == "VentanaMostrarPrestarLibros":
            frame.actualizarPrestamo()
        elif nombre == "VentanaEstanterias":
            frame.actualizarEstanteria()
        elif nombre == "VentanaLibrosAutor":
            frame.actualizarAutor()
        elif nombre == "VentanaLibros":
            frame.actualizarLibro()
        elif nombre == "VentanaNuevosEjemplares":
            frame.actualizarEjemplares()
        elif nombre == "VentanaEditarLibros":
            frame.actualizarEditarLibro()
        elif nombre == "VentanaPrestarLibro":
            frame.actualizarPrestarLibro()
        elif nombre == "VentanaDevolverLibro":
            frame.actualizarDevolverLibro()
        elif nombre == "VentanaMasPrestado":
            frame.actualizarMasPrestado()
        elif nombre == "VentanaOrganizar":
            frame.actualizarOrganizar()
        frame.tkraise()

    def borrar_widget(self,nombre):
        for widget in nombre.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()