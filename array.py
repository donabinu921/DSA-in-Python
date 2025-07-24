class MyArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
    
    def isFull(self):
        return len(self.data) == self.capacity

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def insert(self, value):
        if self.isFull():
            print("Cannot insert. Array is full.")
        else:
            self.data.append(value)
            print(f"{value} inserted.")

    def delete(self, value):
        if self.isEmpty():
            print("Cannot delete. Array is empty.")
        elif value in self.data:
            self.data.remove(value)
            print(f"{value} deleted.")
        else:
            print(f"{value} not found in array.")

    def search(self, value):
        if value in self.data:
            print(f"{value} found at index {self.data.index(value)}.")
        else:
            print(f"{value} not found in array.")

    def display(self):
        print("Array contents:", self.data)


def main():
    capacity = int(input("Enter array capacity: "))
    arr = MyArray(capacity)
    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Size")
        print("6. Is Full")
        print("7. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value to insert: "))
            arr.insert(val)
        elif choice == '2':
            val = int(input("Enter value to delete: "))
            arr.delete(val)
        elif choice == '3':
            val = int(input("Enter value to search: "))
            arr.search(val)
        elif choice == '4':
            arr.display()
        elif choice == '5':
            print("Current size:", arr.size())
        elif choice == '6':
            print("Is full:", arr.isFull())
        elif choice == '7':
            print("Is empty:", arr.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
