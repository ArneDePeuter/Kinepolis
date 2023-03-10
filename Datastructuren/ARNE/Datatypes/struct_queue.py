class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class MyQueue():
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getFront(self):
        if (self.isEmpty()):
            return(False, None)
        iter = self.head
        while (iter.next != None):
            iter = iter.next
        return (True, iter.value)

    def enqueue(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        return True
        
    def dequeue(self):
        if (self.isEmpty()):
            return(False, None)
        prev = iter = self.head
        while (iter.next != None):
            prev = iter
            iter = iter.next
        prev.next = None
        return(True, iter.value)

    def load(self, l):
        self.head = None
        for elem in reversed(l):
            self.enqueue(elem)

    def save(self):
        l = []
        tgt = self.head
        while tgt.next != None:
            l.append(tgt.value)
            tgt = tgt.next
        l.append(tgt.value)
        return l