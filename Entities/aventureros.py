from abc import ABC, abstractmethod
# La clase Aventurero es abstracta porque representa el concepto general de un aventurero,
# sin los detalles específicos de cada tipo (Guerrero, Mago, Ranger). 

# Define los atributos comunes como nombre, ID y experiencia, pero no debe instanciarse sola,
# ya que siempre se requiere un tipo específico de aventurero.

class Aventurero:
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, experiencia:int, dinero:float, misiones_completadas:int):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero
        self.__misiones_completadas = misiones_completadas


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

    @experiencia.setter
    def experiencia(self, valor):
        self.__experiencia = valor

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, cantidad):
        if cantidad >= 0:
            self.__dinero = cantidad
        else:
            raise ValueError("El dinero no puede ser negativo")

    @property
    def misiones_completadas(self):
        return self.__misiones_completadas

    def incrementar_misiones_completadas(self):
        self.__misiones_completadas += 1
        
    def incrementar_dinero(self, cantidad):
        self.dinero += cantidad
        
    def incrementar_experiencia(self, cantidad):
        self.experiencia += cantidad


