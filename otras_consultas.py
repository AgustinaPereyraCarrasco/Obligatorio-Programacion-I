def otras_consultas(aventureros, misiones):
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