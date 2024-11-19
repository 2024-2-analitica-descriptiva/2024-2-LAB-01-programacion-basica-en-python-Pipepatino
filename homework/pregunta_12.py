"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

Rta/
{'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

"""


def pregunta_12():
    """
    Calcula la suma de los valores de la columna 5 (diccionarios codificados como `clave:valor`)
    para cada letra de la columna 1. Retorna un diccionario donde las claves son
    las letras de la columna 1 y los valores son las sumas correspondientes.

    Returns:
        dict: Diccionario con las letras de la columna 1 como claves y la suma de
              los valores de la columna 5 como valores.
    """
    suma_por_letra = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            letra = columnas[0]  # Columna 1
            valores_columna_5 = columnas[4].split(",")  # Dividir los elementos de la columna 5
            
            # Sumar los valores de la columna 5
            suma_valores = sum(int(par.split(":")[1]) for par in valores_columna_5)
            
            # Actualizar el diccionario para la letra correspondiente
            if letra in suma_por_letra:
                suma_por_letra[letra] += suma_valores
            else:
                suma_por_letra[letra] = suma_valores
    
    # Retornar el diccionario ordenado alfabéticamente por las claves
    suma_por_letra_ordenado = dict(sorted(suma_por_letra.items()))
    return suma_por_letra_ordenado

# Llamada a la función y prueba
print(pregunta_12())  