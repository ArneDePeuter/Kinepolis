def createItem(key,val):
    return Item(key, val)


class Item:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
    
    def __lt__(self, other):
        if type(other) == type(self):
            return self.key < other.key
        else:
            return self.key < other

    def __eq__(self, other):
        if type(other) == type(self):
            return self.key == other.key
        else:
            return self.key == other
    
    def __repr__(self):
        return repr(self.val)
    
    def __getattr__(self, name):
        return getattr(self.val, name)

class Node:
    def __init__(self, item=None) -> None:
        self.items = []
        if item is not None:
            self.items = [item]
        self.parent = None
        self.children = []
    
    def __str__(self) -> str:
        s = ""
        for i,val in enumerate(self.items):
            if len(self.items)-1 == i:
                s += str(val)
            else:
                s += str(val) + "\n"
        return s
    
    def __lt__(self, other):
        return self.getBiggestItem() < other.getBiggestItem()
    
    def getBiggestItem(self):
        return self.items[-1]
    
    def getSmallestItem(self):
        return self.items[0]
    
    def addItem(self, newItem):
        self.items.append(newItem)
        self.items.sort()
    
    def addChild(self, newChild):
        self.children.append(newChild)
        self.children.sort()
    
    def removeChild(self, child):
        self.children.remove(child)

    def isEmpty(self):
        return len(self.items) == 0 
    
    def isLeaf(self):
        return len(self.children) == 0
    
    def isRoot(self):
        return self.parent is None
    
    def has1Item(self):
        return len(self.items) == 1

    def left(self):
        return self.children[0]

    def right(self):
        return self.children[-1]
    
    def has2Items(self):
        return len(self.items) == 2
    
    def middle(self):
        return self.children[1]
    
    def has3Items(self):
        return len(self.items) == 3
    
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

        left = Node(self.items[0])
        p.addItem(self.items[1])
        right = Node(self.items[2])

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
    
    def findInsertTarget(self, item):
        if self.has3Items():
            newParent = self.split()
            return newParent.findInsertTarget(item)
        if self.isLeaf():
            return self
        else:
            if item<self.getSmallestItem():
                return self.left().findInsertTarget(item)
            elif item>self.getBiggestItem():
                return self.right().findInsertTarget(item)
            elif self.has2Items():
                return self.middle().findInsertTarget(item)
    
    def insertItem(self, item):
        if not self.isEmpty():
            target = self.findInsertTarget(item)
            target.addItem(item)
        else:
            self.addItem(item)
        return True
    
    def getDoubleItemChild(self):
        for child in self.children:
            if child.has2Items():
                return child
        return None
    
    def merge(self):
        """
        Merges the parent with its children

        preconditions: The parent has 2 items or the parent has 1 value and no doublechild
        postconditions: Merges the parent with its children
        """
        if self.left().isEmpty():
            removedChild = self.left()
            self.removeChild(self.left())
        elif self.right().isEmpty():
            removedChild = self.right()
            self.removeChild(self.right())
        else:
            removedChild = self.middle()
            self.removeChild(self.middle())
            
        self.left().addItem(self.items.pop(0))
        if not removedChild.isLeaf():
            self.left().addChild(removedChild.left())
            removedChild.left().parent = self.left()
        if self.isEmpty():
            self.fixBeforeDel()
    
    def redivide(self):
        doubleChild = self.getDoubleItemChild()
        if doubleChild == self.left():
            self.right().items = self.items
            self.items = [self.left().items.pop()]
            if not doubleChild.isLeaf():
                self.right().addChild(doubleChild.right())
                doubleChild.removeChild(doubleChild.right())
        else:
            self.left().items = self.items
            self.items = [self.right().items.pop(0)]
            if not doubleChild.isLeaf():
                self.left().addChild(doubleChild.left())
                doubleChild.removeChild(doubleChild.left())
        
    def fixBeforeDel(self):
        if self.has1Item():
            p = self.parent
            if p.has2Items():
                p.merge()
            else:
                if p.getDoubleItemChild() is not None:
                    p.redivide()
                else:
                    p.merge()
            return p
        return self
    
    def findInorderAndMerge(self):
        """
        Returns the inorderSuccessor

        preconditions: None
        postconditions: returns the inordersuccessor
        """
        if self.right() is not None:
            current = self.right()
            current = current.fixBeforeDel()
            if current.isLeaf():
                return current
            while current.left() is not None:
                current = current.left()
                current = current.fixBeforeDel()
                if current.isLeaf():
                    return current
            return current
        else:
            current = self.parent
            while current is not None and current < self:
                current = current.parent
                current = current.fixBeforeDel()
            return current

    def retrieveAndMerge(self, item):
        if not self.isRoot():
            newParent = self.fixBeforeDel()
            return newParent.retrieveAndMerge(item)
        if self.isLeaf():
            if self.item == item:
                return self, True
            else:
                return None, False
        else:
            if item<self.getSmallestItem():
                return self.left().retrieveAndMerge(item)
            elif item>self.getBiggestItem():
                return self.right().retrieveAndMerge(item)
            elif self.has2Items():
                return self.middle().retrieveAndMerge(item)

    def deleteItem(self, item):
        node, succes = self.retrieveAndMerge(item)
        if succes:
            leaf = node
            if not node.isLeaf():
                leaf = node.findInorderAndMerge()
                node.items.remove(item)
                node.addItem(leaf.items[0])
                leaf.items.remove(leaf.items[0])
            else:
                leaf.items.remove(item)
            return True
        return False

    def stringList(self, l):
        l = []
        for it in self.items:
            l.append(str(it.key))
        return l
    
    def save(self):
        d = {}
        d['root'] = self.stringList(self.items)
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
    
    def insert(self, item):
        succes = self.root.insertItem(item)
        if not self.root.isRoot():
            self.root = self.root.parent
        return succes

    def delete(self, item):
        return self.root.deleteItem(item)
    
    def save(self):
        return self.root.save()
    
    def inorderTraverse(self, func):
        self.root.inorderTraverse(func)

t = twoThreeFourTree()
for x in [60,30,10,20,50,40,70,80,15,90,100]:
    t.insert(createItem(x, f"test{x}"))

print(t.delete(createItem(60, "")))
print(t.save())