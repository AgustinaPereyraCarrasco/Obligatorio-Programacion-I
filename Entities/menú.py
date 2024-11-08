from aventureros import Guerrero, Ranger, Mago, Mascota
from mision import Mision, gremio, misiones
class Menu:
    def __init__(self, gremio):
        self.gremio = gremio
        
    def menu_principal(self):
        """Menú principal del simulador de gremio de aventureros"""
        while True:
            print("\n--- Menú Principal ---")
            print("1. Registrar aventurero")
            print("2. Registrar misión")
            print("3. Realizar misión")
            print("4. Otras consultas")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
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
                    print("Saliendo... Muchas Gracias por jugar")
                    break
                case _:
                    print("Opción no válida, por favor seleccione otra.")

    def registrar_aventurero(self):
        """Función para registrar un aventurero"""
        try:
            nombre = str(input("Ingrese el nombre del aventurero: "))
            id = int(input("Ingrese el ID del aventurero: "))
            puntos_habilidad = int(input("Ingrese los puntos de habilidad (1-100): "))
            experiencia = int(input("Ingrese la experiencia del aventurero: "))
            dinero = float(input("Ingrese la cantidad de dinero: "))

            if not (1 <= puntos_habilidad <= 100):
                raise ValueError("Los puntos de habilidad deben estar entre 1 y 100.")
            
            clase = int(input("Elija la clase del aventurero: 1-Guerrero, 2-Mago, 3-Ranger: "))
            
            match clase:
                
                case 1:
                    fuerza = int(input("Ingrese la fuerza del guerrero (1-100): "))
                    if not (1 <= fuerza <= 100):
                        raise ValueError("La fuerza debe estar entre 1 y 100.")
                    aventurero = Guerrero(nombre, id, puntos_habilidad, experiencia, dinero, fuerza)
                case 2:
                    mana = int(input("Ingrese el mana del mago (1-1000): "))
                    if not (1 <= mana <= 1000):
                        raise ValueError("El mana debe estar entre 1 y 1000.")
                    aventurero = Mago(nombre, id, puntos_habilidad, experiencia, dinero, mana)
                case 3:
                    tiene_mascota = input("¿Tiene mascota? (S/N): ").upper()
                    mascota = None
                    if tiene_mascota == "S":
                        nombre_mascota = input("Ingrese el nombre de la mascota: ")
                        puntos_habilidad_mascota = int(input("Ingrese los puntos de habilidad de la mascota (1-50): "))
                        if not (1 <= puntos_habilidad_mascota <= 50):
                            raise ValueError("Los puntos de habilidad de la mascota deben estar entre 1 y 50.")
                        mascota = Mascota(nombre_mascota, puntos_habilidad_mascota)
                    aventurero = Ranger(nombre, id, puntos_habilidad, experiencia, dinero, mascota)
                case _:
                    raise ValueError("Clase no válida.")
            
            gremio.append(aventurero)
            print(f"Aventurero {nombre} registrado.")
        
        except ValueError as e:
            print(f"Error: {e}")

    def registrar_mision(self):
        """Función para registrar una misión"""
        try:
            nombre = input("Ingrese el nombre de la misión: ")
            rango = int(input("Ingrese el rango de la misión (1-5): "))
            recompensa = float(input("Ingrese la recompensa: "))
            tipo_mision = input("¿Es misión grupal? (S/N): ").upper()
            
            if tipo_mision == "S":
                min_miembros = int(input("Ingrese el mínimo de miembros para la misión: "))
                mision = Mision(nombre, rango, recompensa, True, min_miembros)
            else:
                mision = Mision(nombre, rango, recompensa, False)

            if not (1 <= rango <= 5):
                raise ValueError("El rango debe estar entre 1 y 5.")
            
            misiones.append(mision)
            print(f"Misión {nombre} registrada")
        
        except ValueError as e:
            print(f"Error: {e}")

    def realizar_mision(self):
        """Función para realizar una misión"""
        try:
            nombre_mision = input("Ingrese el nombre de la misión a realizar: ")
            mision = next((m for m in misiones if m.nombre == nombre_mision), None)
            
            if not mision:
                raise ValueError("Misión no encontrada.")
            
            aventureros_participantes = []
            while True:
                id_aventurero = int(input("Ingrese el ID del aventurero: "))
                aventurero = next((a for a in gremio if a.id == id_aventurero), None)
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
            print("Consultas:")
       
if __name__ == "__main__":
    from Gremio import Gremio
    gremio = Gremio()
    menu = Menu(gremio)
    menu.menu_principal()
