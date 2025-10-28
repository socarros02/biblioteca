
import customtkinter as ctk
from src.data import data_base as db
from CTkMessagebox import CTkMessagebox
libro = 0
# Configuración inicial de apariencia
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # opciones: "blue", "green", "dark-blue"

def mostrar_libro(libro,controller):
    controller.libro_seleccionado= db.get_libro_por_titulo(libro)
    controller.mostrar_frame("VentanaMostrarPrestarLibros")

def encontrar_estanteria(id):
    estanteria=db.get_estanterias()
    for estanteria in estanteria:
        if estanteria["codigo"] == id:
            return estanteria


def abrir_mostrar_estanteria(frame,estanteria,controller):
    controller.borrar_widget(frame)
    estan=encontrar_estanteria(estanteria)

    libros = db.get_estanteria_completa(estanteria)
    frame_titulo = ctk.CTkFrame(frame)
    frame_titulo.pack(fill="x", expand=True, padx=5, pady=5)
    contenedor = ctk.CTkFrame(frame, corner_radius=15)
    contenedor.pack(fill="x", expand=True, padx=5, pady=5)
    lbl_header = ctk.CTkLabel(frame_titulo,text=f"Estanteria {estan['nombre']},codigo {estan['codigo']}",font=("Arial", 15, "bold"))
    lbl_header.pack(pady=5, expand=True, fill="x")

    for widget in contenedor.winfo_children():
        widget.destroy()

    scroll_frame = ctk.CTkScrollableFrame(contenedor,fg_color="transparent")
    scroll_frame.pack(pady=20, expand=True, fill="x")

    for libro in libros:
        libro_actual = libro

        def seleccionar_libro(titulo):
            txt_libro.delete(0, "end")
            txt_libro.insert(0, titulo)

        contenedor_libro = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=10)
        contenedor_libro.pack(fill="x", pady=5, padx=10, expand=True)
        lbl_libro = ctk.CTkButton(
            contenedor_libro,
            text=f"{libro_actual['titulo']} - cantidad de ejemplares: {libro_actual['cantidad']}",
            corner_radius=10,
            anchor="w",
            command=lambda titulo=libro_actual['titulo']: seleccionar_libro(titulo)
        )
        lbl_libro.pack(fill="x", expand=True, padx=5, pady=5)


    contenedor_prestamos = ctk.CTkFrame(frame, corner_radius=15, fg_color="#F5EBE0")
    contenedor_prestamos.pack(pady=5, expand=True, fill="x", padx=15)

    txt_libro = ctk.CTkEntry(contenedor_prestamos, corner_radius=15,placeholder_text="Libro que desea prestar, puede clickear en la lista y se auto completara el campo")
    txt_libro.pack(pady=5,expand=True,fill="x",padx=15)

    lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    txt_nombre = ctk.CTkEntry(contenedor_prestamos, corner_radius=15,placeholder_text="Prestar ejemplar, Ingrese nombre de persona que retira el ejemplar")
    txt_nombre.pack(pady=5, expand=True, fill="x", padx=15, side="left")

    def prestar_ejemplar():
        titulo = txt_libro.get()
        nombre = txt_nombre.get()
        if not nombre or not titulo:
            lbl_error.configure(text="No estan ingrsados todos los campos")
            return
        try:
            existe = db.get_libro_titulo(titulo)
            if existe == None:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Libro no encontrado")
            return
        ejemplar = db.get_id_ejemplar(existe['codigo'])
        msg = CTkMessagebox(title="Confirmar préstamo",
                            message=f"¿Deseas prestar '{titulo}' a {nombre}?",
                            icon="question",
                            option_1="Sí",
                            option_2="No",
                            master=controller)

        if msg.get() == "Sí":
            CTkMessagebox(title="Éxito",
                          message=f"Libro '{titulo}' prestado con éxito.",
                          icon="check",
                          master=controller)
            db.prestar_libro(ejemplar, nombre)
            controller.mostrar_frame("VentanaPrincipal")

    btn_prestar = ctk.CTkButton(contenedor_prestamos, corner_radius=15,command=prestar_ejemplar,text="Prestar")
    btn_prestar.pack(pady=5, expand=True, fill="x", padx=15)



