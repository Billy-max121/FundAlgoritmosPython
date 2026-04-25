#Programa que calcula el IMC
#Declaracion y obtencion de datos
peso = float(input("Ingrese su peso (KG): "))
altura = float(input("Ingrese su altura (M): "))
#Proceso
IMC = peso / altura ** 2
#Mostrar informacion
print("Su IMC es: ", IMC)