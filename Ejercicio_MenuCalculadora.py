n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
op = int(input("Operación (1:Suma, 2:Resta, 3:Multiplicación, 4:División): "))

match op:
    case 1:
        print("Resultado:", n1 + n2)
    case 2:
        print("Resultado:", n1 - n2)
    case 3:
        print("Resultado:", n1 * n2)
    case 4:
        if n2 != 0:
            print("Resultado:", n1 / n2)
        else:
            print("Error: No se puede dividir entre cero.")
    case _:
        print("Opción no válida.")