'''salida = ()
with open('Prueba.txt', "r") as f :
    lineas = [lineas.split() for lineas in f]


for linea in lineas:
    print(linea)'''
    

    #pasa el archivo en formato txt a una lista de listas


from identificador import identificador
from aritmeticos import operador_aritmetico
from asignacion import operador_asignacion
from enteros import es_numero_entero
from logicos import operadores_logicos
from numerosReales import es_numero_real
from puntuacion import simbolo_de_puntuacion
from relacionales import relacionales
from reservadas import palabra_reservada


def main(ruta_archivo):
    salida = []

    try:
        with open(ruta_archivo, "r") as file: 
            lineas = [lineas.split() for lineas in  file]

            for i, linea in enumerate(lineas):
                #print(i, linea)
                #for lexema in linea: 
                if es_numero_entero(linea):
                   print( salida.append((i, linea, "Número entero válido")))
                '''elif es_numero_real(lexema):
                        salida.append((i, lexema, "Número real válido"))
                    elif relacionales(lexema):
                        salida.append((i, lexema, "Operador relacional"))
                    elif operador_aritmetico(lexema):
                        salida.append((i, lexema, "Operador aritmético"))
                    elif operador_asignacion(lexema):
                        salida.append((i, lexema, "Operador de asignación"))
                    elif operadores_logicos(lexema):
                        salida.append((i, lexema, "Operador lógico"))
                    elif palabra_reservada(lexema):
                        salida.append((i, lexema, "Palabra reservada"))
                    elif simbolo_de_puntuacion(lexema):
                        salida.append((i, lexema, "Símbolo de puntuación"))
                    elif identificador(lexema):
                        salida.append((i, lexema, "Identificador válido"))
                    else:
                        salida.append((i, lexema, "No pertenece a ningún lenguaje definido"))'''
        
        for item in salida:
            print(f"Línea {item[0]}: '{item[1]}' -> {item[2]}")       
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    ruta_archivo = input("Ingresa la ruta del archivo a procesar: ")
    main(ruta_archivo)

