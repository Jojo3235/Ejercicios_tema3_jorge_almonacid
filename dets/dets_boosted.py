class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(lista, val):
        new_node = Node(val)
        if lista.head is None:
            lista.head = new_node
        else:
            current_node = lista.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def get(lista, index):
        current_node = lista.head
        for i in range(index):
            current_node = current_node.next
        return current_node.val

    def set(lista, index, val):
        current_node = lista.head
        for i in range(index):
            current_node = current_node.next
        current_node.val = val

    def remove(lista, index):
        if index == 0:
            lista.head = lista.head.next
        else:
            current_node = lista.head
            for i in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next

    def __str__(self):
        current_node = self.head
        values = []
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return str(values)
    

class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = []
        for i in range(m):
            row = LinkedList()
            for j in range(n):
                row.insert(None)
            self.matrix.append(row)

    def set_value(matrix, i, j, value):
        matrix.matrix[i].set(j, value)

    def get_value(matrix, i, j):
        return matrix.matrix[i].get(j)

    def print_matrix(matrix):
        for i in range(matrix.m):
            row = ''
            for j in range(matrix.n):
                row += str(matrix.get_value(i, j)) + ' '
            print(row)
    
    def strassen_determinante(matrix):
        if matrix.m != matrix.n:
            raise ValueError("La matriz debe ser cuadrada")
        if matrix.m == 1:
            return matrix.get_value(0, 0)
        if matrix.m == 2:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0)
        if matrix.m == 3:
            return matrix.get_value(0, 0) * matrix.get_value(1, 1) * matrix.get_value(2, 2) + matrix.get_value(0, 1) * matrix.get_value(1, 2) * matrix.get_value(2, 0) + matrix.get_value(0, 2) * matrix.get_value(1, 0) * matrix.get_value(2, 1) - matrix.get_value(0, 2) * matrix.get_value(1, 1) * matrix.get_value(2, 0) - matrix.get_value(0, 0) * matrix.get_value(1, 2) * matrix.get_value(2, 1) - matrix.get_value(0, 1) * matrix.get_value(1, 0) * matrix.get_value(2, 2)
        else:
            a = Matrix(matrix.m // 2, matrix.n // 2)
            b = Matrix(matrix.m // 2, matrix.n // 2)
            c = Matrix(matrix.m // 2, matrix.n // 2)
            d = Matrix(matrix.m // 2, matrix.n // 2)
            for i in range(matrix.m // 2):
                for j in range(matrix.n // 2):
                    a.set_value(i, j, matrix.get_value(i, j))
                    b.set_value(i, j, matrix.get_value(i, j + matrix.n // 2))
                    c.set_value(i, j, matrix.get_value(i + matrix.m // 2, j))
                    d.set_value(i, j, matrix.get_value(i + matrix.m // 2, j + matrix.n // 2))
            p1 = Matrix.strassen_determinante(a)
            p2 = Matrix.strassen_determinante(b)
            p3 = Matrix.strassen_determinante(c)
            p4 = Matrix.strassen_determinante(d)
            return p1 * p4 - p2 * p3
        
def pedir_tamaño_mat():
    while True:
        try:
            num = int(input("Ingrese el tamaño de la matriz: "))
            if num < 1:
                print("El tamaño de la matriz debe ser mayor o igual a 1")
            else:
                return num
        except ValueError:
            print("El tamaño de la matriz debe ser un número entero")

def pedir_numero():
    while True:
        try:
            num = int(input("Ingrese un número: "))
            return num
        except ValueError:
            print("El número debe ser un número entero")

def main():
    n = 3 #pedir_tamaño_mat()
    matrix = Matrix(n, n)
    for i in range(n):
        for j in range(n):
            print("Ingrese el valor de la posición ({}, {})".format(i, j))
            num = pedir_numero()
            matrix.set_value(i, j, num)
    print("La matriz es:")
    matrix.print_matrix()
    print("El determinante de la matriz es: {}".format(Matrix.strassen_determinante(matrix)))

if __name__ == '__main__':
    main()
