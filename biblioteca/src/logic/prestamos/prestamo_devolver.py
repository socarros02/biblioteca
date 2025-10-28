import customtkinter as ctk
from src.data import data_base as db
from CTkMessagebox import CTkMessagebox


def confirmar(controller,devolucion):
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

def buscar_prestamo(pres,prestamos):
    existe=0
    for i in prestamos:
        if i['prestamo'] == pres:
            existe=1
    return existe

def devolver_libro(frame,controller):



    prestamos = db.get_prestamos()
    if prestamos != None:
        lbl_header = ctk.CTkLabel(frame, text="Prestamos", font=("Arial", 40, "bold"))
        lbl_header.pack(pady=5, expand=True, fill="x")

        frame_devolucion = ctk.CTkFrame(frame, fg_color="transparent")
        frame_devolucion.pack(pady=5, expand=True, fill="x")


        contenedor = ctk.CTkFrame(frame,fg_color="transparent")
        contenedor.pack(pady=5,expand=True,fill="x")


        controller.borrar_widget(contenedor)
        scroll_frame = ctk.CTkScrollableFrame(contenedor)
        scroll_frame.pack(pady=5, expand=True, fill="x")




        for prestamo in prestamos:
            item_frame = ctk.CTkFrame(scroll_frame, corner_radius=12, fg_color="transparent")
            item_frame.pack(pady=8, padx=10, fill="x")

            btn_prestamo = ctk.CTkButton(item_frame,text=f"📖 Préstamo: {prestamo['prestamo']}--📕Ejemplar: {prestamo['ejemplar']}--📚 Título: {prestamo['titulo']}--👤 Persona: {prestamo['persona']}",
                                         anchor="w",
                                         command=lambda devolucion=prestamo['prestamo']:confirmar(controller,devolucion))
            btn_prestamo.pack(pady=5, expand=True, fill="x")




        lbl_error = ctk.CTkLabel(frame, text="", text_color="red")
        lbl_error.pack(fill="x", expand=True, padx=5, pady=5)


        txt_devolucion = ctk.CTkEntry(frame_devolucion,placeholder_text="Indique numero de prestamo que desea devolver")
        txt_devolucion.pack(pady=5, expand=True, fill="x",side="left")
        def devolver_libro(controller,prestamo):

            if prestamo!=0:
                confirmar(controller,prestamo)

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
            confirmar(controller,devolucion)


        btn_devolucion = ctk.CTkButton(frame_devolucion, text="Devolucion",command=lambda:devolver_libro(controller,0))
        btn_devolucion.pack(pady=5,expand=True,fill="x")
    else:
        lbl_header = ctk.CTkLabel(frame, text="No hay prestamos sin finalizar", font=("Arial", 40, "bold"))
        lbl_header.pack(pady=5, expand=True, fill="x")
