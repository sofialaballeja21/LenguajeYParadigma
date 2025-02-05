def es_valida(lexema):
    Q0 = 0  # Estado inicial
    Q = [0, 1]  # Conjunto de estados
    F = [1]  # Estado de aceptación
    
    estado_actual = Q0
    indice = 0

    # Definir alfabeto SIGMA
    SIGMA = {
        "K": 0,
        "L": 1,
        "N": 2,
        "O": 3,
        "OTRO": 4
    }

    # Tabla de transiciones DELTA
    DELTA = [
        [1, 1, 1, 3, 3],  # Transiciones de Q0
        [1, 1, 1, 1, 3],  # Transiciones de Q1
        [3, 3, 3, 3, 3],  # Transiciones del estado muerto Q3
    ]

    # Función para mapear caracteres a símbolos del alfabeto
    def simbolo(caracter):
        if caracter in SIGMA:
            return SIGMA[caracter]
        return SIGMA["OTRO"]

    # Procesar cada carácter del lexema
    while indice < len(lexema) and estado_actual != 3:  # Estado muerto es Q3
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    # Verificar si el estado final es de aceptación
    return estado_actual in F


