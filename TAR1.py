def evaluar_curso():
    print("--- Evaluación de Notas ---")
    
    try:
        nota = float(input("¿Cuál fue la nota final del estudiante? (0 a 100): "))
        
        if nota < 0 or nota > 100:
            print("Esa nota no es válida. Debe estar entre 0 y 100.")
            return

        if nota >= 70:
            print(f"¡Aprobado con un {nota}! Excelente.")
        else:
            print(f"Reprobado con un {nota}. Toca esforzarse más la próxima.")

    except ValueError:
        print("Por favor ingresa un número válido, no letras.")

evaluar_curso()
