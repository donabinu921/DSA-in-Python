class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def isFull(self):
        return len(self.data) == self.capacity

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def enqueue(self, value):
        if self.isFull():
            print("Cannot enqueue. Queue is full.")
        else:
            self.data.append(value)
            print(f"{value} enqueued into queue.")

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue. Queue is empty.")
        else:
            val = self.data.pop(0)
            print(f"{val} dequeued from queue.")

    def peek(self):
        if self.isEmpty():
            print("Queue is empty. Nothing to peek.")
        else:
            print("Front of queue:", self.data[0])

    def display(self):
        print("Queue:", self.data)


def main():
    capacity = int(input("Enter queue capacity: "))
    queue = Queue(capacity)
    while True:
        print("\n1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Is Full")
        print("7. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value to enqueue: "))
            queue.enqueue(val)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            queue.display()
        elif choice == '5':
            print("Current size:", queue.size())
        elif choice == '6':
            print("Is full:", queue.isFull())
        elif choice == '7':
            print("Is empty:", queue.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
