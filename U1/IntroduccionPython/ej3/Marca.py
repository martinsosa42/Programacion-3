class Marca: 
    def __init__(self,nombre:str):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
    
    def __eq__(self,other):
        return isinstance(other, Marca) and self.nombre == other.nombre 