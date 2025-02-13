
def identificador(lexema):
    A, B, C, D, E, F, G, H, M = range(9)  # Definir estados
    Q0 = A  # Estado inicial
    Final = {B, C, D, E, F, G, H}  # Estado final

    SIGMA = {
        "K": 0,  #letra Mayuscula
        "L": 1, #letra minuscula
        "N": 2, # guion bajo
        "O": 3, # digito
        "OTRO": 4 # Otro caracter
    }

    DELTA = [
        #K  L  _  O
        [B, C, D, M], # Estado A (inicial)
        [B, C, D, E], # Estado B (letras)
        [F, G, H, M], # Estado C (dígitos)
        [F, G, H, M], # Estado D (guion bajo)
        [F, G, H, M], # Estado E (letras después de guion bajo)
        [F, G, H, M], # Estado F (dígitos después de guion bajo)
        [F, G, H, M], # Estado G (letras después de dígitos)
        [F, G, H, M], # Estado H (dígitos después de letras)
        [M, M, M, M], # Estado M (muerto)

    ]

    def simbolo(caracter):
        if caracter.isalpha():
            return SIGMA["K"]
        if caracter.isdigit():
            return SIGMA["L"]
        if caracter == "_":
            return SIGMA["N"]
        return SIGMA["O"]
    
    estado_actual = Q0
    indice = 0

    while indice < len(lexema) and estado_actual != M:  # Estado muerto
        estado_actual = DELTA[estado_actual][simbolo(lexema[indice])]
        indice += 1

    # Verificar si el estado final es de aceptación
    return estado_actual in Final


 
