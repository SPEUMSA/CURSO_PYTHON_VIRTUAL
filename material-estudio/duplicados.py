# Elimina duplicados de una lista de números.
def eliminar_duplicados(lista):
    return list(set(lista))

# Ejemplo de uso
numeros = [1, 2, 2, 3, 4, 4, 5]
numeros_sin_duplicados = eliminar_duplicados(numeros)
print(numeros_sin_duplicados)
# Output: [1, 2, 3, 4, 5]