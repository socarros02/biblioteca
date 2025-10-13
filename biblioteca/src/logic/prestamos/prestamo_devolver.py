import customtkinter as ctk
from src.data import data_base as db
from CTkMessagebox import CTkMessagebox
prestamo=0


def buscar_prestamo(pres,prestamos):
    existe=0
    for i in prestamos:
        if i['prestamo'] == pres:
            existe=1
    return existe
def devolver_libro(frame,controller):
    global prestamo
    prestamo = 0

    lbl_lista = ctk.CTkLabel(frame, text="Lista de prestamos", font=("Arial", 45, "bold"))
    lbl_lista.pack(pady=5, expand=True, fill="x")
   
    frame_devolucion = ctk.CTkFrame(frame,fg_color="transparent")
    frame_devolucion.pack(pady=5, expand=True, fill="x")


    contenedor = ctk.CTkFrame(frame)
    contenedor.pack(pady=5,expand=True,fill="x")



    prestamos = db.get_prestamos()
    if len(prestamos)>4:
        controles = ctk.CTkFrame(frame,fg_color="transparent")
        controles.pack(pady=5, expand=True, fill="x")
    if prestamos!=None:
        def mostrar_siguiente():
            global prestamo
            posicion = 0
            controller.borrar_widget(contenedor)
            controller.borrar_widget(controles)
            prestamos=db.get_prestamos()
            while prestamo < len(prestamos) and posicion != 4:
                item_frame = ctk.CTkFrame(contenedor, corner_radius=12, fg_color="#F5EBE0")
                item_frame.pack(pady=8, padx=10, fill="x")

                ctk.CTkLabel(item_frame, text=f"📖 Préstamo: {prestamos[prestamo]['prestamo']}").pack(padx=10, pady=2,side="left")
                ctk.CTkLabel(item_frame, text=f"📕 Ejemplar: {prestamos[prestamo]['ejemplar']}").pack(padx=10, pady=2,side="left")
                ctk.CTkLabel(item_frame, text=f"📚 Título: {prestamos[prestamo]['titulo']}").pack(padx=10,pady=2,side="left")
                ctk.CTkLabel(item_frame, text=f"👤 Persona: {prestamos[prestamo]['persona']}").pack(padx=10,pady=2,side="left")

                posicion +=1
                prestamo += 1
            if prestamo<len(prestamos):
                btn_siguiente = ctk.CTkButton(controles,text="Siguiente",command=mostrar_siguiente)
                btn_siguiente.pack(pady=5,side="right")

            def mostrar_anterior():
                global prestamo
                contador = 8
                while prestamo % 4 != 0:
                    prestamo -= 1
                    contador -= 1
                if contador != 8:
                    prestamo -= 4
                else:
                    prestamo -= 8
                if prestamo < 4:
                    controller.borrar_widget(controles)
                mostrar_siguiente()


            if prestamo>5:
                btn_anterior = ctk.CTkButton(controles,text="Anterior",command=mostrar_anterior)
                btn_anterior.pack(pady=5,side="left")
        mostrar_siguiente()
    lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
    lbl_error.pack(fill="x", expand=True, padx=5, pady=5)


    txt_devolucion = ctk.CTkEntry(frame_devolucion, corner_radius=12,placeholder_text="Indique numero de prestamo que desea devolver")
    txt_devolucion.pack(pady=5, expand=True, fill="x",side="left")
    def devolver_libro(controller):
        global prestamo

        devolucion = txt_devolucion.get()

        if not devolucion:
            lbl_error.configure(text="Ingrese datos validos")
            return

        try:
            devolucion = int(devolucion)
            existe = buscar_prestamo(devolucion, prestamos)
            if existe==0:
                raise ValueError
        except ValueError:
            lbl_error.configure(text="Ingrese datos validos")
            return
        msg = CTkMessagebox(title="Confirmar préstamo",
                            message=f"¿Deseas finalizar el prestamo {devolucion}?",
                            icon="question",
                            option_1="Sí",
                            option_2="No",
                            master=controller)

        if msg.get() == "Sí":
            CTkMessagebox(title="Éxito",
                          message=f"Prestamo {devolucion} finalizdo.",
                          icon="check",
                          master=controller)
            db.devolver_prestamos(devolucion)
            controller.mostrar_frame("VentanaDevolverLibro")
        prestamo=0

    btn_devolucion = ctk.CTkButton(frame_devolucion, text="Devolucion",command=lambda:devolver_libro(controller))
    btn_devolucion.pack(pady=5,expand=True,fill="x")
