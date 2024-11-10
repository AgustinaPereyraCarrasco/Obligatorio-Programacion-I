from abc import ABC, abstractmethod

class Aventurero(ABC):
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float): 
        self.nombre = nombre
        self.id = id
        self.puntos_de_habilidad = puntos_de_habilidad
        self.experiencia = experiencia
        self.dinero = dinero
        self.misiones_completadas = 0  # Nueva propiedad para contar las misiones completadas

    def __str__(self):
        return (f"{self.__class__.__name__}({self.nombre}, ID: {self.id}, "
                f"Habilidad: {self.puntos_de_habilidad}, Experiencia: {self.experiencia}, "
                f"Dinero: {self.dinero:.2f})")

    @abstractmethod
    def calcular_habilidad_total(self):
        pass

    # Los métodos deben modificar los atributos directamente
    def incrementar_dinero(self, cantidad):
        self.dinero += cantidad

    def incrementar_experiencia(self, cantidad):
        self.experiencia += cantidad

    def incrementar_misiones_completadas(self):
        self.misiones_completadas += 1

class Guerrero(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float, fuerza: int):
        super().__init__(nombre, id, puntos_de_habilidad, experiencia, dinero)
        if not (1 <= fuerza <= 100):
            raise ValueError("La fuerza debe estar entre 1 y 100.")
        self.fuerza = fuerza

    def __str__(self):
        return super().__str__() + f", Fuerza: {self.fuerza}"

    def calcular_habilidad_total(self):
        return self.puntos_de_habilidad + self.fuerza / 2

class Mago(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float, mana: int):
        super().__init__(nombre, id, puntos_de_habilidad, experiencia, dinero)
        if not (1 <= mana <= 1000):
            raise ValueError("El mana debe estar entre 1 y 1000.")
        self.mana = mana

    def __str__(self):
        return super().__str__() + f", Mana: {self.mana}"

    def calcular_habilidad_total(self):
        return self.puntos_de_habilidad + self.mana / 100

class Ranger(Aventurero):
    def __init__(self, nombre: str, id: int, puntos_de_habilidad: int, experiencia: int, dinero: float, mascota=None):
        super().__init__(nombre, id, puntos_de_habilidad, experiencia, dinero)
        self.mascota = mascota

    def __str__(self):
        mascota_info = f", Mascota: {self.mascota}" if self.mascota else ""
        return super().__str__() + mascota_info

    def calcular_habilidad_total(self):
        if self.mascota:
            return self.puntos_de_habilidad + self.mascota.puntos_de_habilidad
        return self.puntos_de_habilidad

class Mascota:
    def __init__(self, nombre: str, puntos_de_habilidad: int):
        if not (1 <= puntos_de_habilidad <= 50):
            raise ValueError("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
        self.nombre = nombre
        self.puntos_de_habilidad = puntos_de_habilidad

    def __str__(self):
        return f"{self.nombre} (Habilidad: {self.puntos_de_habilidad})"
