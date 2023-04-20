from ..Datatypes.MyHeap import Heap, createItem

class PrioQueue:
    def __init__(self, maxQueue=False):
        self.heap = Heap(maxQueue)

    def isEmpty(self):
        return self.heap.heapIsEmpty()

    def dequeue(self):
        return self.heap.heapDelete()

    def enqueue(self, key, value):
        return self.heap.heapInsert(createItem(key, value))

    def save(self):
        return self.heap.save()

    def load(self, dataDict):
        return self.heap.load(dataDict)