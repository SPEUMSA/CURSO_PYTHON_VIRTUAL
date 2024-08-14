class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad = 0
    
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"La velocidad del coche ha aumentado a {self.velocidad} km/h")
    
    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"La velocidad del coche ha disminuido a {self.velocidad} km/h")
    
    def detalles(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Velocidad actual: {self.velocidad} km/h")

# Clase Hija
class CocheDeportivo(Coche):
    def __init__(self, marca, modelo, año, turbo):
        super().__init__(marca, modelo, año)
        self.turbo = turbo
    
    def activar_turbo(self):
        if self.turbo:
            self.velocidad += 50
            print("Turbo activado. ¡Velocidad aumentada en 50 km/h!")
        else:
            print("Este coche no tiene turbo.")
    
    def detalles(self):
        super().detalles()
        turbo_status = "Sí" if self.turbo else "No"
        print(f"Turbo: {turbo_status}")

# Creación de objetos
mi_coche = Coche("Toyota", "Corolla", 2020)
mi_coche_deportivo = CocheDeportivo("Ferrari", "488 GTB", 2021, True)

# Uso de métodos del objeto
mi_coche.detalles()  # Muestra los detalles del coche
mi_coche.acelerar(50)  # Aumenta la velocidad del coche
mi_coche.frenar(20)  # Disminuye la velocidad del coche

mi_coche_deportivo.detalles()  # Muestra los detalles del coche deportivo
mi_coche_deportivo.acelerar(70)  # Aumenta la velocidad del coche deportivo
mi_coche_deportivo.activar_turbo()  # Activa el turbo del coche deportivo
mi_coche_deportivo.frenar(30)  # Disminuye la velocidad del coche deportivo