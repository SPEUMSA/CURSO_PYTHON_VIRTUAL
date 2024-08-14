# Calcula el factorial de un número n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero=5
print(factorial(numero))  # Output: 120