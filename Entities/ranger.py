from Entities.aventureros import Aventurero  # Importa la clase abstracta base Aventurero
from Entities.mascota import Mascota  # Importa la clase Mascota, si el Ranger puede tener una mascota

class Ranger(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, misiones_completadas=0, mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero, misiones_completadas)
        self.__mascota = mascota  # La mascota es opcional

    @property
    def mascota(self):
        return self.__mascota

    def calcular_rango(self):
        habilidad_total = self.puntos_habilidad + (self.__mascota.puntos_habilidad if self.__mascota else 0)
        return habilidad_total // 20

    def calcular_habilidad_total(self):
        return self.puntos_habilidad + (self.__mascota.puntos_habilidad if self.__mascota else 0)