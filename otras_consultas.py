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
    # Lógica para mostrar los 10 aventureros con más misiones completadas
    pass

def ver_top_aventureros_habilidad():
    # Lógica para mostrar los 10 aventureros con mayor habilidad total
    pass

def ver_top_misiones_recompensa():
    # Lógica para mostrar las 5 misiones con mayor recompensa
    pass