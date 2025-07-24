class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert_front(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        print(f"{value} inserted at front.")

    def insert_end(self, value):
        node = Node(value)
        if self.isEmpty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
        print(f"{value} inserted at end.")

    def insert_after(self, prev_value, new_value):
        current = self.head
        while current and current.value != prev_value:
            current = current.next
        if current is None:
            print(f"{prev_value} not found.")
        else:
            node = Node(new_value)
            node.next = current.next
            node.prev = current
            if current.next:
                current.next.prev = node
            current.next = node
            print(f"{new_value} inserted after {prev_value}.")

    def delete(self, value):
        if self.isEmpty():
            print("Cannot delete. List is empty.")
            return
        current = self.head
        while current and current.value != value:
            current = current.next
        if current is None:
            print(f"{value} not found in list.")
            return
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        print(f"{value} deleted from list.")

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                print(f"{value} found at position {index}.")
                return
            current = current.next
            index += 1
        print(f"{value} not found in list.")

    def display_forward(self):
        if self.isEmpty():
            print("List is empty.")
        else:
            current = self.head
            print("Forward:", end=" ")
            while current:
                print(current.value, end=" <-> ")
                last = current
                current = current.next
            print("None")

    def display_backward(self):
        if self.isEmpty():
            print("List is empty.")
        else:
            current = self.head
            while current.next:
                current = current.next
            print("Backward:", end=" ")
            while current:
                print(current.value, end=" <-> ")
                current = current.prev
            print("None")


def main():
    dll = DoublyLinkedList()
    while True:
        print("\n1. Insert at Front")
        print("2. Insert at End")
        print("3. Insert After a Node")
        print("4. Delete")
        print("5. Search")
        print("6. Display Forward")
        print("7. Display Backward")
        print("8. Size")
        print("9. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value: "))
            dll.insert_front(val)
        elif choice == '2':
            val = int(input("Enter value: "))
            dll.insert_end(val)
        elif choice == '3':
            prev = int(input("Insert after which value? "))
            val = int(input("Enter value to insert: "))
            dll.insert_after(prev, val)
        elif choice == '4':
            val = int(input("Enter value to delete: "))
            dll.delete(val)
        elif choice == '5':
            val = int(input("Enter value to search: "))
            dll.search(val)
        elif choice == '6':
            dll.display_forward()
        elif choice == '7':
            dll.display_backward()
        elif choice == '8':
            print("Size of list:", dll.size())
        elif choice == '9':
            print("Is empty:", dll.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
