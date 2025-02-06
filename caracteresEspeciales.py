
def es_caracteresEspeciales(lexema):
    """
    Verifica si el lexema es un conjunto válido de caracteres especiales.
    Un lexema válido debe comenzar con una letra o guion bajo,
    y puede incluir letras, dígitos y guiones bajos.
    """
    if not lexema:
        return False

    # El primer carácter debe ser una letra o un guion bajo
    if not (lexema[0].isalpha() or lexema[0] == "_"):
        return False

    # Los caracteres restantes deben ser letras, dígitos o guiones bajos
    for caracter in lexema[1:]:
        if not (caracter.isalnum() or caracter == "_"):
            return False

    return True
