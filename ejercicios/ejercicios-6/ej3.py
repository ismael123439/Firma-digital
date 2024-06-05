def leer_linea_tabla():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debes introducir un número entero.")
    
    while True:
        try:
            m = int(input("Introduce otro número entero entre 1 y 10: "))
            if 1 <= m <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debes introducir un número entero.")
    
    try:
        with open(f"tabla-{n}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m-1].strip())
            else:
                print(f"El archivo tabla-{n}.txt no tiene {m} líneas.")
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

leer_linea_tabla()
