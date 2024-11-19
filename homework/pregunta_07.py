"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
Rta/
[(0, ['C']),
    (1, ['E', 'B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E', 'E', 'D']),
    (4, ['E', 'B']),
    (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
    (6, ['C', 'E', 'A', 'B']),
    (7, ['A', 'C', 'E', 'D']),
    (8, ['E', 'D', 'E', 'A', 'B']),
    (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
"""

def pregunta_07():
    """
    Asocia los valores de la columna 2 con todas las letras de la columna 1
    que están asociadas a esos valores. Retorna una lista de tuplas 
    (valor_columna_2, lista_letras), ordenadas por el valor de la columna 2.

    Returns:
        list: Lista de tuplas con el formato (valor_columna_2, lista_letras),
              ordenadas por el valor de la columna 2.
    """
    asociaciones = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            letra = columnas[0]  # Columna 1
            valor = int(columnas[1])  # Columna 2 (convertir a entero)
            
            # Asociar el valor con la letra correspondiente
            if valor in asociaciones:
                asociaciones[valor].append(letra)
            else:
                asociaciones[valor] = [letra]
    
    # Convertir el diccionario en una lista de tuplas y ordenarla por el valor de la columna 2
    resultado = sorted(asociaciones.items())
    return resultado

# Llamada a la función y prueba
print(pregunta_07())  

