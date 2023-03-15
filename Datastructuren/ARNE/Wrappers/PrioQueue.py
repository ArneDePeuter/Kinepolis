from Datastructuren.ARNE.Datatypes.Heap import Heap, Item

class PriorityQueue(Heap):
    def __init__(self, maxHeap=True):
        super().__init__(maxHeap)

    def createItem(self, key, val):
        return Item(key, val)
    
    def isEmpty(self):
        return self.heapIsEmpty()

    def dequeue(self):
        item, succes = self.heapDelete()
        if succes:
            return [item.val, succes]
        else:
            return [None, succes]
    
    def enqueue(self, item):
        return self.heapInsert(item)