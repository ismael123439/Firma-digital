def crear_listin():
    try:
        open("listin.txt", "x").close()
    except FileExistsError:
        print("El archivo listin.txt ya existe.")

def consultar_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    try:
        with open("listin.txt", "r") as archivo:
            for linea in archivo:
                cliente, telefono = linea.strip().split(',')
                if cliente == nombre:
                    print(f"Teléfono de {cliente}: {telefono}")
                    return
        print(f"No se encontró el teléfono del cliente {nombre}.")
    except FileNotFoundError:
        print("El archivo listin.txt no existe.")

def anadir_cliente():
    nombre = input("Introduce el nombre del nuevo cliente: ")
    telefono = input("Introduce el teléfono del nuevo cliente: ")
    with open("listin.txt", "a") as archivo:
        archivo.write(f"{nombre},{telefono}\n")

def eliminar_cliente():
    nombre = input("Introduce el nombre del cliente a eliminar: ")
    try:
        with open("listin.txt", "r") as archivo:
            lineas = archivo.readlines()
        with open("listin.txt", "w") as archivo:
            encontrado = False
            for linea in lineas:
                cliente, telefono = linea.strip().split(',')
                if cliente != nombre:
                    archivo.write(linea)
                else:
                    encontrado = True
            if encontrado:
                print(f"Cliente {nombre} eliminado.")
            else:
                print(f"No se encontró el cliente {nombre}.")
    except FileNotFoundError:
        print("El archivo listin.txt no existe.")

# Opciones de menú para probar las funciones
def menu():
    while True:
        print("\nListín Telefónico")
        print("1. Crear listín")
        print("2. Consultar teléfono")
        print("3. Añadir cliente")
        print("4. Eliminar cliente")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_listin()
        elif opcion == "2":
            consultar_telefono()
        elif opcion == "3":
            anadir_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()
