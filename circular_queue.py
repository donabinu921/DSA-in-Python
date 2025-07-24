class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    def isFull(self):
        return self.count == self.capacity

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, value):
        if self.isFull():
            print("Cannot enqueue. Circular queue is full.")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.capacity
            self.data[self.rear] = value
            self.count += 1
            print(f"{value} enqueued.")

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue. Circular queue is empty.")
        else:
            val = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.count -= 1
            if self.count == 0:
                self.front = self.rear = -1
            print(f"{val} dequeued.")

    def peek(self):
        if self.isEmpty():
            print("Circular queue is empty. Nothing to peek.")
        else:
            print("Front of queue:", self.data[self.front])

    def display(self):
        if self.isEmpty():
            print("Circular queue is empty.")
        else:
            print("Circular queue contents:")
            idx = self.front
            for _ in range(self.count):
                print(self.data[idx], end=" ")
                idx = (idx + 1) % self.capacity
            print()


def main():
    capacity = int(input("Enter circular queue capacity: "))
    cq = CircularQueue(capacity)
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
            cq.enqueue(val)
        elif choice == '2':
            cq.dequeue()
        elif choice == '3':
            cq.peek()
        elif choice == '4':
            cq.display()
        elif choice == '5':
            print("Current size:", cq.size())
        elif choice == '6':
            print("Is full:", cq.isFull())
        elif choice == '7':
            print("Is empty:", cq.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
