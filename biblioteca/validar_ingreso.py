def fila_columna_maxima(max,mensaje):
    valor = 0
    while valor>max or valor == 0:
        valor = cargarValorNumerico(mensaje)
        if valor>max or valor == 0:
            print("Ingrese un numero valido")
    return valor


def cantidadEspaciosDisponibleEnEstanteria(biblioteca,codigo):
    espacio = 0
    for estanterias in biblioteca:
        if codigo == estanterias['codigo']:
            for fila in estanterias['estanteria']:
                for columna in fila:
                    if estanterias[fila][columna] == 0:
                        espacio +=1
    return espacio

def controlar_codigo_existente(lista,valor):
    igualdad = 0
    if len(lista)>0:
        for i in lista:
            if valor == i["codigo"]:
                igualdad = 1
    return igualdad
