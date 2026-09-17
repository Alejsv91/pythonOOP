# Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer print de toda la estructura.
# No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BT:
    def __init__(self, head):
        self.head = head

    def print_structure(self):
        self._print_node(self.head)

    def _print_node(self, node):
        if node is None:
            return

        print(f"Node: {node.data}")

        if node.left:
            print(f"  Left: {node.left.data}")

        if node.right:
            print(f"  Right: {node.right.data}")

        self._print_node(node.left)
        self._print_node(node.right)
        
root = Node("1")

root.left = Node("2")
root.right = Node("3")

root.left.left = Node("4")
root.left.right = Node("5")

tree = BT(root)

tree.print_structure()