from Marca import Marca
class Automovil: 
    _contador = 0

    def __init__(self, dominio:str, marca: Marca,modelo:str,anio:int, kilometros:int,precio:float):
        Automovil._contador += 1
        self.numero = Automovil._contador
        self.dominio = dominio
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometros = kilometros
        self.precio = precio

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self,numero:int):
        if not isinstance(numero,int) or numero < 0:
            raise ValueError(f"Numero invalido: {numero}. El numero debe ser un numero entero. ")
        self.__numero = int(numero)
    
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self,anio:int):
        if not isinstance(anio,int):
            raise ValueError(f"Año invalido: {anio}. El año debe ser un numero entero.")
        self.__anio = int (anio)
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,precio:float):
        if not isinstance(precio, (int,float)) or precio <= 0:
            raise ValueError(f"Precio invalido: {precio}. El precio debe ser un numero positivo.")
        self.__precio = float(precio)

    @property
    def kilometros(self):
        return self._kilometros

    @kilometros.setter
    def kilometros(self, kilometros:int):
        if not isinstance(kilometros,int) or kilometros < 0:
            raise ValueError(f"Kilometros invalidos: {kilometros}. Los kilometros deben ser mayores o iguales a 0.")
        self.__kilometros = int(kilometros)
    def __str__(self):
        return f"Automovil(número: {self.numero}, dominio: {self.dominio}, marca: {self.marca}, modelo: {self.modelo}, año: {self.anio}, kilometros: {self.kilometros}, precio: {self.precio})"
    
    def __eq__(self,other):
        return isinstance(other,Automovil) and self.numero == other.numero          