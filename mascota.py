class Mascota:
    def __init__(self, nombre, puntos_habilidad):
        self.__nombre = nombre
        self.__puntos_habilidad = puntos_habilidad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad