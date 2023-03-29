class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def get(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.val

    def set(self, index, val):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        current_node.val = val

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
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
        self.m = 3
        self.n = 3
        self.matrix = []
        for i in range(m):
            row = LinkedList()
            for j in range(n):
                row.insert(None)
            self.matrix.append(row)

    def set_value(self, i, j, value):
        self.matrix[i].set(j, value)

    def get_value(self, i, j):
        return self.matrix[i].get(j)

    def print_matrix(self):
        for i in range(self.m):
            row = ''
            for j in range(self.n):
                row += str(self.get_value(i, j)) + ' '
            print(row)

    def sarrus(matriz):
            a = matriz.get_value(0, 0)
            b = matriz.get_value(0, 1)
            c = matriz.get_value(0, 2)
            d = matriz.get_value(1, 0)
            e = matriz.get_value(1, 1)
            f = matriz.get_value(1, 2)
            g = matriz.get_value(2, 0)
            h = matriz.get_value(2, 1)
            i = matriz.get_value(2, 2)
            return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
    

matriz = Matrix(3, 3)
matriz.set_value(0, 0, 1)
matriz.set_value(0, 1, 2)
matriz.set_value(0, 2, 3)
matriz.set_value(1, 0, 4)
matriz.set_value(1, 1, 5)
matriz.set_value(1, 2, 6)
matriz.set_value(2, 0, 7)
matriz.set_value(2, 1, 8)
matriz.set_value(2, 2, 9)
matriz.print_matrix()
print(matriz.sarrus())