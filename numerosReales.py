def es_numero_real(lexema):
    Q0 = 0  # Estado inicial
    Q = [0, 1, 2, 3, 4, 5, 6]  # Conjunto de estados
    F = [2, 4, 6]  # Estados de aceptación (números reales válidos)
    
    estado_actual = Q0
    indice = 0

    # Definir alfabeto SIGMA
    SIGMA = {
        "+": 0,  # Signo positivo
        "-": 1,  # Signo negativo
        "d": 2,  # Dígitos
        ".": 3,  # Punto decimal
        "e": 4,  # Notación científica (minúscula)
        "E": 4,  # Notación científica (mayúscula)
        "OTRO": 5,  # Cualquier otro carácter
    }

    # Tabla de transiciones DELTA
    DELTA = [
        [1, 1, 2, 5, 5, 5],  # Estado 0 (inicial)
        [5, 5, 2, 5, 5, 5],  # Estado 1 (después de signo + o -)
        [5, 5, 2, 3, 4, 5],  # Estado 2 (después de un dígito)
        [5, 5, 4, 5, 5, 5],  # Estado 3 (después de un punto decimal)
        [5, 5, 4, 5, 5, 5],  # Estado 4 (parte decimal válida)
        [5, 5, 6, 5, 5, 5],  # Estado 5 (después de una "e" o "E")
        [5, 5, 6, 5, 5, 5],  # Estado 6 (después del exponente)
    ]

    # Función para mapear caracteres a símbolos del alfabeto
    def simbolo(caracter):
        if caracter == "+":
            return SIGMA["+"]
        if caracter == "-":
            return SIGMA["-"]
        if caracter.isdigit():
            return SIGMA["d"]
        if caracter == ".":
            return SIGMA["."]
        if caracter in ["e", "E"]:
            return SIGMA["e"]
        return SIGMA["OTRO"]

    # Procesar cada carácter del lexema
    while indice < len(lexema) and estado_actual != 5:  # Estado muerto es 5
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    # Verificar si el estado final es de aceptación
    return estado_actual in F
