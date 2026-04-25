print("#### Menu Calculadora ####")
print("Menu Operaciones");
print("1. Suma");
print("2. Resta");
print("3. Multiplicacion");
print("4. Division");
print("");
resultado = 0.0
a = float(input("Ingresa primer numero: "))
b = float(input("Ingresa segundo numero: "))
opc = float(input("Ingresa opcion: "))
match opc:
    case 1:
        resultado = a + b
    case 2:
        resultado = a - b
    case 3:
        resultado = a * b
    case 4:
        resultado = a / b
print("Resultado: ", resultado)