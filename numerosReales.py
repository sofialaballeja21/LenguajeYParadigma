def es_numero_real(lexema):
    Q0 = 0  # Estado inicial
    Q = [0, 1, 2, 3, 4, 5, 6, 7]  # Conjunto de estados
    F = [3, 6]  # Estados de aceptación (números reales válidos)
    
    estado_actual = Q0
    indice = 0

    # Definir alfabeto SIGMA
    SIGMA = {
        "+": 0,
        "-": 1,
        "d": 2,
        ".": 3,
        "e": 4,
        "E": 5,
        "OTRO": 6,
    }

    # Tabla de transiciones DELTA
    DELTA = [
        [2, 2, 7, 7, 7, 7, 7],  # Transiciones de A (estado 0)
        [7, 7, 7, 7, 7, 7, 7],  # Transiciones de B (estado 1)
        [7, 7, 7, 6, 7, 7, 7],  # Transiciones de C (estado 2)
        [7, 7, 7, 7, 7, 7, 7],  # Transiciones de D (estado 3)
        [7, 7, 7, 7, 7, 7, 7],  # Transiciones de E (estado 4)
        [7, 7, 7, 7, 7, 7, 7],  # Transiciones de F (estado 5)
        [7, 7, 7, 7, 7, 7, 7],  # Transiciones de G (estado 6)
        [7, 7, 7, 7, 7, 7, 7],  # Estado muerto (7)
    ]

    # Función para mapear caracteres a símbolos del alfabeto
    def simbolo(caracter):
        if caracter in SIGMA:
            return SIGMA[caracter]
        if caracter.isdigit():  # Reconoce cualquier dígito como "d"
            return SIGMA["d"]
        return SIGMA["OTRO"]

    # Procesar cada carácter del lexema
    while indice < len(lexema) and estado_actual != 7:  # Estado muerto es 7
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    # Verificar si el estado final es de aceptación
    return estado_actual in F
