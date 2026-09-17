from node import Node
        
class Queue:
    head: Node
    
    def __init__(self, head):
        self.head = head
        
    def print_structure(self):
        current_node = self.head
        
        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next
    
    def enqueue(self, node):
        current_node = self.head
        
        while (current_node.next is not None):
            current_node = current_node.next
        
        current_node.next = node
        
    def dequeue(self):
        if self.head:
            self.head = self.head.next        
            
first_node = Node("Hola Mundo")
second_node = Node("Soy el segundo")
first_node.next = second_node

third_node = Node("Soy el tercero")
second_node.next = third_node

structure = Queue(first_node)

forth_node = Node("Soy el nuevo!")
structure.enqueue(forth_node)

structure.print_structure()
# structure.queue()  

# print("DEQUEUE")

# structure.dequeue()
# structure.print_structure()  
    
    
    
    