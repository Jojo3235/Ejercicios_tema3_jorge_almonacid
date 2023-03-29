import time 


class nodoPila(object):
    info, sig = None, None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.size = 0

    def apilar(pila, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.cima = nodo
        pila.size += 1

    def desapilar(pila):
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.size -= 1
        return x
    
    def pila_vacia(pila):
        return pila.cima is None
    
    def en_cima(pila):
        if pila.cima.info:
            return pila.cima.info
        else:
            return None
        
    def size(pila):
        return pila.size
    
    def barrido(pila):
        paux = Pila()
        while not Pila.pila_vacia(pila):
            dato = Pila.desapilar(pila)
            print(dato)
            Pila.apilar(paux, dato)
        while not paux.pila_vacia():
            dato = Pila.desapilar(paux)
            Pila.apilar(pila, dato)

class TorresHanoi(object):
    def __init__(self):
        self.torres = [Pila(), Pila(), Pila()]
        self.movimientos = 0
    
    def agregar_disco(hanoi, disco, torre):
        Pila.apilar(hanoi.torres[torre], disco)
    
    def mover_disco(hanoi, torre_origen, torre_destino):
        disco = Pila.desapilar(hanoi.torres[torre_origen])
        Pila.apilar(hanoi.torres[torre_destino], disco)
        hanoi.movimientos += 1
    
    def resolver(hanoi, n, torre_origen, torre_auxiliar, torre_destino):
        if n == 1:
            hanoi.mover_disco(torre_origen, torre_destino)
        else:
            hanoi.resolver(n - 1, torre_origen, torre_destino, torre_auxiliar)
            hanoi.mover_disco(torre_origen, torre_destino)
            hanoi.resolver(n - 1, torre_auxiliar, torre_origen, torre_destino)
    
    def mostrar(hanoi):
        for i in range(0, 3):
            print("Torre", i)
            Pila.barrido(hanoi.torres[i])
            print("")
        print("Movimientos:", hanoi.movimientos)

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            return numero
        except ValueError:
            print("El valor ingresado no es un numero")

def main():
    hanoi = TorresHanoi()
    n = pedir_numero()
    start = time.time()
    for i in range(n, 0, -1):
        hanoi.agregar_disco(i, 0)
    hanoi.resolver(n, 0, 1, 2)
    hanoi.mostrar()
    end = time.time()
    print("Tiempo de ejecucion: ", end - start)


if __name__ == "__main__":
    main()
