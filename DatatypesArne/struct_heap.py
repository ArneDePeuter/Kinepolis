class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def isEmpty(self):
        return self.value==None
    
    def isLeaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        return self.value<other.value
    
    def __gt__(self, other):
        return self.value>other.value

    def getLastNode(self):
        if self.isLeaf():
            return self
        if self.right:
            return self.right.getLastNode()
        else:
            return self.left.getLastNode()
    
    def removeChild(self, child):
        if child == self.left:
            self.left = None
        else:
            self.right = None
    
    def swap(self, other):
        myVal = self.value
        otherVal = other.value
        self.value = otherVal
        other.value = myVal
    
    def insertComplete(self, val):
        newNode = Node(val)
        newNode.parent = self
        if self.left is None:
            self.left = newNode
        elif self.right is None:
            self.right = newNode
        elif self.left is not None:
            return self.left.insertComplete(val)
        elif self.right is not None:
            return self.right.insertComplete(val)
        return newNode
    
    def fix(self, lastnode):
        if lastnode.parent is not None:
            lastnode.parent.removeChild(lastnode)
        newNode = Node(lastnode.value)
        newNode.parent = self
        if self.left is None:
            self.left = newNode
        elif self.right is None:
            self.right = newNode

    def heapifyUp(self, operator):
        if self.parent is not None:
            if operator(self, self.parent)==self:
                self.swap(self.parent)
                self.parent.heapifyUp(operator)
    
    def heapifyDown(self, operator):
        if self.left is not None:
            if operator(self.left, self)==self.left:
                self.swap(self.left)
                self.left.heapifyDown(operator)
        if self.right is not None:
            if operator(self.right, self)==self.right:
                self.swap(self.right)
                self.right.heapifyDown(operator)
    
    def load(self, d):
        self.value = d["root"]
        if "children" not in d.keys():
            return
        leftTree = d["children"][0]
        rightTree = d["children"][1]
        if type(leftTree)==dict:
            self.left = Node()
            self.left.parent = self
            self.left.load(leftTree)
        else:
            self.left = leftTree
        if type(rightTree)==dict:
            self.right = Node()
            self.right.parent = self
            self.right.load(rightTree)
        else:
            self.right = rightTree
    
    def save(self):
        d = {}
        d["root"] = self.value
        if not self.isLeaf():
            d["children"] = [None, None]
            if type(self.left)==Node:
                if not self.left.isEmpty():
                    d["children"][0] = self.left.save()
            if type(self.right)==Node:
                if not self.right.isEmpty():
                    d["children"][1] = self.right.save()
        return d

class Heap:
    def __init__(self,maxHeap=True):
        self.maxheap = maxHeap
        self.root = Node()
        self.relationOperator = max if self.maxheap else min
    
    def heapIsEmpty(self):
        return self.root.isEmpty()
    
    def heapDelete(self):
        if self.heapIsEmpty():
            return [None, False]
        topVal = self.root.value
        lastNode = self.root.getLastNode()
        self.root.swap(lastNode)
        if lastNode.parent is not None:
            lastNode.parent.removeChild(lastNode)
        self.root.heapifyDown(self.relationOperator)
        if lastNode.parent is not None:
            temp = self.root.getLastNode().parent
            l = temp.left
            r = temp.right
            if l == None:
                lastNode.parent.fix(r)
            elif r == None:
                lastNode.parent.fix(l)
            elif self.relationOperator(l, r) == l:
                lastNode.parent.fix(r)
            elif self.relationOperator(l, r) == r:
                lastNode.parent.fix(l)
                temp.left = r
                temp.right = None
        return [topVal, True]

    def heapInsert(self, value):
        if self.heapIsEmpty():
            self.root.value = value
            return True
        newNode = self.root.insertComplete(value)
        newNode.heapifyUp(self.relationOperator)
        return True
    
    def load(self, d):
        self.root.load(d)

    def save(self):
        return self.root.save()

class HeapQueue(Heap):
    def __init__(self, maxHeap=True):
        super().__init__(maxHeap)
    
    def isEmpty(self):
        return self.heapIsEmpty()

    def dequeue(self):
        return self.heapDelete()
    
    def enqueue(self, val):
        return self.heapInsert(val)