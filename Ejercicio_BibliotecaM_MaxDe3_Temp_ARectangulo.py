def max_de_3(a, b, c):
    """Devuelve el mayor de tres números."""
    return max(a, b, c)

def convertir_temp(c):
    """Convierte Celsius a Fahrenheit (F = C × 9/5 + 32)."""
    return (c * 9/5) + 32

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

# --- Bloque de interacción con el usuario ---

print("--- Mayor de tres números ---")
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
print(f"El mayor es: {max_de_3(n1, n2, n3)}")

print("\n--- Conversión de Temperatura ---")
celsius = float(input("Ingrese grados Celsius: "))
print(f"{celsius}°C equivalen a {convertir_temp(celsius)}°F")

print("\n--- Área de un Rectángulo ---")
b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura: "))
print(f"El área es: {area_rectangulo(b, h)}")