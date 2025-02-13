def palabra_reservada(lexema):
    es_palabra_reservada = ["def", "if", "import", "for", "while", "else", "elif", "return", "with", "as", "range", "in"]

    return lexema in es_palabra_reservada