from caracteresEspeciales import es_caracteresEspeciales
from numerosEnteros import es_numero_entero
from numerosReales import es_numero_real

def leer_archivo(ruta_archivo):
    """
    Lee un archivo y procesa cada línea para verificar si pertenece al lenguaje definido
    por caracteres especiales, números enteros o números reales.
    """
    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
            for i, linea in enumerate(lineas, start=1):
                lexema = linea.strip()  # Quita espacios en blanco o saltos de línea
                
                # Verifica si el lexema es válido en alguno de los lenguajes definidos
                if es_numero_entero(lexema):
                    print(f"Línea {i}: '{lexema}' es un número entero válido.")
                elif es_numero_real(lexema):
                    print(f"Línea {i}: '{lexema}' es un número real válido.")
                elif es_caracteresEspeciales(lexema):
                    print(f"Línea {i}: '{lexema}' es un conjunto válido de caracteres especiales.")
                else:
                    print(f"Línea {i}: '{lexema}' no pertenece a ningún lenguaje definido.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
if __name__ == "__main__":
    
    ruta_archivo = input("Ingresa la ruta del archivo a procesar: ")
    leer_archivo(ruta_archivo)
