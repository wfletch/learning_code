# Implement a Heap Using an array


class Heap():
    def __init__():
        self._heap = []
    def push(self, value):
        self._heap.append(value)

        #Rebuild heap property from our newly inserted value
    def pop(self):
        # Swap with last element in the heap.
        self._swap(0,-1)

        # Rebalance
    def _swap(self, i,j):
        self._heap[j] = self._heap[j] ^ self._heap[i]
        self._heap[i] = self._heap[j] ^ self._heap[i]
        self._heap[j] = self._heap[j] ^ self._heap[i]

    def _heapify_up(self, i):
        pass
    def heapify_up(self, i):
        pass
