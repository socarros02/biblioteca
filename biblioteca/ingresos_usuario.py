import validar_ingreso as validar

def cargar_valor_numerico(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except:
            print("Ingrese un número valido ")

def cargar_valor(mensaje):
    while True:
        try:
            return (input(mensaje))
        except:
            print("Ingrese una opcion valida ")


def disponibilidad_libro():
    disponible = 3
    while disponible != 1 and disponible != 0:
        disponible = cargar_valor_numerico("Ingrese 1 para disponible, y 0 para prestado:\t")
        if disponible != 1 and disponible != 0:
            print("Ingrese un numero valido")
    if disponible == 1:
        disponible = "Disponible"
    else:
        disponible = "Prestado"
    return disponible

def ingresar_codigo(estanteria):
    igualdad = 1
    while igualdad == 1:
        codigo = cargar_valor_numerico("Ingrese codigo de su libro:\t")
        igualdad = validar.controlar_codigo_existente(estanteria,codigo)
    return codigo
