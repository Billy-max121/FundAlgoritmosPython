def sistema_notas():
    total = suma = 0
    mayor, menor = -1, 21
    exc = bno = apr = des = 0
    
    while True:
        nota = int(input("Ingrese nota (0-20 o -1 para salir): "))
        if nota == -1: break
        if 0 <= nota <= 20:
            total += 1; suma += nota
            mayor = max(mayor, nota); menor = min(menor, nota)
            # Clasificación
            if nota >= 17: exc += 1
            elif nota >= 14: bno += 1
            elif nota >= 11: apr += 1
            else: des += 1
        else: print("Nota inválida")
        
    if total > 0:
        print(f"Total: {total} | Promedio: {suma/total:.2f}")
        print(f"Mayor: {mayor} | Menor: {menor}")
        print(f"Exc: {exc} | Bno: {bno} | Apr: {apr} | Des: {des}")

if __name__ == "__main__":
    sistema_notas()