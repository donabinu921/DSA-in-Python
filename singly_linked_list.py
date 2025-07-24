class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
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
        node.next = self.head
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
            current.next = node
            print(f"{new_value} inserted after {prev_value}.")

    def delete(self, value):
        if self.isEmpty():
            print("Cannot delete. List is empty.")
            return
        if self.head.value == value:
            self.head = self.head.next
            print(f"{value} deleted from list.")
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next is None:
            print(f"{value} not found in list.")
        else:
            current.next = current.next.next
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

    def display(self):
        if self.isEmpty():
            print("List is empty.")
        else:
            current = self.head
            print("Linked List:", end=" ")
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")


def main():
    ll = SinglyLinkedList()
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
            ll.insert_front(val)
        elif choice == '2':
            val = int(input("Enter value: "))
            ll.insert_end(val)
        elif choice == '3':
            prev = int(input("Insert after which value? "))
            val = int(input("Enter value to insert: "))
            ll.insert_after(prev, val)
        elif choice == '4':
            val = int(input("Enter value to delete: "))
            ll.delete(val)
        elif choice == '5':
            val = int(input("Enter value to search: "))
            ll.search(val)
        elif choice == '6':
            ll.display()
        elif choice == '7':
            print("Size of list:", ll.size())
        elif choice == '8':
            print("Is empty:", ll.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
