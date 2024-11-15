from .aventureros import Aventurero
#Hereda las características comunes del aventurero
class Guerrero(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, fuerza, misiones_completadas=0):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero, misiones_completadas)
        self.__fuerza = fuerza  # Atributo específico de Guerrero

    @property
    def fuerza(self):
        return self.__fuerza

    def calcular_habilidad_total(self):
        # Cálculo de habilidad total para Guerrero
        return self.puntos_habilidad + self.__fuerza / 2
    