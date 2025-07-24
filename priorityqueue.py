class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def isFull(self):
        return len(self.data) == self.capacity

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def enqueue(self, value, priority):
        if self.isFull():
            print("Cannot enqueue. Priority queue is full.")
        else:
            self.data.append((priority, value))
            self.data.sort()
            print(f"{value} enqueued with priority {priority}.")

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue. Priority queue is empty.")
        else:
            priority, value = self.data.pop(0)
            print(f"{value} with priority {priority} dequeued.")

    def peek(self):
        if self.isEmpty():
            print("Priority queue is empty. Nothing to peek.")
        else:
            priority, value = self.data[0]
            print(f"Front of queue: {value} with priority {priority}")

    def display(self):
        print("Priority Queue (low number = high priority):")
        for priority, value in self.data:
            print(f"{value} (priority {priority})")


def main():
    capacity = int(input("Enter priority queue capacity: "))
    pq = PriorityQueue(capacity)
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
            val = input("Enter value to enqueue: ")
            priority = int(input("Enter priority (lower = higher priority): "))
            pq.enqueue(val, priority)
        elif choice == '2':
            pq.dequeue()
        elif choice == '3':
            pq.peek()
        elif choice == '4':
            pq.display()
        elif choice == '5':
            print("Current size:", pq.size())
        elif choice == '6':
            print("Is full:", pq.isFull())
        elif choice == '7':
            print("Is empty:", pq.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
