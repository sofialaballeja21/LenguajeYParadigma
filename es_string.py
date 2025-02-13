
def es_string(lexema: str) -> bool:
    if ((lexema[0] == '"' and lexema[-1] == '"') or (lexema[0] == "'" and lexema[-1] == "'")) and len(lexema) > 2:
        return True
    return False