from abc import ABC, abstractmethod

class Aventurero(ABC):
    def __init__(self, nombre:str, id:int, puntos_habilidad:int, experiencia:int, dinero:float, misiones_completadas:int):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero
        self.__misiones_completadas = misiones_completadas = 0


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
    
    @abstractmethod
    def calcular_habilidad_total(self):
        pass

    def calcular_rango(self):
        habilidad_total = self.calcular_habilidad_total()
        match habilidad_total:
            case _ if habilidad_total <= 20:
                return 1
            case _ if habilidad_total <= 40:
                return 2
            case _ if habilidad_total <= 60:
                return 3
            case _ if habilidad_total <= 80:
                return 4
            case _:
                return 5

    def incrementar_misiones_completadas(self):
    # Asegúrate de que self.__misiones_completadas sea un entero
        if isinstance(self.__misiones_completadas, int):
            self.__misiones_completadas += 1
        else:
            print("Error: El contador de misiones no es un número entero.")

        
    def incrementar_dinero(self, cantidad):
        self.dinero += cantidad
        
    def incrementar_experiencia(self, cantidad):
        self.experiencia += cantidad


