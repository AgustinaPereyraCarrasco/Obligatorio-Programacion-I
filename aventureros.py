from abc import ABC, abstractmethod
# La clase Aventurero es abstracta porque representa el concepto general de un aventurero,
# sin los detalles específicos de cada tipo (Guerrero, Mago, Ranger). 

# Define los atributos comunes como nombre, ID y experiencia, pero no debe instanciarse sola,
# ya que siempre se requiere un tipo específico de aventurero.

class Aventurero: #Definición de la clase Aventurero
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, experiencia:int, dinero:float):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero

    # Métodos para acceder a los atributos privados
    @property
    def nombre(self):
        return self.__nombre

    @property
    def id(self):
        return self.__id

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad

    @property
    def experiencia(self):
        return self.__experiencia

#Se le hace un setter a experiencia porque la experiencia cambia a lo largo del juego
    @experiencia.setter
    def experiencia(self, valor):
        self.__experiencia = valor

    @property
    def dinero(self):
        return self.__dinero

#Se le hace un setter a dinero porque el dinero cambia a lo largo del juego
    @dinero.setter
    def dinero(self, cantidad):
        if cantidad >= 0:
            self.__dinero = cantidad
        else:
            raise ValueError("El dinero no puede ser negativo")

# Los métodos abstractos como calcular_rango() y calcular_habilidad_total()
# obligan a cada clase hija a implementar su propia lógica.

    @abstractmethod
    def calcular_rango(self):
        pass

    @abstractmethod
    def calcular_habilidad_total(self):
        pass
