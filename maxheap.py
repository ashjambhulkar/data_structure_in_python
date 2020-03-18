class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)

    def __percolateUp(self, index):
        mid = len(self.heap) // 2
        if self.heap[mid] < self.heap[index]:
            self.heap[mid], self.heap[index] = self.heap[index], self.heap[mid]
            self.__percolateUp(mid)

    def getMax(self):
        return self.heap[0]

    def removeMax(self):
        if self.heap:
            temp = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return temp

    def __maxHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if self.heap[largest] < self.heap[left]:
            largest = left
        if self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__maxHeapify(largest)

    def buildHea(self, arr):
        self.heap = arr
        for i in range(len(self.heap)-1, -1, -1):
            self.__maxHeapify(i)


heap = MaxHeap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)
print(heap.getMax())