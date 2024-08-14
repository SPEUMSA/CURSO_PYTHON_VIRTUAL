import math

class Figura:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        pass
    
    def detalles(self):
        print(f"Color: {self.color}")

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        return math.pi * self.radio ** 2
    
    def detalles(self):
        super().detalles()
        print(f"Figura: Círculo, Radio: {self.radio}, Área: {self.area()}")

class Rectangulo(Figura):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def detalles(self):
        super().detalles()
        print(f"Figura: Rectángulo, Ancho: {self.ancho}, Alto: {self.alto}, Área: {self.area()}")

# Creación de objetos
circulo = Circulo("Rojo", 5)
rectangulo = Rectangulo("Azul", 10, 5)

# Uso de métodos del objeto
circulo.detalles()  # Muestra los detalles del círculo
rectangulo.detalles()  # Muestra los detalles del rectángulo