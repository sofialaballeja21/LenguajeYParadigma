def es_numero_real(lexema):
    # Definir estados
    A, B, C, D, E, F, G, H, I, J, M = range(11)  # M es el estado muerto
    Q0 = A  # Estado inicial
    Final = {G, J}  

    
    SIGMA = {
        "-": 0,  
        "+": 1,  
        "d": 2,  
        ".": 3,  
        "e": 4,  # Exponente negativo
        "E": 5,  # Exponente positivo
        "OTRO": 6,  
    }


    DELTA = [
    #  -   +   d   .   e   E   OTRO
    [ B,  C,  D,  E,  M,  M,  M],  # Estado A (inicial)
    [ M,  M,  D,  E,  M,  M,  M],  # Estado B (-)
    [ M,  M,  D,  E,  M,  M,  M],  # Estado C (+)
    [ M,  M,  D,  F,  H,  I,  M],  # Estado D (dígitos)
    [ M,  M,  F,  M,  M,  M,  M],  # Estado E (punto decimal)
    [ M,  M,  G,  M,  H,  I,  M],  # Estado F (dígitos después del punto decimal)
    [ M,  M,  G,  M,  H,  I,  M],  # Estado G (más dígitos después del punto)
    [ J,  J,  J,  M,  M,  M,  M],  # Estado H (exponente negativo)
    [ M,  M,  J,  M,  M,  M,  M],  # Estado I (dígitos después del exponente positivo)
    [ M,  M,  J,  M,  M,  M,  M],  # Estado J (dígitos después del exponente negativo)
    [ M,  M,  M,  M,  M,  M,  M],  # Estado muerto (M)
]


    # Función para mapear caracteres a símbolos del alfabeto
    def simbolo(caracter):
        if caracter == "-":
            return SIGMA["-"]
        if caracter == "+":
            return SIGMA["+"]
        if caracter.isdigit():
            return SIGMA["d"]
        if caracter == ".":
            return SIGMA["."]
        if caracter == "e":
            return SIGMA["e"]  # Exponente negativo
        if caracter == "E":
            return SIGMA["E"]  # Exponente positivo
        return SIGMA["OTRO"]

    # Procesar cada carácter del lexema
    estado_actual = Q0
    indice = 0

    while indice < len(lexema) and estado_actual != M:  # Estado muerto
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    # Verificar si el estado final es de aceptación
    return estado_actual in Final

