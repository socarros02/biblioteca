import customtkinter as ctk
from src.data import data_base as db
from src.gui.windows.estanterias import estanterias

est = 0

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def mostrar_estanteria(estanteria,controller):
    controller.estanteria_actual = db.get_estanteria_seleccionada(estanteria)
    controller.mostrar_frame("VentanaMostrarEstanteria")


def posicion_estanteria(estanterias, codigo):
    valor = -1
    for idx, datos in enumerate(estanterias):
        if int(codigo) == datos['codigo']:
            valor = idx
    return valor


def mostrar_estanterias_disponibles(biblioteca, frame,controller):


    scroll_frame = ctk.CTkScrollableFrame(frame)
    scroll_frame.pack(expand=True, fill="x")


    controller.borrar_widget(scroll_frame)

    for estanteria in biblioteca:


        fila_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent",corner_radius=5)
        fila_frame.pack(fill="x", pady=2)
        estanteria_actual = estanteria
        disponible =estanteria_actual['capacidad']- db.contar_ejemplares_por_estanteria(estanteria_actual["codigo"])

        btn_ver = ctk.CTkButton(
            fila_frame,
            text=f"🗄️{estanteria_actual['nombre']}   -   código {estanteria_actual['codigo']}  -   capacidad {estanteria_actual['capacidad']}  -  espacios disponibles {disponible}",
            text_color="white",
            command=lambda estanteriaX=estanteria_actual['codigo']: mostrar_estanteria(estanteriaX, controller),
            width=25
        )
        btn_ver.pack(pady=5,padx=15,expand=True,fill="x")







def abrir_estanteria(frame,controller):

    biblioteca = db.get_estanterias()


    controller.borrar_widget(frame)

    header = ctk.CTkFrame(frame, fg_color="transparent",height=10)
    header.pack( padx=5, pady=5)
    busqueda_frame = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)



    lbl_header = ctk.CTkLabel(header, text= "Estanterias",corner_radius=15,font=("Arial",30))
    lbl_header.pack(padx=5, pady=5,expand=True)



    mostrar_estanterias_disponibles(biblioteca, frame,controller)

    caja_texto_ingresar_codigo = ctk.CTkEntry(busqueda_frame, placeholder_text="Código de estantería...")
    caja_texto_ingresar_codigo.pack(side="left", fill="x", expand=True, padx=5,pady=5)

    def elegir_estanteria():

        codigo = int(caja_texto_ingresar_codigo.get())
        estanteria = db.get_estanteria_seleccionada(codigo)
        print(estanteria)
        if estanteria != -1:
            controller.estanteria_actual = estanteria
            controller.mostrar_frame("VentanaMostrarEstanteria")
        else:
            print("La estantería no existe")

    boton_ver_estanteria = ctk.CTkButton(busqueda_frame, text="Ver", command=elegir_estanteria)
    boton_ver_estanteria.pack(side="left", padx=5,pady=5)





