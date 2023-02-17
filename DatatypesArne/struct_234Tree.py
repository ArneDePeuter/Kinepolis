class Node:
    def __init__(self, value=None) -> None:
        self.values = []
        if value is not None:
            self.values = [value]
        self.parent = None
        self.children = []
    
    def __str__(self) -> str:
        s = ""
        for i,val in enumerate(self.values):
            if len(self.values)-1 == i:
                s += str(val)
            else:
                s += str(val) + "\n"
        return s
    
    def __lt__(self, other):
        return self.getBiggestValue() < other.getBiggestValue()
    
    def getBiggestValue(self):
        return self.values[-1]
    
    def getSmallestValue(self):
        return self.values[0]
    
    def addValue(self, newVal):
        self.values.append(newVal)
        self.values.sort()
    
    def addChild(self, newChild):
        self.children.append(newChild)
        self.children.sort()
    
    def removeChild(self, child):
        self.children.remove(child)

    def isEmpty(self):
        return len(self.values) == 0 
    
    def isLeaf(self):
        return len(self.children) == 0
    
    def isRoot(self):
        return self.parent is None
    
    def has1(self):
        return len(self.values) == 1

    def left(self):
        return self.children[0]

    def right(self):
        return self.children[-1]
    
    def has2(self):
        return len(self.values) == 2
    
    def middle(self):
        return self.children[1]
    
    def has3(self):
        return len(self.values) == 3
    
    def otherMiddle(self):
        return self.children[2]
    
    def inorderTraverse(self, func):
        if self.isLeaf():
            func(self)
        else:
            if self.left() is not None:
                self.left().inorderTraverse(func)
                func(self)
            if self.right() is not None:
                self.right().inorderTraverse(func)
        
    def split(self):
        if self.isRoot():
            p = Node()
            self.parent = p
        else:
            p = self.parent
            p.removeChild(self)

        left = Node(self.values[0])
        p.addValue(self.values[1])
        right = Node(self.values[2])

        left.parent = p
        right.parent = p
        
        p.addChild(left)
        p.addChild(right)
        
        if not self.isLeaf():
            left.addChild(self.left())
            self.left().parent = left
            left.addChild(self.middle())
            self.middle().parent = left
            right.addChild(self.otherMiddle())
            self.otherMiddle().parent = right
            right.addChild(self.right())
            self.right().parent = right
        return p
    
    def findInsertTarget(self, value):
        if self.has3():
            newParent = self.split()
            return newParent.findInsertTarget(value)
        if self.isLeaf():
            return self
        else:
            if value<self.getSmallestValue():
                return self.left().findInsertTarget(value)
            elif value>self.getBiggestValue():
                return self.right().findInsertTarget(value)
            elif self.has2():
                return self.middle().findInsertTarget(value)
    
    def insert(self, value):
        if not self.isEmpty():
            target = self.findInsertTarget(value)
            target.addValue(value)
        else:
            self.addValue(value)
        return True
    
    def save(self):
        d = {}
        d['root'] = self.values
        l = []
        if not self.isLeaf():
            for child in self.children:
                l.append(child.save())
            d['children'] = l
        return d

class twoThreeFourTree:
    def __init__(self) -> None:
        self.root = Node()
    
    def isEmpty(self):
        return self.root.isEmpty()
    
    def insert(self, value):
        succes = self.root.insert(value)
        if not self.root.isRoot():
            self.root = self.root.parent
        return succes
    
    def save(self):
        return self.root.save()
    
    def inorderTraverse(self, func):
        self.root.inorderTraverse(func)