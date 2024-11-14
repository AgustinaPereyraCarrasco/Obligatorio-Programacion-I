from Exceptions.exceptions import RangoMisionError

class Mision:
    def __init__(self, nombre, recompensa, rango, tipo_mision, min_miembros=1):
        if not (1 <= rango <= 5):
            raise RangoMisionError(f"El rango de la misión {rango} no es válido. Debe estar entre 1 y 5.")
        self.nombre = nombre
        self.recompensa = recompensa
        self.rango = rango
        self.tipo_mision = tipo_mision
        self.min_miembros = min_miembros
        self.completado = False

    def completar_mision(self):
        self.completado = True
        print(f"La misión {self.nombre} ha sido completada.")

    def __str__(self):
        return f"Mision({self.nombre}, Rango: {self.rango}, Recompensa: {self.recompensa})"