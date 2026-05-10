def leer_nota(mensaje):
    """Pide y valida una nota entre 0 y 20."""
    while True:
        try:
            nota = float(input(f"{mensaje} (0-20): "))
            if 0 <= nota <= 20:
                return nota
            else:
                print(" [Error] La nota debe estar entre 0 y 20.")
        except ValueError:
            print(" [Error] Debe ingresar un número válido.")

def es_aprobado(nota):
    """Retorna True si la nota es mayor o igual a 11."""
    return nota >= 11

def clasificar_nota(nota):
    """Retorna la categoría de la nota según el puntaje."""
    if nota >= 18:
        return "Excelente"
    elif nota >= 15:
        return "Bueno"
    elif nota >= 11:
        return "Aprobado"
    else:
        return "Desaprobado"

def calcular_promedio(suma, n):
    """Calcula y retorna el promedio."""
    return suma / n if n > 0 else 0.0

def mostrar_estadisticas(prom, mayor, menor, aprobados, total):
    """Muestra el resumen final de los datos procesados."""
    print("\n" + "="*40)
    print("        RESUMEN DE ESTADÍSTICAS         ")
    print("="*40)
    print(f" Promedio General:   {prom:.2f}")
    print(f" Nota más Alta:      {mayor}")
    print(f" Nota más Baja:      {menor}")
    print(f" Total Aprobados:    {aprobados}")
    print(f" Total Desaprobados: {total - aprobados}")
    print(f" Porcentaje Éxito:   {(aprobados / total) * 100:.1f}%")
    print("="*40 + "\n")

def main():
    # Variables de acumulación
    suma_notas = 0
    nota_mayor = -1.0
    nota_menor = 21.0
    contador_aprobados = 0
    
    print("=== SISTEMA DE ANÁLISIS DE NOTAS (PYTHON) ===")
    try:
        total_notas = int(input("¿Cuántas notas desea ingresar?: "))
    except ValueError:
        print("Cantidad no válida.")
        return

    for i in range(1, total_notas + 1):
        # 1. Leer y validar
        nota_actual = leer_nota(f"Estudiante {i}")
        
        # 2. Acumular y comparar
        suma_notas += nota_actual
        if nota_actual > nota_mayor: nota_mayor = nota_actual
        if nota_actual < nota_menor: nota_menor = nota_actual
        
        # 3. Evaluar aprobación
        if es_aprobado(nota_actual):
            contador_aprobados += 1
            
        # 4. Clasificar y mostrar resultado parcial
        categoria = clasificar_nota(nota_actual)
        print(f"   -> Clasificación: {categoria}")

    # 5. Cálculos finales mediante funciones
    promedio_final = calcular_promedio(suma_notas, total_notas)
    
    # 6. Mostrar reporte
    mostrar_estadisticas(promedio_final, nota_mayor, nota_menor, contador_aprobados, total_notas)

# Punto de entrada del script
if __name__ == "__main__":
    main()