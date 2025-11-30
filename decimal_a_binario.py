def decimal_a_binario(n):
    if n == 0: return "0" #Manejamos el caso del 0, ya que si el número
    # que sale es 0 no se va a ejecutar el bucle while
    resultado = ""
    i = 1
    print(f"Número decimal ingresado: {n}")
    print("Operación que realiza el bucle While:")
    while n != 0:
        if n % 2 == 0:
            resultado = "0" + resultado
            print(f"{i}ª iteración: {n} / 2 = {n // 2} 🡢 resto = {n % 2} | resultado: {resultado}")
        else:
            resultado = "1" + resultado
            print(f"{i}ª iteración: {n} / 2 = {n // 2} 🡢 resto = {n % 2} | resultado: {resultado}")
        n = n // 2
        i += 1
    return f"Número binario obtenido: {resultado}"

print(decimal_a_binario(10))