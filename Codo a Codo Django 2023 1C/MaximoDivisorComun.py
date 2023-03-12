def maxDivisor(numeroA, numeroB):
    if numeroA == 0 or numeroB == 0:
        return "Ingresar numeros mayores a 0"
    if numeroA % numeroB == 0:
        return "El maximo comun divisor es: " + str(numeroB)
    if numeroB % numeroA == 0:
        return "El maximo comun divisor es: " + str(numeroA)
    numeroMenor = min(numeroA, numeroB)
    aux = 1
    while aux < numeroMenor:
        if numeroB % aux == 0 and numeroA % aux == 0:
            divisor = aux
        aux += 1
    return divisor