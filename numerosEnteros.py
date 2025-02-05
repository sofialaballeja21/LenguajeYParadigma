def es_numero_entero(lexema):
    Q0 = 0  # Estado inicial
    Q = [0, 1, 2, 3, 4]  # Conjunto de estados
    F = [3]  # Estados de aceptación (números enteros válidos)
    
    estado_actual = Q0
    indice = 0

    # Definir alfabeto SIGMA
    SIGMA = {
        "+": 0,
        "-": 1,
        "d": 2,
        "OTRO": 3
    }

    # Tabla de transiciones DELTA
    DELTA = [
        [2, 2, 4, 4],  # Transiciones de A (estado 0)
        [4, 4, 3, 4],  # Transiciones de B (estado 1)
        [4, 4, 3, 4],  # Transiciones de C (estado 2)
        [4, 4, 3, 4],  # Transiciones de D (estado 3)
        [4, 4, 4, 4],  # Transiciones del estado muerto (estado 4)
    ]

    # Función para mapear caracteres a símbolos del alfabeto
    def simbolo(caracter):
        if caracter in SIGMA:
            return SIGMA[caracter]
        if caracter.isdigit():  # Reconoce cualquier dígito como "d"
            return SIGMA["d"]
        return SIGMA["OTRO"]

    # Procesar cada carácter del lexema
    while indice < len(lexema) and estado_actual != 4:  # Estado muerto es 4
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    # Verificar si el estado final es de aceptación
    return estado_actual in F
