from Marca import Marca
class Automovil: 
    numero = 0

    def __init__(self, dominio:str, marca: Marca,modelo:str,anio:int, kilometros:int,precio:float):
        Automovil.numero += 1
        self.numero = Automovil.numero
        self.dominio = dominio
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometros = kilometros
        self.precio = precio

    def __str__(self):
        return f"Automovil(número: {self.numero}, dominio: {self.dominio}, marca: {self.marca}, modelo: {self.modelo}, año: {self.anio}, kilometros: {self.kilometros}, precio: {self.precio})"
    
    def __eq__(self,other):
        return isinstance(other,Automovil) and self.numero == other.numero          