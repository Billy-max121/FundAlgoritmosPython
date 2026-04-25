import math

#palabra reservada def Nombre de Funcion(parametros)
def AreaCirculo(radio):
    # Proceso
    resultado = math.pi * radio ** 2
    # retornar el resultado al usuario
    return resultado

# Obtener el valor del radio del usuario
radio = float(input("Ingrese radio del circulo: "))
# Invocar a la funcion para calcular el valor de area del circulo
resultado = AreaCirculo(radio)
print("El valor de area del circulo es: ", resultado)

