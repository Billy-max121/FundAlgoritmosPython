valores = [84, 12, 57, 93, 2, 45, 68, 19, 71, 33, 5, 
                88, 14, 62, 27, 99, 41, 7, 50, 76, 18, 91, 
                24, 66, 3, 54, 82, 39, 11, 73, 48, 8, 95, 21, 
                60, 36, 1, 79, 44, 15, 87, 52, 6, 92, 30, 64, 
                23, 77, 49, 10]
print("Valores Almacenados");
for i in range(len(valores)):
    print(valores[i], ", ")

# Captura de Datos de Usuario
valorBuscar = int(input("Ingrese valor a buscar"));

# Busqueda Lineal;
pos = -1
for i in range(len[valores]):
    if valores[i] == valorBuscar:
        pos = i
        break

if pos == -1:
    print("No hallado")
else:
    print("Valor hallado: ", pos)