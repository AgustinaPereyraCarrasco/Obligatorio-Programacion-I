from gremio import Gremio 
from aventureros import Aventurero
from Guerrero import Guerrero 
from Mago import Mago
from Ranger import Ranger
from Mascota import Mascota
from misiones import Mision  
from exceptions import ( 
    InvalidClassError, InvalidHabilidadError, InvalidExperienciaError, 
    InvalidDineroError, InvalidFuerzaError, InvalidManaError, InvalidMascotaError, IDError, NombreMisionError, RangoMisionError
)

class Menu:
    def __init__(self, gremio):
        self.gremio = gremio

    def menu_principal(self):
        while True:
            print("\n ¡Bienvenido al simulador de Dungeons & Dragons! \n")
            print("1. Registrar Aventurero")
            print("2. Registrar Misión")
            print("3. Realizar Misión")
            print("4. Otras Consultas")
            print("5. Salir \n")
            
            opcion = input("Seleccione una opción (1-5): ")
            
            if opcion == "1":
                self.registrar_aventurero()
            elif opcion == "2":
                self.registrar_mision()
            elif opcion == "3":
                self.realizar_mision()
            elif opcion == "4":
                self.otras_consultas()
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")

    def registrar_aventurero(self):
        try:
            tipo = input("Ingrese el tipo de aventurero (Guerrero/Mago/Ranger): ").capitalize()
            if tipo not in ["Guerrero", "Mago", "Ranger"]:
                raise InvalidClassError(f"Tipo de aventurero '{tipo}' no válido.")
                
            nombre = input("Nombre: ")
            id_aventurero = int(input("ID: "))
            if self.gremio.obtener_aventurero_por_id(id_aventurero):
                raise IDError(f"El ID {id_aventurero} ya está en uso. Elija otro ID.")

            habilidad = int(input("Puntos de habilidad (1-100): "))
            if not (1 <= habilidad <= 100):
                raise InvalidHabilidadError("Los puntos de habilidad deben estar entre 1 y 100.")

            experiencia = int(input("Experiencia: "))
            if experiencia < 0:
                raise InvalidExperienciaError("La experiencia no puede ser negativa.")

            dinero = float(input("Dinero: "))
            if dinero < 0:
                raise InvalidDineroError("El dinero no puede ser negativo.")

            if tipo == "Guerrero":
                fuerza = int(input("Fuerza (1-100): "))
                if not (1 <= fuerza <= 100):
                    raise InvalidFuerzaError("La fuerza debe estar entre 1 y 100.")
                aventurero = Guerrero(nombre, id_aventurero, habilidad, experiencia, dinero, fuerza)

            elif tipo == "Mago":
                mana = int(input("Mana (1-1000): "))
                if not (1 <= mana <= 1000):
                    raise InvalidManaError("El mana debe estar entre 1 y 1000.")
                aventurero = Mago(nombre, id_aventurero, habilidad, experiencia, dinero, mana)

            elif tipo == "Ranger":
                tiene_mascota = input("¿Tiene mascota? (S/N): ").upper()
                if tiene_mascota == "S":
                    nombre_mascota = input("Nombre de la mascota: ")
                    habilidad_mascota = int(input("Puntos de habilidad de la mascota (1-50): "))
                    if not (1 <= habilidad_mascota <= 50):
                        raise InvalidMascotaError("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
                    mascota = Mascota(nombre_mascota, habilidad_mascota)
                    aventurero = Ranger(nombre, id_aventurero, habilidad, experiencia, dinero, mascota)
                else:
                    aventurero = Ranger(nombre, id_aventurero, habilidad, experiencia, dinero)

            self.gremio.registrar_aventurero(aventurero)

        except (InvalidClassError, InvalidHabilidadError, InvalidExperienciaError, InvalidDineroError,
                InvalidFuerzaError, InvalidManaError, InvalidMascotaError, IDError) as e:
            print(f"Error: {e}")

    def registrar_mision(self):
        try:
            nombre = input("Nombre de la misión: ")
            recompensa = float(input("Recompensa: "))
            rango = int(input("Rango de la misión (1-5): "))

            if self.gremio.obtener_mision_por_nombre(nombre):
                raise NombreMisionError(f"El nombre de misión '{nombre}' ya está en uso. Elija otro nombre.")

            tipo_mision = input("¿Es misión grupal? (S/N): ").upper() == "S"
            min_miembros = int(input("Número mínimo de miembros para misión grupal: ")) if tipo_mision else 1

            mision = Mision(nombre, recompensa, rango, tipo_mision, min_miembros)
            self.gremio.registrar_mision(mision)

        except (NombreMisionError, RangoMisionError) as e:
            print(f"Error: {e}")

    def realizar_mision(self):
        try:
            nombre_mision = input("Ingrese el nombre de la misión a realizar: ")
            mision = self.gremio.obtener_mision_por_nombre(nombre_mision)
            
            if not mision:
                raise ValueError("Misión no encontrada.")
            
            aventureros_participantes = []
            while True:
                id_aventurero = int(input("Ingrese el ID del aventurero: "))
                aventurero = self.gremio.obtener_aventurero_por_id(id_aventurero)
                if aventurero:
                    aventureros_participantes.append(aventurero)
                else:
                    print("Aventurero no encontrado.")
                
                continuar = input("¿Registrar otro aventurero? (S/N): ").upper()
                if continuar == "N":
                    break

            if mision.tipo_mision and len(aventureros_participantes) < mision.min_miembros:
                raise ValueError("No hay suficientes aventureros para la misión grupal.")

            for aventurero in aventureros_participantes:
                if aventurero.calcular_habilidad_total() < mision.rango * 20:
                    raise ValueError(f"El aventurero {aventurero.nombre} no cumple con el rango de la misión.")
            
            mision.completar_mision()
            recompensa_por_aventurero = mision.recompensa / len(aventureros_participantes)
            
            for aventurero in aventureros_participantes:
                aventurero.incrementar_dinero(recompensa_por_aventurero)
                aventurero.incrementar_experiencia(mision.rango * 10)
                aventurero.incrementar_misiones_completadas()

            print(f"Misión {nombre_mision} completada.")
        
        except ValueError as e:
            print(f"Error: {e}")

    def otras_consultas(self, aventureros, misiones):
        while True:
            print("\n--- Otras Consultas ---")
            print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
            print("2. Ver Top 10 Aventureros con Mayor Habilidad")
            print("3. Ver Top 5 Misiones con Mayor Recompensa")
            print("4. Volver al Menú Principal")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                ver_top_aventureros_misiones()
            elif opcion == "2":
                ver_top_aventureros_habilidad()
            elif opcion == "3":
                ver_top_misiones_recompensa()
            elif opcion == "4":
                print("Regresando al menú principal...")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
                
    def ver_top_aventureros_misiones():
        top_aventureros = sorted(self.aventureros, key=lambda a: (-a.misiones_resueltas, a.nombre))[:10]
        return [f"{i+1}. {a.nombre} - Misiones Resueltas: {a.misiones_resueltas}" for i, a in enumerate(top_aventureros)]

    def ver_top_aventureros_habilidad():
        top_aventureros = sorted(self.aventureros, key=lambda a: (-a.calcular_habilidad_total(), a.experiencia))[:10]
        return [f"{i+1}. {a.nombre} - Habilidad Total: {a.calcular_habilidad_total()}" for i, a in enumerate(top_aventureros)]

    def ver_top_misiones_recompensa():
        top_misiones = sorted(self.misiones, key=lambda m: (-m.recompensa, m.nombre))[:5]
        return [f"{i+1}. {m.nombre} - Recompensa: {m.recompensa}" for i, m in enumerate(top_misiones)]

if __name__ == "__main__":
    from gremio import Gremio
    gremio = Gremio()
    menu = Menu(gremio)
    menu.menu_principal()
