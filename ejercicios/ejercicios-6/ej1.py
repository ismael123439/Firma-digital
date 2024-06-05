def guardar_tabla():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debes introducir un número entero.")
    
    with open(f"tabla-{n}.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")

guardar_tabla()
