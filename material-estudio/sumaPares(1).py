#Calcula la suma de los números pares en una lista.    
def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma
    
# Ejemplo de uso
lista= [1, 2, 3, 4, 5, 6]
total=suma_pares(lista)
print(total)
#retorna 12