"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
Rta/
{'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
"""

def pregunta_11():
    """
    Calcula la suma de la columna 2 para cada letra que aparece en la columna 4.
    Retorna un diccionario donde las claves son las letras únicas de la columna 4
    y los valores son las sumas correspondientes, ordenados alfabéticamente.

    Returns:
        dict: Diccionario con las claves de la columna 4 y la suma de la columna 2,
              ordenado alfabéticamente por las claves.
    """
    suma_por_letra = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            valor_columna_2 = int(columnas[1])  # Convertir la columna 2 a entero
            letras_columna_4 = columnas[3].split(",")  # Dividir los elementos de la columna 4
            
            # Sumar el valor de la columna 2 a cada letra en la columna 4
            for letra in letras_columna_4:
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor_columna_2
                else:
                    suma_por_letra[letra] = valor_columna_2
    
    # Ordenar el diccionario alfabéticamente por las claves
    suma_por_letra_ordenado = dict(sorted(suma_por_letra.items()))
    return suma_por_letra_ordenado

# Llamada a la función y prueba
print(pregunta_11())  
