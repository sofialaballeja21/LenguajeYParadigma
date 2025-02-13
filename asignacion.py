def operador_asignacion(lexema):
    es_operador_asignacion = ["+=", '=', "*=", "/=", "%=", "-=", "**=", "//="]

    return lexema in es_operador_asignacion