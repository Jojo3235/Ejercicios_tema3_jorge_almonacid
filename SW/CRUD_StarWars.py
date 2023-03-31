# Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

#  realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;

# mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
# determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
# indicar cuál es la nave que requiere mayor cantidad de tripulación;
# mostrar todas las naves que comienzan con AT;
# listar todas las naves que pueden llevar seis o más pasajeros;
#  mostrar toda la información de la nave más pequeña y la más grande

import csv
from config import DATABASE_PATH
import math

class Nodo:
    def __init__(self, info):
        self.info = info
        self.sig = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def agregar(self, info):
        nodo = Nodo(info)
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            self.ultimo.sig = nodo
            self.ultimo = nodo
        self.size += 1

    def mostrar(self):
        aux = self.primero
        while aux is not None:
            print(aux.info)
            aux = aux.sig

    def buscar(self, info):
        aux = self.primero
        while aux is not None:
            if aux.info == info:
                return aux
            aux = aux.sig
        return None
    
    def eliminar(self, info):
        aux = self.primero
        anterior = None
        while aux is not None:
            if aux.info == info:
                if anterior is None:
                    self.primero = aux.sig
                else:
                    anterior.sig = aux.sig
                self.size -= 1
                return aux
            anterior = aux
            aux = aux.sig
        return None
    

class Nave:
    def __init__(self, nombre, tripulacion, pasajeros, largo):
        self.nombre = nombre
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros
        self.largo = largo

    def __str__(self):
        return f"Nombre: {self.nombre} - Tripulacion: {self.tripulacion} - Pasajeros: {self.pasajeros} - Largo: {self.largo}"

class ControlNaves:
    def __init__(self):
        self.naves = ListaEnlazada()
        self.cargar_datos()

    def cargar_datos(self):
        with open(DATABASE_PATH, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                largo = row[4]
                tripulacion = row[6]
                pasajeros = row[7]
                nave = Nave(row[0], tripulacion, pasajeros, largo)
                self.naves.agregar(nave)

    def mostrar_naves(self):
        self.naves.mostrar()

    def mostrar_naves_ordenadas(self):
        naves_ordenadas = self.naves
        naves_ordenadas.primero = self.merge_sort(naves_ordenadas.primero)
        naves_ordenadas.mostrar()

    def mostrar_nave(self, nombre):
        aux = self.naves.primero
        while aux is not None:
            if aux.info.nombre == nombre:
                print(aux.info)
            aux = aux.sig

    def merge_sort(self, lista):
        if lista is None or lista.sig is None:
            return lista
        medio = self.get_middle(lista)
        siguiente_medio = medio.sig
        medio.sig = None
        izquierda = self.merge_sort(lista)
        derecha = self.merge_sort(siguiente_medio)
        return self.merge(izquierda, derecha)
    
    def get_middle(self, lista):
        if lista is None:
            return lista
        slow = lista
        fast = lista
        while fast.sig is not None and fast.sig.sig is not None:
            slow = slow.sig
            fast = fast.sig.sig
        return slow
    
    def merge(self, izquierda, derecha):
        if izquierda is None:
            return derecha
        if derecha is None:
            return izquierda
        resultado = None
        if izquierda.info.nombre < derecha.info.nombre:
            resultado = izquierda
            resultado.sig = self.merge(izquierda.sig, derecha)
        else:
            resultado = derecha
            resultado.sig = self.merge(izquierda, derecha.sig)
        return resultado

    def mostrar_naves_con_mas_pasajeros(self, cantidad_naves):
        naves_ordenadas = self.naves
        naves_ordenadas.primero = self.merge_sort(naves_ordenadas.primero)
        aux = naves_ordenadas.primero
        for i in range(cantidad_naves):
            print(aux.info)
            aux = aux.sig

    def nave_con_mas_tripulacion(self):
        naves_ordenadas = self.naves
        naves_ordenadas.primero = self.merge_sort(naves_ordenadas.primero)
        print(naves_ordenadas.primero.info)

    def mostrar_naves_con_AT(self):
        aux = self.naves.primero
        while aux is not None:
            if aux.info.nombre.startswith("AT"):
                print(aux.info)
            aux = aux.sig

    def mostrar_naves_con_mas_pasajeros_que(self, cantidad):
        aux = self.naves.primero
        while aux is not None:
            if int(aux.info.pasajeros) > cantidad:
                print(aux.info)
            aux = aux.sig

    def nave_mas_grande(self):
        aux = self.naves.primero
        nave_mas_grande = aux.info
        while aux is not None:
            if aux.info.largo < nave_mas_grande.largo:
                nave_mas_grande = aux.info
            aux = aux.sig
        print(nave_mas_grande)

    def nave_mas_pequena(self):
        aux = self.naves.primero
        nave_mas_pequena = aux.info
        while aux is not None:
            if aux.info.largo > nave_mas_pequena.largo:
                nave_mas_pequena = aux.info
            aux = aux.sig
        print(nave_mas_pequena)


        

if __name__ == "__main__":
    control = ControlNaves()
    control.mostrar_naves()
    control.mostrar_nave("Millennium Falcon")
    control.mostrar_nave("Death Star")
    control.mostrar_naves_con_mas_pasajeros(5)
    control.nave_con_mas_tripulacion()
    control.mostrar_naves_con_AT()
    # control.mostrar_naves_con_mas_pasajeros_que(6)
    control.nave_mas_pequena()
    control.nave_mas_grande()
