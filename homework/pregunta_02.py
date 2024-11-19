"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

Rta/
[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

"""


def pregunta_02():
    """
    Retorna la cantidad de registros por cada letra de la primera columna 
    como una lista de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Returns:
        list: Lista de tuplas con la letra y la cantidad de registros,
              ordenadas alfabéticamente.
    """
    conteo = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Obtener la primera columna
            letra = linea.strip().split("\t")[0]
            # Contar las apariciones de cada letra
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
    
    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(conteo.items())
    return resultado

# Llamada a la función y prueba
print(pregunta_02())  
