class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def getLength(self):
        return self.size

    def insert(self, index, item):
        if index == 1:
            prevHead = self.head
            self.head = Node(item)
            self.head.next = prevHead
        elif index > self.size + 1 or index < 1:
            return False
        else:
            idCounter = 1
            tgt = self.head
            while idCounter != index - 1:
                tgt = tgt.next
                idCounter += 1
            if tgt.next == None:
                tgt.next = Node(item)
                tgt.next.prev = tgt
            else:
                prevNode = tgt.next
                tgt.next = Node(item)
                tgt.next.next = prevNode
                prevNode.prev = tgt.next
        self.size += 1
        return True

    def retrieve(self, index):
        if index > self.size:
            return None, False
        idCounter = 1
        tgt = self.head
        while tgt.next != None and idCounter < index:
            tgt = tgt.next
            idCounter += 1
        return tgt.item, True

    def save(self):
        items = []
        tgt = self.head
        while tgt != None:
            items.append(tgt.item)
            tgt = tgt.next
        return items

    def load(self, items):
        self.__init__()
        pos = 1
        for item in items:
            self.insert(pos, item)
            pos += 1

    def delete(self, index):
        if index > self.size or index < 1:
            return False
        if index == 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            idCounter = 1
            tgt = self.head
            while tgt.next != None and idCounter < index:
                tgt = tgt.next
                idCounter += 1
            if tgt.next == None:
                tgt.prev.next = None
            else:
                tgt.prev.next = tgt.next
                tgt.next = tgt.next.next
        self.size -= 1
        return True
