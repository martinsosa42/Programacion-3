def calcular_puntos(p_ganados,p_empatados):
    return (p_ganados * 3) + p_empatados

def partidos_jugados(p_ganados, p_perdidos, p_empatados):
    return p_ganados + p_perdidos + p_empatados

def ingresar_str(cadena : str) -> str:
    while True:
        valor = input(cadena)
        if valor.strip():  # Verifica que no sea una cadena vacía
            return valor
        else:
            print("Error: No se puede ingresar una cadena vacía.")

def ingresar_int(cadena : str) -> int:
    while True: 
        valor = input(cadena)
        if valor.isdigit():  # Verifica que el valor ingresado sea un número entero
            return int(valor)
        else:
            print("Error: Por favor, ingrese un número entero válido.")

def main():
    nombre = ingresar_str("Ingrese el nombre de un equipo de futbol: ") 
    partidos_ganados = ingresar_int("Ingrese el numero de partidos ganados: ")
    partidos_empatados = ingresar_int("Ingrese el numero de partidos empatados: ")
    partidos_perdidos = ingresar_int("Ingrese el numero de partidos perdidos: ")

    print ("a. El nombre del equipo es: ",nombre)
    print ("b. El numero de partidos ganados es: ",partidos_ganados)
    print("c.1. El numero de partidos empatados es: ",partidos_empatados)
    print("c.2. El numero de partidos perdidos es: ",partidos_perdidos)

    print("d. El numero total de partidos jugados es: ",partidos_jugados(partidos_ganados, partidos_perdidos, partidos_empatados))
    print("e. El numero de puntos obtenidos es: ",calcular_puntos(partidos_ganados, partidos_empatados))

if __name__ == "__main__":    
    main()
