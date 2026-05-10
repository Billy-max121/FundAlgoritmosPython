# ① Función que verifica si un número es par
def EsPar(n):
    return n % 2 == 0


# ② Función que calcula el factorial
def Factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


# Programa principal

# Prueba de EsPar
numero = int(input("Ingrese un número: "))

if EsPar(numero):
    print("El número es par")
else:
    print("El número es impar")


# Prueba de Factorial
n = int(input("Ingrese un número para calcular su factorial: "))

print("Factorial:", Factorial(n))