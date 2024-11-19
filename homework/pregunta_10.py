"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
Rta/
[('E', 3, 5),
    ('A', 3, 4),
    ...
    ('E', 2, 3),
    ('E', 3, 3)]

    """


def pregunta_10():
    """
    Por cada registro, cuenta la cantidad de elementos en las columnas 4 y 5.
    Retorna una lista de tuplas donde cada tupla contiene:
    (letra_columna_1, cantidad_elementos_columna_4, cantidad_elementos_columna_5).

    Returns:
        list: Lista de tuplas con el formato 
              (letra, cantidad_elementos_columna_4, cantidad_elementos_columna_5).
    """
    resultado = []
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            letra = columnas[0]  # Columna 1
            columna_4 = columnas[3].split(",")  # Elementos de la columna 4
            columna_5 = columnas[4].split(",")  # Elementos de la columna 5
            
            # Contar los elementos de las columnas 4 y 5
            cantidad_columna_4 = len(columna_4)
            cantidad_columna_5 = len(columna_5)
            
            # Añadir la tupla al resultado
            resultado.append((letra, cantidad_columna_4, cantidad_columna_5))
    
    return resultado

# Llamada a la función y prueba
print(pregunta_10()) 

