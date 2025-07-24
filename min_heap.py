class MinHeap:
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

    def get_min(self):
        if self.isEmpty():
            print("Heap is empty.")
        else:
            print("Minimum element:", self.heap[0])

    def delete_min(self):
        if self.isEmpty():
            print("Cannot delete. Heap is empty.")
            return
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if not self.isEmpty():
            self.heap[0] = last_val
            self._heapify_down(0)
        print(f"{min_val} deleted.")

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def display(self):
        if self.isEmpty():
            print("Heap is empty.")
        else:
            print("Heap elements:", self.heap)


def main():
    heap = MinHeap()
    while True:
        print("\n1. Insert")
        print("2. Delete Min")
        print("3. Get Min")
        print("4. Display Heap")
        print("5. Size")
        print("6. Is Empty")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            val = int(input("Enter value to insert: "))
            heap.insert(val)
        elif choice == '2':
            heap.delete_min()
        elif choice == '3':
            heap.get_min()
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
