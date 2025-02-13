'''from identificador import identificador
from aritmeticos import operador_aritmetico
from asignacion import operador_asignacion
from enteros import es_numero_entero
from logicos import operadores_logicos
from numerosReales import es_numero_real
from puntuacion import simbolo_de_puntuacion
from relacionales import relacionales
from reservadas import palabra_reservada
from es_string import es_string'''

import aritmeticos
import asignacion
import enteros
import es_string
import identificador
import logicos
import puntuacion
import relacionales
import numerosReales
import reservadas

def analizar_lexicamente(lexema):
    if es_string.es_string(lexema):
        return f"El lexema '{lexema[1:-1]}' es un string."
    else:
        if numerosReales.es_numero_real(lexema):
            return f"El lexema '{lexema}' es un número real."
        elif enteros.es_numero_entero(lexema):
            return f"El lexema '{lexema}' es un número entero."
        elif reservadas.palabra_reservada(lexema):
            return f"El lexema '{lexema}' es una palabra reservada."
        elif identificador.identificador(lexema):
            return f"El lexema '{lexema}' es un identificador."
        elif aritmeticos.operador_aritmetico(lexema):
            return f"El lexema '{lexema}' es un operador aritmético."
        elif asignacion.operador_asignacion(lexema):
            return f"El lexema '{lexema}' es un operador de asignación."
        elif relacionales.relacionales(lexema):
            return f"El lexema '{lexema}' es un operador relacional."
        elif logicos.operadores_logicos(lexema):
            return f"El lexema '{lexema}' es un operador lógico."
        elif puntuacion.simbolo_de_puntuacion(lexema):
            return f"El lexema '{lexema}' es un símbolo de puntuación."
        else:
            return f"El lexema '{lexema}' es un operador desconocido. Error."

def main():
    archivo = input("Ingrese el nombre del archivo: ")
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                lexemas = linea.strip().split()
                for lexema in lexemas:
                    print(analizar_lexicamente(lexema))
    except FileNotFoundError:
        print("Error: No se encontró el archivo especificado.")

if __name__ == "__main__":
    main()
