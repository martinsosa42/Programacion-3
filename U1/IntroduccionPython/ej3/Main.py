from Marca import Marca
from Automovil import Automovil
from AutomovilAdmin import AutomovilAdmin

def main():
    admin = AutomovilAdmin()
    Auto1 = Automovil("ABC123", Marca("Toyota"), "Corolla", 2020, 50000, 20000.0)

    Auto2 = Automovil("DEF456", Marca("Honda"), "Civic", 2019, 30000, 22000.0)

    Auto3 = Automovil("GHI789", Marca("Ford"), "Focus", 2021, 501000, 25000.0)

    Auto4 = Automovil("JKL012", Marca("Chevrolet"), "Cruze", 2018, 40000, 18000.0)

    Auto5 = Automovil("MNO345", Marca("Nissan"), "Sentra", 2022, 10000, 27000.0)

    admin.agregar_automovil(Auto1)
    admin.agregar_automovil(Auto2)
    admin.agregar_automovil(Auto3)
    admin.agregar_automovil(Auto4)
    admin.agregar_automovil(Auto5)

    for auto in admin._AutomovilAdmin__lista:
        print(auto)

if __name__ == "__main__":
    main()