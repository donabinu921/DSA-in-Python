class MaxHeap:
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        print(f"{value} inserted.")

    def get_max(self):
        if self.isEmpty():
            print("Heap is empty.")
        else:
            print("Maximum element:", self.heap[0])

    def delete_max(self):
        if self.isEmpty():
            print("Cannot delete. Heap is empty.")
            return
        max_val = self.heap[0]
        last_val = self.heap.pop()
        if not self.isEmpty():
            self.heap[0] = last_val
            self._heapify_down(0)
        print(f"{max_val} deleted.")

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def display(self):
        if self.isEmpty():
            print("Heap is empty.")
        else:
            print("Heap elements:", self.heap)


def main():
    heap = MaxHeap()
    while True:
        print("\n1. Insert")
        print("2. Delete Max")
        print("3. Get Max")
        print("4. Display Heap")
        print("5. Size")
        print("6. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value to insert: "))
            heap.insert(val)
        elif choice == '2':
            heap.delete_max()
        elif choice == '3':
            heap.get_max()
        elif choice == '4':
            heap.display()
        elif choice == '5':
            print("Size of heap:", heap.size())
        elif choice == '6':
            print("Is empty:", heap.isEmpty())
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
