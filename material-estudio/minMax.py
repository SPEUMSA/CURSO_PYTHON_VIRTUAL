#  Encuentra el número más pequeño y el más grande en una lista de números.
def encontrar_min_max(lista):
    if not lista:
        return None, None
    return min(lista), max(lista)
#   
# Ejemplo de uso
numeros = [3, 5, 1, 9, 2, 8]
min_num, max_num = encontrar_min_max(numeros)
print(f"El número más pequeño es {min_num} y el más grande es {max_num}")
# Output: El número más pequeño es 1 y el más grande es 9