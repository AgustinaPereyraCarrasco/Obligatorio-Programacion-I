from .aventureros import Aventurero
#Hereda las características comunes del aventurero
class Guerrero(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, fuerza, misiones_completadas=0):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero, misiones_completadas)
        if not (1 <= fuerza <= 100):
            raise ValueError("La fuerza debe estar entre 1 y 100.")
        self.__fuerza = fuerza  # Atributo específico de Guerrero

    @property
    def fuerza(self):
        return self.__fuerza

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

    def calcular_habilidad_total(self):
        # Cálculo de habilidad total para Guerrero
        return self.puntos_habilidad + self.__fuerza / 2
    