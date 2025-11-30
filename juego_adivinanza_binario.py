"""
Juego de Adivinanza Binaria:
El programa muestra un número en binario y el usuario debe adivinar su valor decimal,
o al revés: se muestra un número decimal y el usuario debe adivinar su valor en binario.
El usuario puede elegir el modo de juego.
Por cada respuesta correcta el usuario suma un punto.
"""
import random # módulo de Python que proporciona funciones para generar números aleatorios.

def decimal_a_binario(decimal):
    if decimal == 0: return "0"
    resultado = ""
    while decimal != 0:
        if decimal % 2 == 0:
            resultado = "0" + resultado
        else:
            resultado = "1" + resultado
        decimal //= 2
    return resultado

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in binario[::-1]:
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal

def modo_binario_a_decimal():
    """El programa muestra un número en binario y el usuario
        debe responder su equivalente en decimal."""

    numero = random.randint(0, 31)  # rango corto de 0 a 31 (5 bits)
    binario = decimal_a_binario(numero)

    print(f"\nConvertí este número binario a decimal:")
    print(f"👉 {binario}")
    respuesta = input("Tu respuesta: ")

    # Validar que la respuesta sea un número entero
    if not respuesta.isdigit():
        print("❌ Entrada inválida. Debés ingresar un número entero.")
        return False
    if int(respuesta) == numero:
        print("✔ Correcto!!")
        return True
    else:
        print(f"❌ Incorrecto. La respuesta correcta era {numero}.")
        return False

def modo_decimal_a_binario():
    """El programa muestra un número decimal y el usuario
        debe responder su equivalente en binario."""

    numero = random.randint(0, 31)
    print(f"\nConvertí este número decimal a binario:")
    print(f"👉 {numero}")
    respuesta = input("Tu respuesta: ")

    # Validar que la respuesta sea un número binario
    for r in respuesta:
        if r != "0" and r != "1":
            print("❌ Entrada inválida. Debés ingresar solo 0s y 1s.")
            return False
    if respuesta == decimal_a_binario(numero):
        print("✓ Correcto!")
        return True
    else:
        print(f"❌ Incorrecto. La respuesta correcta era {decimal_a_binario(numero)}.")
        return False

print("\n=== JUEGO DE ADIVINANZA BINARIA ===")

puntaje = 0

while True:
    print("\nElegí un modo:")
    print("1) Binario → Decimal")
    print("2) Decimal → Binario")
    print("3) Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        if modo_binario_a_decimal():
            puntaje += 1
            print(f"Puntaje actual: {puntaje}")

    elif opcion == "2":
        if modo_decimal_a_binario():
            puntaje += 1
            print(f"Puntaje actual: {puntaje}")

    elif opcion == "3":
        print(f"\nJuego terminado. Puntaje final: {puntaje}")
        break

    else:
        print("\nOpción inválida.")