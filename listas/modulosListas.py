'''
Created on 30 nov. 2016

@author: usuario
'''
def crearLista(lista): 
    '''

        voy a hacer una lista donde incluya una serie de elemenetos
    '''
    try:
        elemento=int(input("introducir un elemento"))
        lista.append(elemento)
    except:
        elemento=input("introducir elemento")
        lista.append(elemento)
        
def imprimirLista (lista):
    try:
        for indice in lista:
            print(indice)
    except:
        print("alerta de bomba")
if __name__=="__main__":
    l=[]
    crearLista(l)
    imprimirLista(l)