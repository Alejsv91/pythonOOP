class Node:
    data: str
    next: "Node"
    
    def __init__(self, data):
        self.data = data
        self.next = None