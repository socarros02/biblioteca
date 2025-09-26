import customtkinter as ctk
from carpeta_libros import libros as lib
from estanterias import interfaz_estanteria as iu_estanteria
from estanterias import mostrar_estanteria as m_estanteria
from estanterias import nueva_estanteria as n_estanteria
from estanterias import editar_estanteria as e_estanteria
from data_base import data_base as db
import carpeta_libros.mostrar_libro as p_libro
import carpeta_libros.libros_x_autor as a_libro
import os
from PIL import Image, ImageTk
theme_path = os.path.join(os.path.dirname(__file__), "themes", "coffee.json")

imagen = Image.open("C:/Users/Amadeo/PycharmProjects/biblioteca/themes/biblioteca.jpg")
imagen = imagen.resize((200, 500))



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
                  VentanaEditarEstanteria]

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
        frame.tkraise()

    def borrar_widget(self,nombre):
        for widget in nombre.winfo_children():
            widget.destroy()


class VentanaPrincipal(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        content = ctk.CTkFrame(self)
        content.pack(expand=True,fill="both")
        ctk_imagen = ctk.CTkImage(light_image=imagen, dark_image=imagen, size=(300, 500))
        lbl_imagen = ctk.CTkLabel(content, image=ctk_imagen)
        lbl_imagen.pack(side="left")

        titulo = ctk.CTkLabel(content, text="Biblioteca 🏫", font=("Arial", 45, "bold"))
        titulo.pack(pady=20)

        boton_estanterias = ctk.CTkButton(
            content, text="Estanterías 🗄️",font=("Arial", 25, "bold"),
            command=lambda: controller.mostrar_frame("VentanaEstanterias"),width=250
        )
        boton_estanterias.pack(pady=10,padx=10)

        boton_libros = ctk.CTkButton(
            content, text="Libros 📚",font=("Arial", 25, "bold"),
            command=lambda: controller.mostrar_frame("VentanaLibros"),width=250
        )
        boton_libros.pack(pady=10,padx=10)


class VentanaEstanterias(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_estanterias = ctk.CTkFrame(self)
        self.frame_estanterias.pack(fill="both", expand=True, padx=20, pady=20)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)

    def actualizarEstanteria(self):
        for widget in self.frame_estanterias.winfo_children():
            widget.destroy()
        iu_estanteria.abrir_estanteria(self.frame_estanterias, self.controller)


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
        m_estanteria.abrir_mostrar_estanteria(self.frame_estanteria, estanteria, self.controller,self)

class VentanaCrearEstanteria(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        frame_crear_estanteria = ctk.CTkFrame(self)
        frame_crear_estanteria.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)
        n_estanteria.crear_estanteria(frame_crear_estanteria,controller)

class VentanaEditarEstanteria(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        frame_editar_estanteria = ctk.CTkFrame(self)
        frame_editar_estanteria.pack(fill="both", expand=True, padx=10, pady=10)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.pack(pady=10)
        e_estanteria.editar_estanteria(frame_editar_estanteria,controller)



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

class VentanaMostrarPrestarLibros(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.frame_libros = ctk.CTkFrame(self)
        self.frame_libros.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.frame_libros.rowconfigure(0, weight=1)
        self.frame_libros.columnconfigure(0, weight=1)

        btn_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        btn_volver.grid(row=2, column=0, pady=10, sticky="ew", columnspan=3)


    def actualizarPrestamo(self):
        for widget in self.frame_libros.winfo_children():
            widget.destroy()
        libro = self.controller.libro_seleccionado
        p_libro.mostrar_prestar_libro(self.frame_libros, libro,self.controller,self)

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
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        btn_volver.grid(row=2, column=0, pady=10, sticky="ew", columnspan=3)

    def actualizarAutor(self):
        for widget in self.frame_libros_autor.winfo_children():
            widget.destroy()
        autor = self.controller.autor_seleccionado
        a_libro.mostrar_libro_autor(self.frame_libros_autor, autor, self.controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()