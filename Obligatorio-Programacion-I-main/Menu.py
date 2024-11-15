from Entities.Gremio import Gremio
from Entities.guerrero import Guerrero 
from Entities.mago import Mago
from Entities.ranger import Ranger
from Entities.mascota import Mascota
from Entities.misiones import Mision  
from Exceptions.exceptions import ( 
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

    def otras_consultas(self):
        while True:
            print("\n--- Otras Consultas ---")
            print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
            print("2. Ver Top 10 Aventureros con Mayor Habilidad")
            print("3. Ver Top 5 Misiones con Mayor Recompensa")
            print("4. Volver al Menú Principal")
        
            opcion = input("Seleccione una opción: ")
        
            match opcion:
                case "1":
                   self.ver_top_aventureros_misiones()
                case "2":
                   self.ver_top_aventureros_habilidad()
                case "3":
                   self.ver_top_misiones_recompensa()
                case "4":
                    print("Regresando al menú principal...")
                    break
                case _:
                    print("Opción inválida. Por favor, intente de nuevo.")

    def ver_top_aventureros_misiones(self):

        aventureros_ordenados = self.gremio.aventureros[:]
        for i in range(len(aventureros_ordenados)):
            for j in range(i + 1, len(aventureros_ordenados)):
                if aventureros_ordenados[i].misiones_completadas < aventureros_ordenados[j].misiones_completadas:
                    aventureros_ordenados[i], aventureros_ordenados[j] = aventureros_ordenados[j], aventureros_ordenados[i]
                elif aventureros_ordenados[i].misiones_completadas == aventureros_ordenados[j].misiones_completadas:
                    if aventureros_ordenados[i].nombre > aventureros_ordenados[j].nombre:
                        aventureros_ordenados[i], aventureros_ordenados[j] = aventureros_ordenados[j], aventureros_ordenados[i]
        
        # Mostrar los 10 primeros
        print("\nTop 10 Aventureros con Más Misiones Resueltas:")
        for i in range(min(10, len(aventureros_ordenados))):
            print(f"{i + 1}. {aventureros_ordenados[i].nombre} - Misiones Resueltas: {aventureros_ordenados[i].misiones_completadas}")

    def ver_top_aventureros_habilidad(self):
        # Ordenación por habilidad total y nombre
        aventureros_ordenados = self.gremio.aventureros[:]
        for i in range(len(aventureros_ordenados)):
            for j in range(i + 1, len(aventureros_ordenados)):
                if aventureros_ordenados[i].calcular_habilidad_total() < aventureros_ordenados[j].calcular_habilidad_total():
                    aventureros_ordenados[i], aventureros_ordenados[j] = aventureros_ordenados[j], aventureros_ordenados[i]
                elif aventureros_ordenados[i].calcular_habilidad_total() == aventureros_ordenados[j].calcular_habilidad_total():
                        if aventureros_ordenados[i].nombre > aventureros_ordenados[j].nombre:
                            aventureros_ordenados[i], aventureros_ordenados[j] = aventureros_ordenados[j], aventureros_ordenados[i]
        # Mostrar los 10 primeros
        print("\nTop 10 Aventureros con Mayor Habilidad Total:")
        for i in range(min(10, len(aventureros_ordenados))):
            print(f"{i + 1}. {aventureros_ordenados[i].nombre} - Habilidad Total: {aventureros_ordenados[i].calcular_habilidad_total()}")

    def ver_top_misiones_recompensa(self):
        # Ordenar las misiones por recompensa (de mayor a menor) y por nombre
        misiones_ordenadas = self.gremio.misiones[:]
        for i in range(len(misiones_ordenadas)):
            for j in range(i + 1, len(misiones_ordenadas)):
                if misiones_ordenadas[i].recompensa < misiones_ordenadas[j].recompensa:
                    misiones_ordenadas[i], misiones_ordenadas[j] = misiones_ordenadas[j], misiones_ordenadas[i]
                elif misiones_ordenadas[i].recompensa == misiones_ordenadas[j].recompensa:
                    if misiones_ordenadas[i].nombre > misiones_ordenadas[j].nombre:
                        misiones_ordenadas[i], misiones_ordenadas[j] = misiones_ordenadas[j], misiones_ordenadas[i]

        # Mostrar las 5 primeras
        print("\nTop 5 Misiones con Mayor Recompensa:")
        for i in range(min(5, len(misiones_ordenadas))):
            print(f"{i + 1}. {misiones_ordenadas[i].nombre} - Recompensa: {misiones_ordenadas[i].recompensa}")

if __name__ == "__main__":
    gremio = Gremio() 
    menu = Menu(gremio)
    menu.menu_principal()