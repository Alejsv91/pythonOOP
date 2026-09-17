# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de push (para agregar nodos) y pop (para quitar nodos).
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts 
# o tuples ni módulos como collections.

class Node:
    data: str
    next: "Node"
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    head: Node
    
    def __init__(self, head: Node):
        self.head = head
    
    def push(self, node: Node):
        next_node = self.head
        self.head = node
        self.head.next = next_node
        
    def pop(self):
        if self.head is not None:
            self.head = self.head.next            
    
    def print_stack(self):
        current_node = self.head
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
        
node1 = Node("This is node 1")
node2 = Node("This is node 2")
node3 = Node("This is node 3")

stack = Stack(node1)
stack.push(node2)
stack.push(node3)

stack.print_stack()

print("--- Pop a node from stack ---")
stack.pop()

stack.print_stack()