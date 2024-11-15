from .aventureros import Aventurero  # Importa la clase abstracta base Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, experiencia, dinero, mana, misiones_completadas=0):
        super().__init__(nombre, id, puntos_habilidad, experiencia, dinero, misiones_completadas)
        if not (1 <= mana <= 1000):
            raise ValueError("El mana debe estar entre 1 y 1000.")
        self.__mana = mana   # Atributo específico de Mago

    @property
    def mana(self):
        return self.__mana

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
        # Cálculo de habilidad total para Mago
        return self.puntos_habilidad + self.__mana / 10
    