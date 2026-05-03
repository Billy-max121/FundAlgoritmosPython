precio = 100.50
precioConDescuento = 0.0

def CalcularDescuento(_precio):
    if _precio > 80:
        _precio = _precio - (_precio * 0.1)
    print("Valor de precio (copia): ", _precio)
    return _precio

print("Precio original: ", precio);
precioConDescuento = CalcularDescuento(precio)
print ("Precio con descuento: ", precioConDescuento)
