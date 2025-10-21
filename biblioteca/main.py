import os
import customtkinter as ctk
from PIL import Image
from src.data import data_base as db
from src.gui.windows.estanterias.estanterias_borrar import VentanaBorrarEstanteria
from src.gui.windows.libros.libros_borrar import VentanaBorrarLibro

from src.gui.windows.win_main import VentanaPrincipal
from src.gui.windows.estanterias.estanterias import VentanaEstanterias
from src.gui.windows.estanterias.estanterias_mostrar import VentanaMostrarEstanteria
from src.gui.windows.estanterias.estanterias_crear import VentanaCrearEstanteria
from src.gui.windows.estanterias.estanterias_editar import VentanaEditarEstanteria
from src.gui.windows.libros.libros import VentanaLibros
from src.gui.windows.libros.libros_mostrar import VentanaMostrarPrestarLibros
from src.gui.windows.libros.libros_autor import VentanaLibrosAutor
from src.gui.windows.libros.libros_nuevos_ejemplares import VentanaNuevosEjemplares
from src.gui.windows.libros.libros_editar import VentanaEditarLibros
from src.gui.windows.prestamos.prestar_libros import VentanaPrestarLibro
from src.gui.windows.prestamos.devolver_libros import VentanaDevolverLibro
from src.gui.windows.prestamos.prestar_mayor import VentanaMasPrestado
from src.gui.windows.organizador.organizar import VentanaOrganizar

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
                  VentanaOrganizar,
                  VentanaBorrarEstanteria,
                  VentanaBorrarLibro]

        for F in (frames):
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.mostrar_frame("VentanaPrincipal")

    def mostrar_frame(self, nombre):
        frame = self.frames[nombre]
        for atributo in dir(frame):
            if atributo.startswith("actualizar"):
                getattr(frame, atributo)()
                break
        frame.tkraise()

    def borrar_widget(self,nombre):
        for widget in nombre.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()