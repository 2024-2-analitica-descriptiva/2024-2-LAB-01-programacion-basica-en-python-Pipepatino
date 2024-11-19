"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
Rta/
{'aaa': 13,
    'bbb': 16,
    'ccc': 23,
    'ddd': 23,
    'eee': 15,
    'fff': 20,
    'ggg': 13,
    'hhh': 16,
    'iii': 18,
    'jjj': 18}}
"""

def pregunta_09():
    """
    Cuenta la cantidad de registros en los que aparece cada clave de la columna 5
    (diccionarios codificados en formato `clave:valor`). Retorna un diccionario 
    ordenado alfabéticamente por las claves de la columna 5.

    Returns:
        dict: Diccionario con las claves de la columna 5 y su frecuencia,
              ordenado alfabéticamente por clave.
    """
    conteo = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            # La columna 5 contiene los diccionarios codificados
            codigos = columnas[4].split(",")  # Separar los pares clave:valor
            
            for codigo in codigos:
                clave, _ = codigo.split(":")  # Obtener solo la clave
                # Contar la aparición de cada clave
                if clave in conteo:
                    conteo[clave] += 1
                else:
                    conteo[clave] = 1
    
    # Ordenar el diccionario alfabéticamente por clave y convertirlo en un nuevo diccionario
    conteo_ordenado = dict(sorted(conteo.items()))
    return conteo_ordenado

# Llamada a la función y prueba
print(pregunta_09())  


