import customtkinter as ctk
from data_base import data_base as db

est = 0

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def posicion_estanteria(estanterias, codigo):
    valor = -1
    for idx, datos in enumerate(estanterias):
        if int(codigo) == datos['codigo']:
            valor = idx
    return valor


def mostrar_estanterias_disponibles(biblioteca, frame,controller):
    global est
    est=0
    lista_frame = ctk.CTkFrame(frame, fg_color="transparent")
    lista_frame.pack(fill="both", expand=True, pady=10)
    controles = ctk.CTkFrame(frame, fg_color="transparent")
    controles.pack(fill="both", expand=True, pady=10)

    def mostrar_anterior():
        global est
        contador = 10
        while est % 5 != 0:
            est -= 1
            contador -= 1
        if contador != 10:
            est -= 5
        else:
            est -= 10
        if est < 5:
            controller.borrar_widget(controles)
        mostrar_siguiente()

    def mostrar_siguiente():
        global est
        posicion=0

        controller.borrar_widget(lista_frame)

        while posicion!=5 and est<len(biblioteca):

            fila_frame = ctk.CTkFrame(lista_frame, fg_color="transparent",corner_radius=5)
            fila_frame.pack(fill="x", pady=2)
            estanteria_actual = biblioteca[est]
            disponible =estanteria_actual['capacidad']- db.contar_ejemplares_por_estanteria(estanteria_actual["codigo"])
            label = ctk.CTkLabel(
                fila_frame,
                text=f"🗄️{estanteria_actual['nombre']}   -   código {estanteria_actual['codigo']}  -   capacidad {estanteria_actual['capacidad']}  -  espacios disponibles {disponible}",
                text_color="#333333",
                fg_color="#F5EBE0",
                corner_radius=8,
                padx=10,
                pady=5
            )
            label.pack(pady=5,expand=True,fill="x",padx=15)
            est+=1
            posicion+=1

        btn_siguiente = ctk.CTkButton(
            controles,
            text="siguiente",
            corner_radius=8,
            command=mostrar_siguiente,
            width=50
        )
        btn_siguiente.pack(side="right", padx=100, pady=5)
        if est> len(biblioteca) - 1:
            controller.borrar_widget(controles)

        if est > 5:
            btn_anterior = ctk.CTkButton(
                controles,
                text="anterior",
                corner_radius=8,
                command=mostrar_anterior,
                width=50
            )
            btn_anterior.pack(side="left", padx=100, pady=5)


    mostrar_siguiente()






def abrir_estanteria(frame,controller):

    biblioteca = db.get_estanterias()


    controller.borrar_widget(frame)

    header = ctk.CTkFrame(frame, fg_color="transparent",height=10)
    header.pack( padx=5, pady=5)
    busqueda_frame = ctk.CTkFrame(frame, fg_color="transparent")
    busqueda_frame.pack(fill="x", pady=10, padx=10)



    contenedor = ctk.CTkFrame(frame)
    contenedor.pack(fill="both", expand=True, padx=20, pady=2)

    lbl_header = ctk.CTkLabel(header, text= "Estanterias",corner_radius=15,font=("Arial",30))
    lbl_header.pack(padx=5, pady=5,expand=True)



    mostrar_estanterias_disponibles(biblioteca, contenedor,controller)

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





