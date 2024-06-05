import csv
from datetime import datetime
from collections import defaultdict

def leer_fixture(nombre_archivo):
    partidos = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['Date'] = datetime.strptime(row['Date'], '%d/%m/%Y %H:%M')
                partidos.append(row)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
    except csv.Error:
        print(f"Error: El archivo {nombre_archivo} tiene un formato incorrecto.")
    return partidos

def actualizar_resultados(nombre_archivo_resultados, partidos, equipos):
    try:
        with open(nombre_archivo_resultados, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match_number = int(row['Match Number'])
                home_goals = int(row['Home Team Goals'])
                away_goals = int(row['Away Team Goals'])

                partido = next(p for p in partidos if int(p['Match Number']) == match_number)
                home_team = partido['Home Team']
                away_team = partido['Away Team']

                # Actualizar resultados para el equipo local
                equipos[home_team]['PartidosJugados'] += 1
                equipos[home_team]['GolesAFavor'] += home_goals
                equipos[home_team]['GolesEnContra'] += away_goals
                equipos[home_team]['DiferenciaDeGoles'] += (home_goals - away_goals)
                
                # Actualizar resultados para el equipo visitante
                equipos[away_team]['PartidosJugados'] += 1
                equipos[away_team]['GolesAFavor'] += away_goals
                equipos[away_team]['GolesEnContra'] += home_goals
                equipos[away_team]['DiferenciaDeGoles'] += (away_goals - home_goals)

                if home_goals > away_goals:
                    equipos[home_team]['Victorias'] += 1
                    equipos[home_team]['Puntos'] += 3
                    equipos[away_team]['Derrotas'] += 1
                elif home_goals < away_goals:
                    equipos[away_team]['Victorias'] += 1
                    equipos[away_team]['Puntos'] += 3
                    equipos[home_team]['Derrotas'] += 1
                else:
                    equipos[home_team]['Empates'] += 1
                    equipos[away_team]['Empates'] += 1
                    equipos[home_team]['Puntos'] += 1
                    equipos[away_team]['Puntos'] += 1
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo_resultados} no se encontró.")
    except csv.Error:
        print(f"Error: El archivo {nombre_archivo_resultados} tiene un formato incorrecto.")

def calcular_posiciones(grupos, equipos):
    posiciones = {}
    for grupo, equipos_grupo in grupos.items():
        posiciones_grupo = sorted(equipos_grupo, key=lambda equipo: (
            equipos[equipo]['Puntos'], 
            equipos[equipo]['DiferenciaDeGoles'], 
            equipos[equipo]['GolesAFavor']), reverse=True)
        posiciones[grupo] = posiciones_grupo
    return posiciones

def generar_informe_final(nombre_archivo_salida, posiciones, equipos):
    try:
        with open(nombre_archivo_salida, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Grupo', 'Equipo', 'Puntos', 'PartidosJugados', 'Victorias', 'Empates', 'Derrotas', 'GolesAFavor', 'GolesEnContra', 'DiferenciaDeGoles']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for grupo, equipos_grupo in posiciones.items():
                for equipo in equipos_grupo:
                    equipo_data = equipos[equipo]
                    writer.writerow({
                        'Grupo': grupo,
                        'Equipo': equipo,
                        'Puntos': equipo_data['Puntos'],
                        'PartidosJugados': equipo_data['PartidosJugados'],
                        'Victorias': equipo_data['Victorias'],
                        'Empates': equipo_data['Empates'],
                        'Derrotas': equipo_data['Derrotas'],
                        'GolesAFavor': equipo_data['GolesAFavor'],
                        'GolesEnContra': equipo_data['GolesEnContra'],
                        'DiferenciaDeGoles': equipo_data['DiferenciaDeGoles']
                    })
    except FileNotFoundError:
        print(f"Error: No se pudo crear el archivo {nombre_archivo_salida}.")
    except csv.Error:
        print(f"Error: Ocurrió un problema al escribir en el archivo {nombre_archivo_salida}.")

def main():
    partidos = leer_fixture('copa-america-2024-UTC.csv')
    
    equipos = defaultdict(lambda: {'Puntos': 0, 'PartidosJugados': 0, 'Victorias': 0, 'Empates': 0, 'Derrotas': 0, 'GolesAFavor': 0, 'GolesEnContra': 0, 'DiferenciaDeGoles': 0})
    grupos = defaultdict(list)

    for partido in partidos:
        grupo = partido['Group']
        if partido['Home Team'] not in grupos[grupo]:
            grupos[grupo].append(partido['Home Team'])
        if partido['Away Team'] not in grupos[grupo]:
            grupos[grupo].append(partido['Away Team'])

    actualizar_resultados('resultados.csv', partidos, equipos)
    posiciones = calcular_posiciones(grupos, equipos)
    generar_informe_final('informe_final.csv', posiciones, equipos)

if __name__ == "__main__":
    main()
