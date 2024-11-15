from Entities.gremio import Gremio
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
            
            match opcion:
                case "1":
                    self.registrar_aventurero()
                case "2":
                    self.registrar_mision()
                case "3":
                    self.realizar_mision()
                case "4":
                    self.otras_consultas()
                case "5":
                    print("¡Gracias por usar el simulador! Hasta luego.")
                    return
                case _:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

    def registrar_aventurero(self):
        try:
            tipo = input("Ingrese el tipo de aventurero (Guerrero/Mago/Ranger): ").capitalize()
            while tipo not in ["Guerrero", "Mago", "Ranger"]:
                print("Tipo de aventurero no válido. Ingrese Guerrero, Mago o Ranger.")
                tipo = input("Ingrese el tipo de aventurero (Guerrero/Mago/Ranger): ").capitalize()
                
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
                habilidad = int(input("Puntos de habilidad (1-100): "))
                if not (1 <= habilidad <= 100):
                        raise InvalidHabilidadError("Los puntos de habilidad deben estar entre 1 y 100.")
                tiene_mascota = input("¿Tiene mascota? (S/N): ").upper()
                while tiene_mascota not in ["S", "N"]:
                    print("Respuesta inválida. Por favor ingrese 'S' para Sí o 'N' para No.")
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

            tipo_mision = input("¿Es misión grupal? (S/N): ").upper()
            while tipo_mision not in ["S", "N"]:
                print("Respuesta inválida. Por favor ingrese 'S' para Sí o 'N' para No.")
                tipo_mision = input("¿Es misión grupal? (S/N): ").upper()
            tipo_mision = tipo_mision == "S"
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
                while continuar not in ["S", "N"]:
                    print("Opción inválida. Por favor, ingrese 'S' para sí o 'N' para no.")
                    continuar = input("¿Registrar otro aventurero? (S/N): ").upper()
                if continuar == "N":
                    break
        
            # Verificar si la misión es grupal
            if mision.tipo_mision and len(aventureros_participantes) < mision.min_miembros:
                raise ValueError("No hay suficientes aventureros para la misión grupal.")
        
            # Verificar que cada aventurero cumpla con el rango de habilidad para la misión
            for aventurero in aventureros_participantes:
                if aventurero.calcular_habilidad_total() < mision.rango * 20:
                    raise ValueError(f"El aventurero {aventurero.nombre} no cumple con el rango de la misión.")
        
            # Completar misión y distribuir recompensas y experiencia
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
            while opcion not in ["1", "2", "3", "4"]:
                print("Opción inválida. Por favor, intente de nuevo.")
                opcion = input("Seleccione una opción: ")
    
            match opcion:
                case "1":
                    self.ver_top_aventureros_misiones()
                case "2":
                    self.ver_top_aventureros_habilidad()
                case "3":
                    self.ver_top_misiones_recompensa()
                case "4":
                    return

    def ver_top_aventureros_misiones(self):
        top = self.gremio.obtener_top_aventureros_misiones()
        # Ordenar aventureros según el número de misiones completadas
        top_ordenado = sorted(top, key=lambda aventurero: aventurero.misiones_completadas, reverse=True)
        
        for rank, aventurero in enumerate(top_ordenado, start=1):
            print(f"{rank}. {aventurero.nombre} - Misiones: {aventurero.misiones_completadas}")

    def ver_top_aventureros_habilidad(self):
        top = self.gremio.obtener_top_aventureros_habilidad()
        # Ordenar aventureros según la habilidad total
        top_ordenado = sorted(top, key=lambda aventurero: aventurero.calcular_habilidad_total(), reverse=True)

        for rank, aventurero in enumerate(top_ordenado, start=1):
            print(f"{rank}. {aventurero.nombre} - Habilidad Total: {aventurero.calcular_habilidad_total()}")

    def ver_top_misiones_recompensa(self):
        top = self.gremio.obtener_top_misiones_recompensa()
        # Ordenar misiones según la recompensa
        top_ordenado = sorted(top, key=lambda mision: mision.recompensa, reverse=True)

        for rank, mision in enumerate(top_ordenado, start=1):
            print(f"{rank}. {mision.nombre} - Recompensa: {mision.recompensa}")


if __name__ == "__main__":
    gremio = Gremio() 
    menu = Menu(gremio)
    menu.menu_principal()