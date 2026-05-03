def procesar_numeros():
    n = int(input("¿Cuántos números desea sumar? "))
    suma = 0
    mayor = float('-inf')
    menor = float('inf')
    
    i = 0
    while i < n:
        num = int(input(f"Ingrese número {i + 1}: "))
        suma += num
        if num > mayor: mayor = num
        if num < menor: menor = num
        i += 1
    
    promedio = suma / n
    print(f"Cantidad: {n} | Suma total: {suma} | Promedio: {promedio:.2f}")
    print(f"Número mayor: {mayor} | Número menor: {menor}")

if __name__ == "__main__":
    procesar_numeros()