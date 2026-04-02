from funciones import suma_lista, filtrar_menores, valores, unicos_set, unicos_dict1, unicos_dict2, unicos_dict3, histograma


def main():
    lista = [2,6,3,5,6,2,9,1,6,]
    texto = """ Estas aplicaciones manejan grandes cantidades de texto para realizar clasificaciones o traducciones, 
    lo que implica un gran trabajo de procesamiento. 
    Transformar texto en algo que un algoritmo pueda procesar es un proceso complejo. En este artículo, analizaremos los pasos 
    involucrados en el procesamiento de texto. """
    print(f"El resultado de la suma de la lista es: {suma_lista(lista)}")
    print(f"Los numeros menores a 5 en la lista son: {filtrar_menores(lista, 5)}")
    print(f"El menor, central y mayor de la lista son: {valores(lista)}")
    print(f"Unicos set: {unicos_set(lista)}")
    print(f"Unicos dict1: {unicos_dict1(lista)}")
    print(f"Unicos dict2: {unicos_dict2(lista)}")
    print(f"Unicos dict3: {unicos_dict3(lista)}")
    print(f"Histograma: ",histograma(texto))

if __name__=="__main__":
    main()    