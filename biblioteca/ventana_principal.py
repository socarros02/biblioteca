import customtkinter as ctk
from estanterias import interfaz_estanteria as iu_estanteria


# Configuración de apariencia
ctk.set_appearance_mode("dark")   # opciones: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


def ventana_princial(ventana):
    if ventana != 1:
        ventana.destroy()

    ventana = ctk.CTk()
    ventana.geometry("700x700")
    ventana.title("Biblioteca")

    ventana.grid_rowconfigure(0, weight=1)   # fila del título
    ventana.grid_rowconfigure(1, weight=3)   # fila de los botones
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_columnconfigure(2, weight=1)

    # Título principal
    titulo = ctk.CTkLabel(
        ventana,
        text="Biblioteca",
        fg_color="lightblue",
        text_color="black",
        corner_radius=10,
        font=("Arial", 28, "bold"),
        padx=10,
        pady=10
    )
    titulo.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=20)

    # Botones principales
    boton_estanterias = ctk.CTkButton(
        ventana,
        text="Estanterías",
        command=lambda: iu_estanteria.abrir_estanteria(1),
        height=60,
        width=150,
        corner_radius=12
    )

    boton_libros = ctk.CTkButton(
        ventana,
        text="Libros",
        height=60,
        width=150,
        corner_radius=12
    )

    boton_autores = ctk.CTkButton(
        ventana,
        text="Autores",
        height=60,
        width=150,
        corner_radius=12
    )

    # Ubicación en grid
    boton_estanterias.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
    boton_libros.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    boton_autores.grid(row=1, column=2, sticky="nsew", padx=20, pady=20)

    ventana.mainloop()
