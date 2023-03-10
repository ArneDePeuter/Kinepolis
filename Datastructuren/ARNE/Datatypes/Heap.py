def createItem(key,val):
    return Item(key, val)

class Item:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
    
    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self) -> str:
        return "key: " + str(self.key) + ", val: " + str(self.val)

class Node:
    def __init__(self, item=None) -> None:
        self.item = item
        self.left = None
        self.right = None
        self.parent = None
    
    def isEmpty(self):
        return self.item is None
    
    def isLeaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        return self.item.key<other.item.key
    
    def __gt__(self, other):
        return self.item.key>other.item.key

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
        myItem = self.item
        otherItem = other.item
        self.item = otherItem
        other.item = myItem
    
    def insertComplete(self, item):
        newNode = Node(item)
        newNode.parent = self
        if self.left is None:
            self.left = newNode
        elif self.right is None:
            self.right = newNode
        elif self.left is not None:
            return self.left.insertComplete(item)
        elif self.right is not None:
            return self.right.insertComplete(item)
        return newNode
    
    def fix(self, lastnode):
        if lastnode.parent is not None:
            lastnode.parent.removeChild(lastnode)
        newNode = Node(lastnode.item)
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
        self.item = createItem(d["root"], "")
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
        d["root"] = self.item.val
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
            return [False, None]
        topItem = self.root.item
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
        return [True, topItem]

    def heapInsert(self, item):
        if self.heapIsEmpty():
            self.root.item = item
            return True
        newNode = self.root.insertComplete(item)
        newNode.heapifyUp(self.relationOperator)
        return True
    
    def load(self, d):
        self.root.load(d)

    def save(self):
        return self.root.save()

