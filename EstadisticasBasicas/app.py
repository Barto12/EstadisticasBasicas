import numpy as np


def calcular_estadisticas(datos):
    """
    Calcula las estadísticas básicas (media, mediana y desviación estándar) de una lista de números.

    Argumentos:
        datos (list): Lista de datos numéricos (enteros o flotantes).

    Retorna:
        dict: Diccionario con las siguientes claves:
            "media": Media aritmética de los datos.
            "mediana": Mediana de los datos.
            "desviacion_estandar": Desviación estándar de los datos.

    Excepciones:
        TypeError: Si la lista contiene elementos no numéricos.
        ValueError: Si la lista está vacía.
    """

    print(f"Datos recibidos en la función: {datos}")

    # Verificar que la lista no esté vacía
    if len(datos) == 0:
        print("Error: La lista de datos no debe estar vacía.")
        raise ValueError("La lista de datos no debe estar vacía.")

    # Verificar que todos los elementos en la lista sean números
    for i, x in enumerate(datos):
        print(f"Verificando el elemento {i}: {x}")
        if not isinstance(x, (int, float)):
            print(f"Error: Elemento no numérico encontrado en la posición {i}: {x}")
            raise TypeError("Todos los elementos de la lista deben ser números.")

    # Convertir la lista de datos en un array de NumPy
    datos_np = np.array(datos)
    print(f"Array de NumPy creado: {datos_np}")

    # Calcular la media, mediana y desviación estándar
    media = np.mean(datos_np)
    print(f"Media calculada: {media}")
    mediana = np.median(datos_np)
    print(f"Mediana calculada: {mediana}")
    desviacion_estandar = np.std(datos_np)
    print(f"Desviación estándar calculada: {desviacion_estandar}")

    # Devolver un diccionario con las estadísticas calculadas
    return {
        "media": media,
        "mediana": mediana,
        "desviacion_estandar": desviacion_estandar
    }


# Ejemplo de uso con datos válidos
datos_validos = [10, 20, 30, 40, 50]
print("Lista de datos válida:", datos_validos)
try:
    estadisticas = calcular_estadisticas(datos_validos)
    print("Estadísticas de datos válidos:")
    print("Media:", estadisticas["media"])
    print("Mediana:", estadisticas["mediana"])
    print("Desviación estándar:", estadisticas["desviacion_estandar"])
except (TypeError, ValueError) as e:
    print(e)

# Ejemplo de uso con datos inválidos (lista vacía)
datos_vacios = []
print("Lista de datos vacía:", datos_vacios)
try:
    estadisticas_vacios = calcular_estadisticas(datos_vacios)
    print("Estadísticas de datos vacíos:")
    print("Media:", estadisticas_vacios["media"])
    print("Mediana:", estadisticas_vacios["mediana"])
    print("Desviación estándar:", estadisticas_vacios["desviacion_estandar"])
except (TypeError, ValueError) as e:
    print(e)

# Ejemplo de uso con datos inválidos (valor no numérico)
datos_invalidos = [10, '20', 30, None, 50]
print("Lista de datos inválidos:", datos_invalidos)
try:
    estadisticas_invalidos = calcular_estadisticas(datos_invalidos)
    print("Estadísticas de datos inválidos:")
    print("Media:", estadisticas_invalidos["media"])
    print("Mediana:", estadisticas_invalidos["mediana"])
    print("Desviación estándar:", estadisticas_invalidos["desviacion_estandar"])
except (TypeError, ValueError) as e:
    print(e)
