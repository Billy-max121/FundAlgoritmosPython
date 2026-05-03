def Contar():
    cont = 0 # variable local de la func
    cont = cont + 1 # suma 1 a la variable local
    print ("Var cont de la funcion: ", cont)

cont = 100; # declara variable local main
cont = cont + 1 # sumando 1 a la var local main
Contar()
Contar()
Contar()
print ("Var cont de Main: ", cont)