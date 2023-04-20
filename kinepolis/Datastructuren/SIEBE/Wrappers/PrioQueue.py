from ..Datatypes.MyHeap import Heap

class PrioQueue:
    def __init__(self, maxQueue=True):
        self.heap = Heap(maxQueue)

    def isEmpty(self):
        return self.heap.heapIsEmpty()

    def dequeue(self):
        return self.heap.heapDelete()

    def enqueue(self, item):
        return self.heap.heapInsert(item)

    def save(self):
        return self.heap.save()

    def load(self, dataDict):
        return self.heap.load(dataDict)