from Datastructuren.ARNE.Datatypes.Heap import Heap, createItem

class PriorityQueue(Heap):
    def __init__(self, maxHeap=True):
        super().__init__(maxHeap)
    
    def isEmpty(self):
        return self.heapIsEmpty()

    def dequeue(self):
        item, succes = self.heapDelete()
        if succes:
            return [item.val, succes]
        else:
            return [None, succes]
    
    def enqueue(self, key, val):
        return self.heapInsert(createItem(key, val))