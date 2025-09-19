import customtkinter as ctk
from carpeta_libros import libros as lib
import base_datos
from estanterias import interfaz_estanteria as iu_estanteria
from estanterias import mostrar_estanteria as m_estanteria
import base_datos as db
from estanterias import nueva_estanteria as n_estanteria
import carpeta_libros.mostrar_libro as p_libro
import carpeta_libros.libros_x_autor as a_libro

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.biblioteca = db.biblioteca
        self.libros = db.libros
        self.estanteria_actual = db.biblioteca[0]['estanteria']
        self.libro_seleccionado = db.libros[0]
        self.autor_seleccionado = db.libros[0]['autor']

        self.geometry("700x700")
        self.title("Biblioteca")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.container.columnconfigure(0, weight=1)
        self.frames = {}

        frames = [VentanaPrincipal, VentanaEstanterias, VentanaLibros,VentanaMostrarEstanteria,VentanaCrearEstanteria,VentanaMostrarPrestarLibros,VentanaLibrosAutor]

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
        frame.tkraise()


class VentanaPrincipal(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        titulo = ctk.CTkLabel(self, text="Biblioteca", font=("Arial", 28, "bold"))
        titulo.pack(pady=20)

        boton_estanterias = ctk.CTkButton(
            self, text="Estanterías",
            command=lambda: controller.mostrar_frame("VentanaEstanterias")
        )
        boton_estanterias.pack(pady=10)

        boton_libros = ctk.CTkButton(
            self, text="Libros",
            command=lambda: controller.mostrar_frame("VentanaLibros")
        )
        boton_libros.pack(pady=10)


class VentanaEstanterias(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.frame_estanterias = ctk.CTkFrame(self)
        self.frame_estanterias.pack(fill="both", expand=True, padx=20, pady=20)
        self.frame_estanterias.columnconfigure(0, weight=1)

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
        self.frame_estanteria.pack(fill="both", expand=True, padx=20, pady=20)


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
        frame_crear_estanteria.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.grid(row=2, column=0, pady=10, sticky="ew", columnspan=3)
        n_estanteria.crear_estanteria(frame_crear_estanteria,controller,self.controller.biblioteca)



class VentanaLibros(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)


        frame_libros = ctk.CTkFrame(self)
        frame_libros.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


        frame_libros.rowconfigure(0, weight=1)
        frame_libros.columnconfigure(0, weight=1)


        lib.mostrar_libros(frame_libros,controller)

        boton_volver = ctk.CTkButton(
            self, text="Volver",
            command=lambda: controller.mostrar_frame("VentanaPrincipal")
        )
        boton_volver.grid(row=2, column=0, pady=10, sticky="ew",columnspan=3)

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