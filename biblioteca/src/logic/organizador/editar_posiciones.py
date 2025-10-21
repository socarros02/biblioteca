import customtkinter as ctk
from src.data import data_base as db
import interfaz_estanteria as iu
from CTkMessagebox import CTkMessagebox


def mostrar_estanterias_disponibles(biblioteca, frame, controller,txt):
    scroll_frame = ctk.CTkScrollableFrame(frame)
    scroll_frame.pack(expand=True, fill="x")

    controller.borrar_widget(scroll_frame)

    for estanteria in biblioteca:
        def seleccionar_estanteria(estanteria):
            txt.delete(0, "end")
            txt.insert(0, estanteria)

        fila_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent", corner_radius=5)
        fila_frame.pack(fill="x", pady=2)
        estanteria_actual = estanteria
        disponible = estanteria_actual['capacidad'] - db.contar_ejemplares_por_estanteria(
            estanteria_actual["codigo"])

        btn_ver = ctk.CTkButton(
            fila_frame,
            text=f"🗄️{estanteria_actual['nombre']}   -   código {estanteria_actual['codigo']}  -   capacidad {estanteria_actual['capacidad']}  -  espacios disponibles {disponible}",
            text_color="white",
            command=lambda estanteriaX=estanteria_actual['codigo']: seleccionar_estanteria(estanteriaX),
            width=25
        )
        btn_ver.pack(pady=5, padx=15, expand=True, fill="x")

def elegir_estanteria(frame,libro,controller):
    estanterias = db.get_estanterias()
    cantidad_ejemplares= db.cantidad_ejemplares_por_libro(libro['codigo'])

    lbl_isbn_viejo = ctk.CTkLabel(frame, text=f"El libro que quieres mover de estanteria es {libro['titulo']} \n Y tiene {cantidad_ejemplares} ejemplares a mover",font=("Arial", 15, "bold"))
    lbl_isbn_viejo.pack(pady=5, expand=True, fill="x")

    contenedor= ctk.CTkFrame(frame)
    contenedor.pack(pady=5,expand=True,fill="x",padx=15)



    lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)

    caja_texto_ingresar_codigo = ctk.CTkEntry(frame, placeholder_text="Código de estantería...")
    caja_texto_ingresar_codigo.pack(side="left", fill="x", expand=True, padx=5)

    mostrar_estanterias_disponibles(estanterias,contenedor,controller,caja_texto_ingresar_codigo)


    def confirmar_estanteria():
        codigo = caja_texto_ingresar_codigo.get()

        if not codigo:
            lbl_error.configure(text="Ingrese datos validos")
            return

        try:
            codigo = int(codigo)
            estanteria = db.get_estanteria_seleccionada(codigo)
            if estanteria == None:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Ingrese datos validos")
            return
        try:
            capacidad = db.capacidad_maxima(estanteria)
            ocupado = db.contar_ejemplares_por_estanteria(estanteria)
            if capacidad-cantidad_ejemplares-ocupado>=0:
                CTkMessagebox(title="Éxito",
                              message=f"Los ejemplares de {libro['titulo']}, se cambiaron a la estanteria codigo {estanteria}, con exito",
                              icon="check",
                              master=controller)
                db.cambiar_de_estanteria(estanteria,libro['codigo'])
                controller.mostrar_frame("VentanaPrincipal")
            else:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="La estanteria no puede soportar tantos logic_libros, \ncambie otros logic_libros de esa estanteria para poder realizar este cambio")
            return

    boton_ver_estanteria = ctk.CTkButton(frame, text="Elegir", command=confirmar_estanteria)
    boton_ver_estanteria.pack(side="left", padx=5)



def cambiar_estanterias(frame, controller):

    contenedor = ctk.CTkFrame(frame)
    contenedor.pack(fill="both", expand=True, padx=20, pady=20)

    lbl_header = ctk.CTkLabel(contenedor, text="Cambiar ejemplares de estanteria", font=("Arial",15, "bold"))
    lbl_header.pack(padx=5, pady=5)

    busqueda_frame = ctk.CTkFrame(contenedor, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)

    txt_isbn = ctk.CTkEntry(busqueda_frame, placeholder_text="Isbn del libro...")
    txt_isbn.pack(side="left", fill="x", expand=True, padx=5, pady=5)

    def elegir_libro():
        isbn = txt_isbn.get()
        libro = db.get_libro_por_codigo(isbn)

        if not libro:
            lbl_error.configure(text="Ingrese datos validos")
            return

        if libro == None:
            lbl_error.configure(text="Ingrese datos validos")
            return
        else:
            busqueda_frame.destroy()
            contenedor.destroy()
            elegir_estanteria(frame,libro,controller)


    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Elegir", command=elegir_libro)
    boton_ver_estanteria.pack(side="left", padx=5, pady=5)
    lbl_error = ctk.CTkLabel(busqueda_frame, text="", text_color="red")
    lbl_error.pack(side="bottom", fill="x", expand=True, padx=5, pady=5)