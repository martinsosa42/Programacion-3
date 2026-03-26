from typing import List, Dict

from funciones import ingresar_str, ingresar_int, partidos_jugados, calcular_puntos

def main():
    lista:List[Dict] = []

    while True:
        nombre = ingresar_str("Ingrese el nombre de un equipo de fútbol: ")  
        partidos_ganados = ingresar_int("Ingrese el número de partidos ganados: ")
        partidos_empatados = ingresar_int("Ingrese el número de partidos empatados: ")
        partidos_perdidos = ingresar_int("Ingrese el número de partidos perdidos: ")
        partidos_totales = partidos_jugados(partidos_ganados, partidos_empatados, partidos_perdidos)
        puntos = calcular_puntos(partidos_ganados, partidos_empatados)

        equipo = {
            "nombre": nombre,
            "partidos_ganados": partidos_ganados,
            "partidos_empatados": partidos_empatados,
            "partidos_perdidos": partidos_perdidos,
            "partidos_totales": partidos_totales,
            "puntos": puntos
        }

        lista.append(equipo)
        continuar = input("¿Desea ingresar otro equipo? (s/n): ")
        if continuar.lower() != 's':
            break

    print("Todos los datos: ")
    for equipo in lista:
        print("a. El nombre del equipo es:", equipo["nombre"])
        print("b. El número de partidos ganados es:", equipo["partidos_ganados"])   
        print("c.1. El número de partidos empatados es:", equipo["partidos_empatados"])
        print("c.2. El número de partidos perdidos es:", equipo["partidos_perdidos"])
        print("d. El número de partidos jugados es:", equipo["partidos_totales"])
        print("e. El número de puntos es:", equipo["puntos"])
        
    sorted_lista = sorted(lista,key = lambda x:x["puntos"], reverse=True)
    print ("\n Equipos ordenados por puntos obtenidos (de mayor a menor): ")
    for equipo in sorted_lista:
        print(equipo["nombre"],"-",equipo["puntos"],"puntos"),

if __name__ == "__main__":
    main()