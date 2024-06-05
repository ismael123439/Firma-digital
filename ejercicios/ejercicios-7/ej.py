from contextlib import contextmanager

@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    archivo = None
    try:
        archivo = open(ruta_archivo, modo)
        yield archivo
    finally:
        if archivo:
            archivo.close()

def leer_archivo(ruta_archivo):
    try:
        with gestionar_archivo(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
    except Exception as e:
        print(f"Error: Ocurrió un problema al leer el archivo: {e}")

def escribir_archivo(ruta_archivo, lineas):
    try:
        with gestionar_archivo(ruta_archivo, 'w') as archivo:
            for linea in lineas:
                archivo.write(linea + '\n')
    except Exception as e:
        print(f"Error: Ocurrió un problema al escribir en el archivo: {e}")

lineas_a_escribir = ["Línea 1", "Línea 2", "Línea 3"]
escribir_archivo('archivo_ejemplo.txt', lineas_a_escribir)

leer_archivo('archivo_ejemplo.txt')
