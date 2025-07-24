class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def isFull(self):
        return len(self.data) == self.capacity

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def push(self, value):
        if self.isFull():
            print("Cannot push. Stack is full.")
        else:
            self.data.append(value)
            print(f"{value} pushed onto stack.")

    def pop(self):
        if self.isEmpty():
            print("Cannot pop. Stack is empty.")
        else:
            val = self.data.pop()
            print(f"{val} popped from stack.")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty. Nothing to peek.")
        else:
            print("Top of stack:", self.data[-1])

    def display(self):
        print("Stack:", list(reversed(self.data)))


def main():
    capacity = int(input("Enter stack capacity: "))
    stack = Stack(capacity)
    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Is Full")
        print("7. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value to push: "))
            stack.push(val)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print("Current size:", stack.size())
        elif choice == '6':
            print("Is full:", stack.isFull())
        elif choice == '7':
            print("Is empty:", stack.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
