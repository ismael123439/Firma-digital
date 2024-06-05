class JugadorFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numero_camiseta):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
        self.pais = pais
        self.numero_camiseta = numero_camiseta
        self.goles_marcados = 0
        self.asistencias = 0
        self.tarjetas_amarillas = 0
        self.tarjetas_rojas = 0
        self.premios = []

    def actualizar_informacion(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Atributo {key} no válido")

    def calcular_promedio_goles(self):
        total_partidos = 1 
        return self.goles_marcados / total_partidos

    def es_goleador(self):
        return self.goles_marcados > 10  

    def agregar_premio(self, premio):
        self.premios.append(premio)

    def eliminar_premio(self, premio):
        if premio in self.premios:
            self.premios.remove(premio)
        else:
            print(f"{premio} no encontrado en la lista de premios")

    def actualizacion_estadisticas(self):
        print("Estadísticas actualizadas")

def mostrar_menu():
    print("\nMenu:")
    print("1. Crear nuevo jugador")
    print("2. Mostrar información de un jugador")
    print("3. Actualizar información de un jugador")
    print("4. Calcular promedio de goles por partido")
    print("5. Verificar si un jugador es goleador")
    print("6. Agregar premio a un jugador")
    print("7. Eliminar premio de un jugador")
    print("8. Salir")

def main():
    jugadores = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del jugador: ")
            edad = int(input("Edad del jugador: "))
            posicion = input("Posición del jugador: ")
            equipo = input("Equipo actual del jugador: ")
            pais = input("País de origen del jugador: ")
            numero_camiseta = input("Número de camiseta del jugador: ")
            jugador = JugadorFutbol(nombre, edad, posicion, equipo, pais, numero_camiseta)
            jugadores.append(jugador)
            print("¡Jugador creado!")

        elif opcion == "2":
            if jugadores:
                for i, jugador in enumerate(jugadores):
                    print(f"{i+1}. {jugador.nombre}")
                index = int(input("Seleccione el número de jugador para mostrar su información: ")) - 1
                print(vars(jugadores[index]))
            else:
                print("No hay jugadores creados")

        elif opcion == "3":
            if jugadores:
                for i, jugador in enumerate(jugadores):
                    print(f"{i+1}. {jugador.nombre}")
                index = int(input("Seleccione el número de jugador para actualizar su información: ")) - 1
                atributo = input("Atributo a actualizar: ")
                valor = input("Nuevo valor: ")
                jugadores[index].actualizar_informacion(**{atributo: valor})
                print("¡Información actualizada!")
            else:
                print("No hay jugadores creados")

        elif opcion == "4":
            if jugadores:
                for i, jugador in enumerate(jugadores):
                    print(f"{i+1}. {jugador.nombre}")
                index = int(input("Seleccione el número de jugador para calcular su promedio de goles: ")) - 1
                promedio_goles = jugadores[index].calcular_promedio_goles()
                print(f"Promedio de goles por partido: {promedio_goles}")
            else:
                print("No hay jugadores creados")

        elif opcion == "5":
            if jugadores:
                for i, jugador in enumerate(jugadores):
                    print(f"{i+1}. {jugador.nombre}")
                index = int(input("Seleccione el número de jugador para verificar si es goleador: ")) - 1
                if jugadores[index].es_goleador():
                    print("El jugador es un goleador")
                else:
                    print("El jugador no es un goleador")
            else:
                print("No hay jugadores creados")

        elif opcion == "6":
            if jugadores:
                for i, jugador in enumerate(jugadores):
                    print(f"{i+1}. {jugador.nombre}")
                index = int(input("Seleccione el número de jugador para agregar un premio: ")) - 1
                premio = input("Premio a agregar: ")
                jugadores[index].agregar_premio(premio)
                print("Premio agregado exitosamente")
            else:
                print("No hay jugadores creados")

        elif opcion == "7":
            if jugadores:
                for i, jugador in enumerate(jugadores):
                    print(f"{i+1}. {jugador.nombre}")
                index = int(input("Seleccione el número de jugador para eliminar un premio: ")) - 1
                premio = input("Premio a eliminar: ")
                jugadores[index].eliminar_premio(premio)
                print("Premio eliminado exitosamente")
            else:
                print("No hay jugadores creados")

        elif opcion == "8":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
