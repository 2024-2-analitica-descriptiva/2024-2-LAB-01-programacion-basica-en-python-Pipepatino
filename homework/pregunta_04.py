"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.

Rta/
[('01', 3),
    ('02', 4),
    ('03', 2),
    ('04', 4),
    ('05', 3),
    ('06', 3),
    ('07', 5),
    ('08', 6),
    ('09', 3),
    ('10', 2),
    ('11', 2),
    ('12', 3)]
    
"""

def pregunta_04():
    """
    Retorna la cantidad de registros por cada mes basado en la columna 3 
    (que contiene fechas en formato `YYYY-MM-DD`) como una lista de 
    tuplas (mes, cantidad), ordenadas por el número del mes.

    Returns:
        list: Lista de tuplas con el mes (en formato MM) y la cantidad de registros,
              ordenadas por número de mes.
    """
    conteo = {}
    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            # Dividir la línea en columnas separadas por tabulaciones
            columnas = linea.strip().split("\t")
            # Extraer el mes de la columna 3 (formato YYYY-MM-DD)
            fecha = columnas[2]
            mes = fecha.split("-")[1]  # Obtener el mes (MM)
            
            # Contar las apariciones de cada mes
            if mes in conteo:
                conteo[mes] += 1
            else:
                conteo[mes] = 1
    
    # Convertir el diccionario en una lista de tuplas y ordenarla por número de mes
    resultado = sorted(conteo.items(), key=lambda x: int(x[0]))
    return resultado

# Llamada a la función y prueba
print(pregunta_04())  # Esto debería imprimir algo como [('01', 3), ('02', 5), ..., ('12', 4)]
