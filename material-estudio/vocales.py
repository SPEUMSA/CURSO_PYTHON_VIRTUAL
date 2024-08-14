# Cuenta el número de vocales en una cadena de texto.
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

# Ejemplo de uso
total=contar_vocales("Hola Mundo")
print(total)  # Salida: 4
total2=contar_vocales("Python")
print(total2)      # Salida: 1