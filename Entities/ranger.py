from .aventureros import Aventurero  # Importa la clase abstracta base Aventurero
from .mascota import Mascota  # Importa la clase Mascota, si el Ranger puede tener una mascota

class Ranger(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, misiones_completadas=0, mascota=None):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero, misiones_completadas)
        self.__mascota = mascota  # La mascota es opcional

    @property
    def mascota(self):
        return self.__mascota

    def calcular_habilidad_total(self):
        return self.puntos_habilidad + (self.__mascota.puntos_habilidad if self.__mascota else 0)
    
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
            