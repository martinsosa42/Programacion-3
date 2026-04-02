
from Marca import Marca
from Automovil import Automovil
from funciones import ingresar_str,ingresar_int,ingresar_float

def main():
    Auto1 = Automovil("ABC123", Marca("Toyota"), "Corolla", 2020, 50000, 20000.0)
    print (Auto1)
    Auto2 = Automovil("DEF456", Marca("Honda"), "Civic", 2019, 30000, 22000.0)
    print (Auto2)

if __name__ == "__main__":
    main()