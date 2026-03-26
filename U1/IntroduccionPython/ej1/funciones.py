from typing import List, Dict

def calcular_puntos(ganados: int, empatados: int) -> int:
    return (ganados * 3) + empatados

def partidos_jugados(ganados: int, empatados:int, perdidos:int):
    return ganados + perdidos + empatados

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