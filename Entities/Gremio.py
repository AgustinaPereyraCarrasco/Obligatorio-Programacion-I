class Gremio:
    def __init__(self):
        self.aventureros = []
        self.misiones = []

    def registrar_aventurero(self, nombre, clase, id, puntos_habilidad, experiencia, dinero):
        if clase.lower() == "guerrero":
            from aventureros import Guerrero
            nuevo_aventurero = Guerrero(nombre, id, puntos_habilidad, experiencia, dinero)
        elif clase.lower() == "mago":
            from aventureros import Mago
            nuevo_aventurero = Mago(nombre, id, puntos_habilidad, experiencia, dinero)
        elif clase.lower() == "ranger":
            from aventureros import Ranger
            nuevo_aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero)
        else:
            print("Clase de aventurero no válida.")
            return

        self.aventureros.append(nuevo_aventurero)
        print(f"Aventurero {nombre} registrado exitosamente.")

    def registrar_mision(self, nombre, rango, recompensa, es_grupal, cantidad_minima=None):
        from mision import Mision
        nueva_mision = Mision(nombre, rango, recompensa, es_grupal, cantidad_minima)
        self.misiones.append(nueva_mision)
        print(f"Misión {nombre} registrada exitosamente.")

    def asignar_mision(self, nombre_mision, ids_aventureros):
        print("Asignando misión...")
