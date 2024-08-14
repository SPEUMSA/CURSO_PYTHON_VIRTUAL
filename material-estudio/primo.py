# Verifica si un número es primo.
#Verifica si el numero se divide solo entre 1 y si mismo
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ejemplo de uso
numero=11
print(es_primo(numero))  # Output: True
numero2=4
print(es_primo(numero2))   # Output: False