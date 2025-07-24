class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)
        print(f"{value} inserted.")

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                print(f"{value} found in tree.")
                return
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        print(f"{value} not found in tree.")

    def delete(self, value):
        def _delete(node, value):
            if not node:
                return node, False
            if value < node.value:
                node.left, deleted = _delete(node.left, value)
            elif value > node.value:
                node.right, deleted = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right, True
                elif not node.right:
                    return node.left, True
                temp = self._minValueNode(node.right)
                node.value = temp.value
                node.right, _ = _delete(node.right, temp.value)
                return node, True
            return node, deleted

        self.root, deleted = _delete(self.root, value)
        if deleted:
            print(f"{value} deleted.")
        else:
            print(f"{value} not found in tree.")

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def in_order(self):
        def _in_order(node):
            if node:
                _in_order(node.left)
                print(node.value, end=" ")
                _in_order(node.right)
        if self.isEmpty():
            print("Tree is empty.")
        else:
            print("In-order traversal:", end=" ")
            _in_order(self.root)
            print()

    def pre_order(self):
        def _pre_order(node):
            if node:
                print(node.value, end=" ")
                _pre_order(node.left)
                _pre_order(node.right)
        if self.isEmpty():
            print("Tree is empty.")
        else:
            print("Pre-order traversal:", end=" ")
            _pre_order(self.root)
            print()

    def post_order(self):
        def _post_order(node):
            if node:
                _post_order(node.left)
                _post_order(node.right)
                print(node.value, end=" ")
        if self.isEmpty():
            print("Tree is empty.")
        else:
            print("Post-order traversal:", end=" ")
            _post_order(self.root)
            print()

    def size(self):
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)


def main():
    bst = BST()
    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. In-order Traversal")
        print("5. Pre-order Traversal")
        print("6. Post-order Traversal")
        print("7. Size")
        print("8. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value to insert: "))
            bst.insert(val)
        elif choice == '2':
            val = int(input("Enter value to delete: "))
            bst.delete(val)
        elif choice == '3':
            val = int(input("Enter value to search: "))
            bst.search(val)
        elif choice == '4':
            bst.in_order()
        elif choice == '5':
            bst.pre_order()
        elif choice == '6':
            bst.post_order()
        elif choice == '7':
            print("Size of tree:", bst.size())
        elif choice == '8':
            print("Is empty:", bst.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
