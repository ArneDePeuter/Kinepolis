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
    """
    A twoThreeTree Node
    """
    def __init__(self, item=None) -> None:
        """
        Initialise the Node

        preconditions: None
        postconditions: Node gets created
        """
        self.items = []
        if item is not None:
            self.items = [item]  #create value list items
        self.children = []
        self.parent = None
    
    #LT operator to sort nodes
    def __lt__(self, other):
        return self.items[-1]<other.items[0]
    
    #str operator to print items of node
    def __str__(self):
        s = ""
        for i, item in enumerate(self.items):
            if (i==len(self.items)-1):
                s+=str(item)
            else:
                s+= str(item) + "\n"
        return s
    
    #returns true if the node is a root
    def isRoot(self):
        return self.parent == None
    
    #returns true if the node is a leaf
    def isLeaf(self):
        return len(self.children) == 0
    
    #returns true if the node is empty
    def isEmpty(self):
        return len(self.items) == 0
    
    #returns true if the node has 2 items
    def has2Items(self):
        return len(self.items) == 2

    #returns true if the node has 3 items
    def has3Items(self):
        return len(self.items) == 3

    def left(self):
        return self.children[0]
    
    def middle(self):
        return self.children[1]
    
    def right(self):
        return self.children[-1]
    
    #returns true if the node contains the searchkey
    def containsItem(self, item):
        for myItem in self.items:
            if item == myItem: #val found
                return True
        return False
    
    #removes a childnode from the node
    def removeChildNode(self, childnode):
        self.children.remove(childnode) #remove from children list
    
    #adds a childnode to the children and keeps the children sorted
    def addChildNode(self, newChild):
        self.children.append(newChild) #add to children list
        self.children.sort()    #sort
            
    #traverses the tree inorder
    def inorderTraverse(self, func):
        if self.isLeaf():
            func(self)
        elif self.has2Items():
            self.left().inorderTraverse(func)
            func(self.items[0])
            self.middle().inorderTraverse(func)
            func(self.items[1])
            self.right().inorderTraverse(func)
        else:
            self.left().inorderTraverse(func)
            func(self.items[0])
            self.right().inorderTraverse(func)
    
    def retrieveItem(self, item):
        if self.containsItem(item):
            return [True, self]
        elif self.isLeaf():
            return [False, None]
        
        if self.has2Items():
            if (item<self.items[0]):
                return self.left().retrieveItem(item)
            elif (item<self.items[1]):
                return self.middle().retrieveItem(item)
            else:
                return self.right().retrieveItem(item)
        else:
            if (item<self.items[0]):
                return self.left().retrieveItem(item)
            else:
                return self.right().retrieveItem(item)
    
    #adds an item to the node and keeps the items sorted
    def addItem(self, item):
        self.items.append(item)
        self.items.sort()
    
    def insertToLeafNode(self, item):
        """ 
        adds an item to the corresponding leafnode of that value

        preconditions: None
        postconditions: adds a value to the corresponding leafnode of that value if its not already in the leaf
        """
        if (self.isLeaf()):
            self.addItem(item)
            return self
        elif self.has2Items():
            if (item<self.items[0]):
                return self.left().insertToLeafNode(item)
            elif (item<self.items[1]):
                return self.middle().insertToLeafNode(item)
            else:
                return self.right().insertToLeafNode(item)
        else:
            if (item<self.items[0] or self.children[1]==None):
                return self.left().insertToLeafNode(item)
            else:
                return self.right().insertToLeafNode(item)
    
    def split(self):
        """
        Splits a node after insertion

        preconditions: The given node has 3 items
        postconditions: The given node gets split
        """
        if (self.isRoot()):
            p = Node()
            self.parent = p
        else:
            p = self.parent
            p.removeChildNode(self)
        
        n1 = Node(self.items[0])
        n1.parent = p
        n2 = Node(self.items[2])
        n2.parent = p
        p.addChildNode(n1)
        p.addChildNode(n2)
        p.addItem(self.items[1])

        if not self.isLeaf():
            l1 = self.children[0]
            l2 = self.children[1]
            r1 = self.children[2]
            r2 = self.children[3]
            l1.parent = n1
            l2.parent = n1
            r1.parent = n2
            r2.parent = n2
            n1.children = [l1, l2]
            n1.children.sort()
            n2.children = [r1, r2]
            n2.children.sort()

        if p.has3Items():
            p.split()

    def insertItem(self, item):
        """
        Inserts an item to the right 2-3 Node
    
        preconditions: None
        postconditions: Item gets inserted into the 2-3 Node if its not already in the tree
        """
        leafNode = self.insertToLeafNode(item)

        if (leafNode.has3Items()):
            leafNode.split()
        return True
    
    def inorderSuccessor(self):
        """
        Returns the inorderSuccessor

        preconditions: None
        postconditions: returns the inordersuccessor
        """
        if self.right() is not None:
            current = self.right()
            if current.isLeaf():
                return current
            while current.left() is not None:
                current = current.left()
                if current.isLeaf():
                    return current
            return current
        else:
            current = self.parent
            while current is not None and current < self:
                current = current.parent
            return current
    
    def deleteItem(self, item):
        """
        Deletes an item from the corresponding 2-3 Node

        preconditions: None
        postconditions: The requested value gets removed
                        returns bool (val deleted -> True else False)
        """
        succes, node = self.retrieveItem(item)
        if succes:
            leaf = node
            if not node.isLeaf():
                leaf = node.inorderSuccessor()
                node.items.remove(item)
                node.addItem(leaf.items[0])
                leaf.items.remove(leaf.items[0])
            else:
                leaf.items.remove(item)
            
            if leaf.isEmpty():
                leaf.fix()
            return True
        else:
            return False
    
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
            self.removeChildNode(self.left())
        elif self.right().isEmpty():
            removedChild = self.right()
            self.removeChildNode(self.right())
        else:
            removedChild = self.middle()
            self.removeChildNode(self.middle())
            
        self.left().addItem(self.items.pop(0))
        if not removedChild.isLeaf():
            self.left().addChildNode(removedChild.left())
            removedChild.left().parent = self.left()

        if self.isEmpty():
            self.fix()
    
    def redivide(self):
        doubleChild = self.getDoubleItemChild()
        if doubleChild == self.left():
            self.right().items = self.items
            self.items = [self.left().items.pop()]
            if not doubleChild.isLeaf():
                self.right().addChildNode(doubleChild.right())
                doubleChild.removeChildNode(doubleChild.right())
        else:
            self.left().items = self.items
            self.items = [self.right().items.pop(0)]
            if not doubleChild.isLeaf():
                self.left().addChildNode(doubleChild.left())
                doubleChild.removeChildNode(doubleChild.left())
        
    #fixes the node after a delete violation
    def fix(self):
        if self.isRoot():
            return
        
        p = self.parent
        if p.has2Items():
            p.merge()
        else:
            if p.getDoubleItemChild() is not None:
                p.redivide()
            else:
                p.merge()

    #loads in a 2-3 Tree from a given dictionary, the parent of the node is parent
    def load(self, d, parent):
        self.parent = parent
        self.items = d["root"]
        if "children" in d():
            self.children = list(d["children"])
            for i,child in enumerate(self.children):
                self.children[i] = Node()
                self.children[i].load(child, self)
    
    #returns a dictionary of the given node
    def save(self):
        d = {}
        d["root"] = self.items
        if not self.isLeaf():
            d["children"] = []
            for child in self.children:
                newD = {}
                if child is not None:
                    if child.isLeaf():
                        newD["root"] = child.items
                    else:
                        newD = child.save()  
                    d["children"].append(newD)
        return d

class TwoThreeTree:
    """
    TwoThreeTree object
    """
    def __init__(self) -> None:
        """
        Initialises a twothreetree with a root containing no items

        preconditions: None
        postconditions: Tree gets created
        """
        self.root = Node()
    
    #returns true if the tree is empty
    def isEmpty(self):
        return self.root.isEmpty()
    
    #traverses the tree inorder
    def inorderTraverse(self, func):
        self.root.inorderTraverse(func)

    def retrieveItem(self, item):
        """
        Retrieves an item from the tree

        preconditions: None
        postconditions: returns the value and True if found else return None and False
        """
        succes, item = self.root.retrieveItem(item)
        return [succes, item]
    
    def insertItem(self, item):
        """
        Inserts an item to the tree

        preconditions: None
        postconditions: Item gets inserted in the tree
                        Returns True if insertions is done
        """
        succes = self.root.insertItem(item)
        if succes:
            if self.root.parent is not None:
                self.root = self.root.parent
        return succes
    
    def deleteItem(self, item):
        """
        Deletes an item from the tree

        preconditions: None
        postconditions: Item gets deleted from the tree
                        Returns True if deletion is done
        """
        succes = self.root.deleteItem(item)
        if succes:
            if len(self.root.items)==0 and len(self.root.children) > 0:
                    self.root = self.root.children[0]
                    for child in self.root.children:
                        child.parent = self.root
                    self.root.parent = None
        return succes
    
    #loads a 2-3 tree in from given dictionary
    def load(self, d):
        self.root.load(d, None)

    #returns a dictionary containing info about the 2-3 tree
    def save(self):
        return self.root.save()