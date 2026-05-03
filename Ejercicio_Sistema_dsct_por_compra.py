def calcular_descuento():

    tipo = int(input("Ingrese tipo de cliente (1=VIP, 2=Regular): "))
    monto = float(input("Ingrese monto de compra: "))

    if tipo == 1:  # proceso del VIP
        tasa = 0.20 if monto > 100 else 0.10
    else:          # Proceso del Regular
        tasa = 0.10 if monto > 200 else 0.05

    descuento = monto * tasa
    total = monto - descuento

    print(f"Descuento aplicado: S/{descuento:.2f}")
    print(f"Monto final a pagar: S/{total:.2f}")

if __name__ == "__main__":
    calcular_descuento()