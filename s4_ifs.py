nota = float(input("Ingrese nota: "))
if nota <= 20 and nota >= 0:
    if nota >= 17:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")
else:
    print("Nota invalida")