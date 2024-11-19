"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

Rta/
[('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

"""


def pregunta_05():
    """
    Retorna una lista de tuplas con el valor máximo y mínimo de la columna 2 
    por cada letra de la columna 1, ordenadas alfabéticamente.

    Returns:
        list: Lista de tuplas con el formato (letra, valor_máximo, valor_mínimo),
              ordenadas alfabéticamente por la letra.
    """
    valores = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])  # Convertir la columna 2 a entero
            
            # Actualizar el máximo y mínimo para cada letra
            if letra in valores:
                valores[letra]["max"] = max(valores[letra]["max"], valor)
                valores[letra]["min"] = min(valores[letra]["min"], valor)
            else:
                valores[letra] = {"max": valor, "min": valor}
    
    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente
    resultado = [(letra, datos["max"], datos["min"]) for letra, datos in sorted(valores.items())]
    return resultado

# Llamada a la función y prueba
print(pregunta_05()) 