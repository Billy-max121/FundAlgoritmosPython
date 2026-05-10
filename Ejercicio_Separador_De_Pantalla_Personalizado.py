# Función que recibe un carácter y un número
def MostrarLinea(caracter, n):
    for i in range(n):
        print(caracter, end="")
    print()  # Salto de línea


# Programa principal
caracter = input("Ingrese un carácter o símbolo: ")
n = int(input("Ingrese la cantidad de veces: "))

MostrarLinea(caracter, n)