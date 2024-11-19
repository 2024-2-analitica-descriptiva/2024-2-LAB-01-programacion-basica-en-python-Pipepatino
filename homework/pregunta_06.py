"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

Rta/
[('aaa', 1, 9),
    ('bbb', 1, 9),
    ('ccc', 1, 10),
    ('ddd', 0, 9),
    ('eee', 1, 7),
    ('fff', 0, 9),
    ('ggg', 3, 10),
    ('hhh', 0, 9),
    ('iii', 0, 9),
    ('jjj', 5, 17)]

"""


def pregunta_06():
    """
    Procesa la columna 5 del archivo para calcular el valor mínimo y máximo 
    asociado a cada clave en los diccionarios codificados en esa columna.

    Returns:
        list: Lista de tuplas con el formato (clave, valor_mínimo, valor_máximo),
              ordenadas alfabéticamente por la clave.
    """
    # Abrir el archivo
    with open('files/input/data.csv', 'r') as archivo:
        # Inicializar los valores máximos y mínimos para cada clave
        valores = {}
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            diccionario = columnas[4]
            # Dividir el diccionario en claves y valores
            pares = diccionario.split(",")
            for par in pares:
                clave, valor = par.split(":")
                valor = int(valor)
                if clave in valores:
                    valores[clave]["max"] = max(valores[clave]["max"], valor)
                    valores[clave]["min"] = min(valores[clave]["min"], valor)
                else:
                    valores[clave] = {"max": valor, "min": valor}
    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente
    resultado = []
    for clave in sorted(valores.keys()):
        resultado.append((clave, valores[clave]["min"], valores[clave]["max"]))
    return resultado
print(pregunta_06()) 
