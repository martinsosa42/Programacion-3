from collections import Counter

def suma_lista(lista : list[int]):
    if not isinstance(lista,list):
        raise TypeError("El argumento debe ser una lista.")
    
    for num in lista:
        if not isinstance(num,int):
            raise TypeError("Hay un elemento de la lista que no es un entero")
    return sum(lista)

def filtrar_menores(lista : list[int], k : int):
    if not isinstance(lista,list):
        raise TypeError("El argumento debe ser una lista.")
        
    for num in lista:
        if not isinstance(num,int):
            raise TypeError("Hay un elemento de la lista que no es un entero")
            
    return [num for num in lista if num < k]

def valores(lista : list[int]):
    if not isinstance(lista,list):
        raise TypeError("El argumento debe ser una lista. ")
    
    for num in lista: 
        if not isinstance(num,int):
            raise TypeError("Hay un elemento de la lista que no es un entero")
        
        ordenada = sorted(lista)
        menor = ordenada[0]
        mayor = ordenada[-1]
        mid = len(ordenada) // 2
        
        if len(ordenada) % 2 == 0:
            central = ordenada[mid-1], ordenada[mid]
        else:
            central = ordenada[mid]

    return menor, central, mayor 
    
def unicos_set(lista : list[int]) -> list[int]:
    if not isinstance(lista,list):
        raise TypeError("El argumento debe ser una lista. ")
    
    for num in lista: 
        if not isinstance(num,int):
            raise TypeError("Hay un elemento de la lista que no es un entero")
        
    return list(set(lista))

#1 clase
def unicos_dict1(lista: list[int]) -> list[int]:
    diccionario : dict[int, int]= {}
    for aux in lista:
        diccionario[aux] = aux
    
    print(diccionario)

    res = []
    for k in diccionario.keys():
        res.append(k)

    return res

#2 clase
def unicos_dict2(lista : list[int]) -> list[int]:
    return list({x: None for x in lista}.keys())

#3 otra forma que no dimos en clase
def unicos_dict3(lista : list[int]) -> list[int]:
    return list(dict.fromkeys(lista))
    
def histograma (texto : str) -> dict[str, int]:
    return Counter(texto.lower())