def es_numero_entero(lexema):
    A, B, C, D, M = range(5)  # Definir estados
    Q0 = A  
    Final = [D]

    estado_actual = Q0
    indice = 0

    SIGMA = {
        "+" : 0,
        "-" : 1,
        "d" : 2,
        "OTRO" : 3 
    }

    DELTA = [ 
        [B, C, D, M], # Estado A (inicial)
        [M, M, D, M], # Estado B (-)
        [M, M, D, M], # Estado C (+)
        [M, M, D, M], # Estado D (dígitos, permite más dígitos)
        [M, M, M, M], # Estado M (muerto)
    ]

    def simbolo(caracter):
        if caracter == "+":
            return SIGMA["+"]
        if caracter == "-":
            return SIGMA["-"]
        if caracter.isdigit():
            return SIGMA["d"]
        return SIGMA["OTRO"]
    
    while indice < len(lexema) and estado_actual != M:
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    return estado_actual in Final

