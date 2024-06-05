def leer_tabla():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debes introducir un número entero.")
    
    try:
        with open(f"tabla-{n}.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

leer_tabla()
