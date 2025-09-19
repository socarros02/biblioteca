def buscar_titulo(estanteria,titulo):
    valorF = -1
    valorC = -1
    for i, fila in enumerate(estanteria):
        for j, columna in enumerate(fila):
            if columna != 0:
                if columna['libro']['titulo'] == titulo:
                    valorF = i
                    valorC= j
    return valorF,valorC
