from aventureros import Aventurero
from guerrero import Guerrero 
from mago import Mago
from ranger import Ranger
from mascota import Mascota
from misiones import Mision  
from exceptions import IDError, NombreMisionError

class Gremio:
    def __init__(self):
        self.aventureros = []
        self.misiones = []

    def registrar_aventurero(self, aventurero):
        # Validación de ID único
        if any(a.id == aventurero.id for a in self.aventureros):
            raise IDError(f"El ID {aventurero.id} ya está en uso. Elija otro ID.")
        self.aventureros.append(aventurero)
        print(f"Aventurero {aventurero.nombre} registrado con éxito.")

    def registrar_mision(self, mision):
        # Validación de nombre único para misiones
        if any(m.nombre == mision.nombre for m in self.misiones):
            raise NombreMisionError(f"El nombre de misión '{mision.nombre}' ya está en uso. Elija otro nombre.")
        self.misiones.append(mision)
        print(f"Misión {mision.nombre} registrada con éxito.")

    def obtener_aventurero_por_id(self, id_aventurero):
        return next((a for a in self.aventureros if a.id == id_aventurero), None)

    def obtener_mision_por_nombre(self, nombre_mision):
        return next((m for m in self.misiones if m.nombre == nombre_mision), None)

    def listar_aventureros(self):
        return [str(aventurero) for aventurero in self.aventureros]

    def listar_misiones(self):
        return [str(mision) for mision in self.misiones]

