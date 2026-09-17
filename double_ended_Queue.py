# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de push_left y push_right (para agregar nodos al inicio
# y al final) y pop_left
# y pop_right (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts 
# o tuples ni módulos como collections.

from node import Node

class DoubleEndedQueue:
    head: Node
    
    def __init__(self, head: Node):
        self.head = head
        
    def push_left(self, node: Node):
        next_node = self.head
        self.head = node
        self.head.next = next_node
        
    def pop_left(self):
        if self.head is not None:
            self.head = self.head.next      
    
    def push_right(self, node: Node):
        current_node = self.head
        
        while (current_node.next is not None):
            current_node = current_node.next
        
        current_node.next = node    
        
    def pop_right(self):
        current_node = self.head
        
        while (current_node.next is not None):
            current_node = current_node.next
            current_node.next = None
    
    def print_structure(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
            
node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")
node4 = Node("Node 4")

deq = DoubleEndedQueue(node1)
deq.push_left(node2)

print("---- First deq ----")
deq.print_structure()

print("---- Push left a node ----")
deq.push_left(node3)
deq.print_structure()

print("---- pop left a node ----")
deq.pop_left()
deq.print_structure()

print("---- push right ----")
deq.push_right(node4)
deq.print_structure()

print("---- pop right ----")
deq.pop_right()
deq.print_structure()


    
