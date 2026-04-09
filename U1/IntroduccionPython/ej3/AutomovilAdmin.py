from Automovil import Automovil

class AutomovilAdmin:
    def __init__(self):
        self.__lista : list[Automovil] = []

    def agregar_automovil(self, auto : Automovil):
        if not isinstance(auto, Automovil):
            raise TypeError("Solo se pueden agregar Objetos de tipo Automovil.")
        if auto in self.__lista:
            raise ValueError("El auto ya existe en la lista.")
        
        self.__lista.append(auto)