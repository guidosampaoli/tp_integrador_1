def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    i = 1
    print(f"\nNúmero binario ingresado: {binario}")
    print("Operación que realiza el bucle For:")
    print("Aplicamos 'slicing' en la cadena recibida como binario")
    print(f"Tenemos {binario} y hacemos \"{binario}\"[::-1] = {binario[::-1]}"
          f"para comenzar a iterar de atrás hacia adelante:\n")
    for digito in binario[::-1]:
        print(f"{i}ª iteración: {digito} x (2^{potencia}) = {digito} x {2 ** potencia} = {int(digito) * (2 ** potencia)} decimal")
        print(f"En la variable 'decimal' tenemos {decimal} y sumamos {int(digito) * (2 ** potencia)}\n")
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
        i += 1
    return f"Sumatoria final: obtenemos {decimal} decimal"

print(binario_a_decimal("1010"))