class Mision:
    def __init__(self, nombre:str, rango:int, recompensa:float, tipo_mision, min_miembros=1):
        self.nombre = nombre
        self.rango = rango
        self.recompensa = recompensa
        self.tipo_mision = tipo_mision
        self.min_miembros = min_miembros
        self.completada = False

    def completar_mision(self):
        self.completada = True

gremio = []  # Lista para almacenar los aventureros
misiones = []  # Lista para almacenar las misiones