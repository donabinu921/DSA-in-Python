class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail is None

    def size(self):
        if self.isEmpty():
            return 0
        count = 1
        current = self.tail.next
        while current != self.tail:
            count += 1
            current = current.next
        return count

    def insert_front(self, value):
        node = Node(value)
        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
        print(f"{value} inserted at front.")

    def insert_end(self, value):
        node = Node(value)
        if self.isEmpty():
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        print(f"{value} inserted at end.")

    def insert_after(self, target, value):
        if self.isEmpty():
            print("List is empty.")
            return
        current = self.tail.next
        while True:
            if current.value == target:
                node = Node(value)
                node.next = current.next
                current.next = node
                if current == self.tail:
                    self.tail = node
                print(f"{value} inserted after {target}.")
                return
            current = current.next
            if current == self.tail.next:
                break
        print(f"{target} not found.")

    def delete(self, value):
        if self.isEmpty():
            print("Cannot delete. List is empty.")
            return
        current = self.tail.next
        prev = self.tail
        while True:
            if current.value == value:
                if current == self.tail and current.next == self.tail:
                    self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                print(f"{value} deleted from list.")
                return
            prev = current
            current = current.next
            if current == self.tail.next:
                break
        print(f"{value} not found in list.")

    def search(self, value):
        if self.isEmpty():
            print("List is empty.")
            return
        current = self.tail.next
        index = 0
        while True:
            if current.value == value:
                print(f"{value} found at position {index}.")
                return
            current = current.next
            index += 1
            if current == self.tail.next:
                break
        print(f"{value} not found in list.")

    def display(self):
        if self.isEmpty():
            print("List is empty.")
            return
        current = self.tail.next
        print("Circular Linked List:", end=" ")
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.tail.next:
                break
        print("(back to start)")


def main():
    cll = CircularLinkedList()
    while True:
        print("\n1. Insert at Front")
        print("2. Insert at End")
        print("3. Insert After a Node")
        print("4. Delete")
        print("5. Search")
        print("6. Display")
        print("7. Size")
        print("8. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value: "))
            cll.insert_front(val)
        elif choice == '2':
            val = int(input("Enter value: "))
            cll.insert_end(val)
        elif choice == '3':
            target = int(input("Insert after which value? "))
            val = int(input("Enter value to insert: "))
            cll.insert_after(target, val)
        elif choice == '4':
            val = int(input("Enter value to delete: "))
            cll.delete(val)
        elif choice == '5':
            val = int(input("Enter value to search: "))
            cll.search(val)
        elif choice == '6':
            cll.display()
        elif choice == '7':
            print("Size of list:", cll.size())
        elif choice == '8':
            print("Is empty:", cll.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
