import math

#palabra reservada def Nombre de Funcion(parametros)
def AreaCirculo(radio):
    # Proceso
    resultado = math.pi * radio ** 2
    # retornar el resultado al usuario
    return resultado

def AreaTriangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado

# Obtener el valor del radio del usuario
radio = float(input("Ingrese radio del circulo: "))
# Invocar a la funcion para calcular el valor de area del circulo
resultado = AreaCirculo(radio)
print("El valor de area del circulo es: ", resultado)
# Obtener el area de un triangulo
# obtener los valores de entrada del usuario (inputs)
base = float(input("Ingrese base del triangulo: "))
altura = float(input("Ingrese altura del triangulo: "))
# validar inputs
if base > 0 and altura > 0:
    # procesar los inputs para obtener la saluda (output)
    resultado = AreaTriangulo(base, altura)
    # mostrar al usuario la salida (output)
    print("El area del triangulo es: ", resultado)
else:
    print("Existe un error en los valores de entrada")
print("Fin del programa")

