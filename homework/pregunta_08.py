"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

Rta/
[(0, ['C']),
    (1, ['B', 'E']),
    (2, ['A', 'E']),
    (3, ['A', 'B', 'D', 'E']),
    (4, ['B', 'E']),
    (5, ['B', 'C', 'D', 'E']),
    (6, ['A', 'B', 'C', 'E']),
    (7, ['A', 'C', 'D', 'E']),
    (8, ['A', 'B', 'D', 'E']),
    (9, ['A', 'B', 'C', 'E'])]

    """


def pregunta_08():
    """
    Asocia los valores de la columna 2 con las letras únicas de la columna 1 
    que están asociadas a esos valores. Retorna una lista de tuplas 
    (valor_columna_2, lista_letras_ordenadas_sin_repetir), ordenadas por el valor 
    de la columna 2.

    Returns:
        list: Lista de tuplas con el formato 
              (valor_columna_2, lista_letras_ordenadas_sin_repetir),
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
                asociaciones[valor].add(letra)  # Usamos un conjunto para evitar duplicados
            else:
                asociaciones[valor] = {letra}
    
    # Convertir el diccionario en una lista de tuplas, ordenarlas y convertir los conjuntos en listas ordenadas
    resultado = sorted(
        (valor, sorted(list(letras))) for valor, letras in asociaciones.items()
    )
    return resultado

# Llamada a la función y prueba
print(pregunta_08()) 

