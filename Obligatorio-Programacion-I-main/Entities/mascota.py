class Mascota:
    def __init__(self, nombre, puntos_habilidad):
        if not (1 <= puntos_habilidad <= 50):
            raise ValueError("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
        self.__nombre = nombre
        self.__puntos_habilidad = puntos_habilidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad