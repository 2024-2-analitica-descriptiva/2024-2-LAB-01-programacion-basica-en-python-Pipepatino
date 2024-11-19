"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_01():
    """
    Calcula la suma de los valores de la segunda columna de un archivo CSV.

    El archivo CSV se espera que esté ubicado en la ruta "files/input/data.csv",
    con columnas separadas por tabulaciones.

    Returns:
        int: La suma de los valores de la segunda columna.

    Raises:
        FileNotFoundError: Si el archivo no existe en la ruta especificada.
        ValueError: Si algún valor en la segunda columna no puede convertirse a un entero.
    """
    suma = 0
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones (asumiendo que el archivo tiene ese formato)
            columnas = linea.strip().split("\t")
            # Convertir la segunda columna a entero y sumar
            suma += int(columnas[1])
    return suma


# Llamada a la función y prueba
print(pregunta_01())  # Esto debería imprimir 214 si el archivo contiene los datos correctos
