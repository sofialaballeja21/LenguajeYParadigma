def es_numero_entero(lexema):
    Q0 = 0  # Estado inicial
    Q = [0, 1, 2, 3]  # Conjunto de estados
    F = [2]  # Estado de aceptación (números enteros válidos)
    
    estado_actual = Q0
    indice = 0

    # Definir alfabeto SIGMA
    SIGMA = {
        "+": 0,  # Signo positivo
        "-": 1,  # Signo negativo
        "d": 2,  # Dígitos
        "OTRO": 3  # Caracteres inválidos
    }

    # Tabla de transiciones DELTA
    DELTA = [
        [1, 1, 2, 3],  # Estado 0 (inicial)
        [3, 3, 2, 3],  # Estado 1 (después de + o -)
        [3, 3, 2, 3],  # Estado 2 (después de un dígito)
        [3, 3, 3, 3],  # Estado 3 (estado muerto)
    ]

    # Función para mapear caracteres a símbolos del alfabeto
    def simbolo(caracter):
        if caracter == "+":
            return SIGMA["+"]
        if caracter == "-":
            return SIGMA["-"]
        if caracter.isdigit():
            return SIGMA["d"]
        return SIGMA["OTRO"]

    # Procesar cada carácter del lexema
    while indice < len(lexema) and estado_actual != 3:  # Estado muerto es 3
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    # Verificar si el estado final es de aceptación
    return estado_actual in F

