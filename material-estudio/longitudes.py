#   Calcula la longitud de cada palabra en una cadena de texto.
def longitudes_palabras(cadena):
    palabras = cadena.split()
    longitudes = {palabra: len(palabra) for palabra in palabras}
    return longitudes

# Ejemplo de uso
cadena = "Hola mundo esto es Python"
longitudes = longitudes_palabras(cadena)
print(longitudes)
# Salida: {'Hola': 4, 'mundo': 5, 'esto': 4, 'es': 2, 'Python': 6}