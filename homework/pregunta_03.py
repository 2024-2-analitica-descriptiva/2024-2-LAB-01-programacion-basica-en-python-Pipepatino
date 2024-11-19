"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

Rta/
[('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

"""

def pregunta_03():
    """
    Retorna la suma de la columna 2 por cada letra de la primera columna 
    como una lista de tuplas (letra, suma), ordenadas alfabéticamente.

    Returns:
        list: Lista de tuplas con la letra y la suma de los valores de 
              la columna 2, ordenadas alfabéticamente.
    """
    sumas = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])  # Convertir el valor de la columna 2 a entero
            
            # Acumular la suma para cada letra
            if letra in sumas:
                sumas[letra] += valor
            else:
                sumas[letra] = valor
    
    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(sumas.items())
    return resultado

# Llamada a la función y prueba
print(pregunta_03())  
