def createTreeItem(key,val):
    return Node(val)

class Node:
    """
    A twoThreeTree Node
    """
    def __init__(self, value=None) -> None:
        """
        Initialise the Node

        preconditions: None
        postconditions: Node gets created
        """
        self.values = []
        if value is not None:
            self.values = [value]  #create value list with value inside
        self.children = []
        self.parent = None
    
    #LT operator to sort nodes
    def __lt__(self, other):
        return self.values[-1]<other.values[0]
    
    #str operator to print values of node
    def __str__(self):
        s = ""
        for i,val in enumerate(self.values):
            if (i==len(self.values)-1):
                s+=str(val)
            else:
                s+= str(val) + "\n"
        return s
    
    #returns true if the node is a root
    def isRoot(self):
        return self.parent == None
    
    #returns true if the node is a leaf
    def isLeaf(self):
        return len(self.children) == 0
    
    #returns true if the node is empty
    def isEmpty(self):
        return len(self.values) == 0
    
    #returns true if the node has 2 items
    def has2Items(self):
        return len(self.values) == 2

    #returns true if the node has 3 items
    def has3Item(self):
        return len(self.values) == 3
    
    #returns true if the node contains the value
    def containsVal(self, searchval):
        for val in self.values:
            if val==searchval: #val found
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
            self.children[0].inorderTraverse(func)
            func(self.values[0])
            self.children[1].inorderTraverse(func)
            func(self.values[1])
            self.children[2].inorderTraverse(func)
        else:
            self.children[0].inorderTraverse(func)
            func(self.values[0])
            self.children[1].inorderTraverse(func)
    
    def retrieveItem(self, searchval):
        if self.containsVal(searchval):
            return [self, True]
        elif self.isLeaf():
            return [None, False]
        elif self.has2Items():
            if (searchval<self.values[0]):
                return self.children[0].retrieveItem(searchval)
            elif (searchval<self.values[2]):
                return self.children[1].retrieveItem(searchval)
            else:
                return self.children[2].retrieveItem(searchval)
        else:
            if (searchval<self.values[0]):
                return self.children[0].retrieveItem(searchval)
            else:
                return self.children[1].retrieveItem(searchval)
    
    #adds a value to the node and keeps the value sorted
    def addValue(self, val):
        self.values.append(val)
        self.values.sort()
    
    def insertToLeafNode(self, val):
        """ 
        adds a value to the corresponding leafnode of that value

        preconditions: None
        postconditions: adds a value to the corresponding leafnode of that value if its not already in the leaf
        """
        if (self.isLeaf()):
            self.addValue(val)
            return self
        elif self.has2Items():
            if (val<self.values[0]):
                return self.children[0].insertToLeafNode(val)
            elif (val<self.values[2]):
                return self.children[1].insertToLeafNode(val)
            else:
                return self.children[2].insertToLeafNode(val)
        else:
            if (val<self.values[0] or self.children[1]==None):
                return self.children[0].insertToLeafNode(val)
            else:
                return self.children[1].insertToLeafNode(val)
    
    def split(self):
        """
        Splits a node after insertion

        preconditions: The given node has 3 values
        postconditions: The given node gets split
        """
        if (self.isRoot()):
            p = Node()
            self.parent = p
        else:
            p = self.parent
            p.removeChildNode(self)
        
        n1 = Node(self.values[0])
        n1.parent = p
        n2 = Node(self.values[2])
        n2.parent = p
        p.addChildNode(n1)
        p.addChildNode(n2)
        p.addValue(self.values[1])

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

        if (p.has3Item()):
            p.split()

    def insertItem(self, treeItem):
        """
        Inserts an item to the right 2-3 Node
    
        preconditions: None
        postconditions: Item gets inserted into the 2-3 Node if its not already in the tree
        """
        val = treeItem.values[0]
        leafNode = self.insertToLeafNode(val)

        if (leafNode.has3Item()):
            leafNode.split()
        return True
    
    #returns the rightchild
    def right(self):
        return self.children[-1]

    #returns the leftchild
    def left(self):
        return self.children[0]
    
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

    def deleteItem(self, searchVal):
        """
        Deletes an item from the corresponding 2-3 Node

        preconditions: None
        postconditions: The requested value gets removed
                        returns bool (val deleted -> True else False)
        """
        node, succes = self.retrieveItem(searchVal)
        if succes:
            leaf = node
            if not node.isLeaf():
                leaf = node.inorderSuccessor()
                node.values.remove(searchVal)
                node.addValue(leaf.values[0])
                leaf.values.remove(leaf.values[0])
                leaf.addValue(searchVal)
            leaf.values.remove(searchVal)
            
            if len(leaf.values) == 0:
                leaf.fix()
            return True
        else:
            return False

    #returns a node that has 2 children and True or returns None and False if not found
    def hasChildw2Items(self):
        for child in self.children:
            if child is not None:
                if child.has2Items():
                    return [child ,True]
        return [None, False]

    #returns a node that has 1 child and True or returns None and False if not found
    def hasChildw1Item(self):
        for child in self.children:
            if child is not None:
                if len(child.values)==1:
                    return [child, True]
        return [None, False]
    
    #redistributes the values from the children of the node, the doublechild is left
    def redistributeLeft(self, doublechild, emptychild): 
        val = doublechild.values.pop()
        self.addValue(val)
        parentval = self.values.pop()
        emptychild.addValue(parentval)
        self.children.sort()
    
    #redistributes the values from the children of the node, the doublechild is right
    def redistributeRight(self, doublechild, emptychild):
        val = doublechild.values.pop(0)
        self.addValue(val)
        parentval = self.values.pop(0)
        emptychild.addValue(parentval)
        self.children.sort()
    
    #returns an empty child if no empty child return None
    def getEmptyChild(self):
        for child in self.children:
            if child.isEmpty():
                return child
        return None

    def merge(self):
        """
        Merges the parent with its children

        preconditions: The parent has 2 values or the parent has 1 value and no doublechild
        postconditions: Merges the parent with its children
        """
        emptyChild = self.getEmptyChild()
        self.removeChildNode(emptyChild)
        smallestChild = self.children[0]
        val = self.values.pop(0)
        smallestChild.addValue(val)
        smallestChild.children.extend(emptyChild.children)
        if len(self.values)==1:
            smallestChild.children.sort()
            for child in smallestChild.children:
                child.parent = self
            return
        else:
            smallestChild.children.extend(self.children)
            smallestChild.children.remove(smallestChild)
            smallestChild.children.sort()
            for child in smallestChild.children:
                child.parent = self
            smallestChild.parent = self.parent
            if len(self.values)==0 and not self.isRoot():
                self.parent.merge()

    #fixes the node after a delete violation
    def fix(self):
        if (self.isRoot()):
            self.children = self.children[0].children
            self.values = self.children[0].values
        else:
            p = self.parent
            if len(p.values)==2:
                p.merge()
            else:
                child, succes = p.hasChildw2Items()
                if succes:
                    if child == p.left():
                        p.redistributeLeft(child, self)
                    elif child==p.right():
                        p.redistributeRight(child, self)
                else:   
                    p.merge()

    #loads in a 2-3 Tree from a given dictionary, the parent of the node is parent
    def load(self, d, parent):
        self.parent = parent
        self.values = d["root"]
        if "children" in d.keys():
            self.children = list(d["children"])
            for i,child in enumerate(self.children):
                self.children[i] = Node()
                self.children[i].load(child, self)
    
    #returns a dictionary of the given node
    def save(self):
        d = {}
        d["root"] = self.values
        if not self.isLeaf():
            d["children"] = []
            for child in self.children:
                newD = {}
                if child is not None:
                    if child.isLeaf():
                        newD["root"] = child.values
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
        Initialises a twothreetree with a root containing no values

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

    def retrieveItem(self, searchVal):
        """
        Retrieves an item from the tree

        preconditions: None
        postconditions: returns the value and True if found else return None and False
        """
        item, succes = self.root.retrieveItem(searchVal)
        if succes:
            return [searchVal, True]
        else:
            return [None, False]
    
    def insertItem(self, treeItem):
        """
        Inserts an item to the tree

        preconditions: None
        postconditions: Item gets inserted in the tree
                        Returns True if insertions is done
        """
        succes = self.root.insertItem(treeItem)
        if succes:
            if self.root.parent is not None:
                self.root = self.root.parent
        return succes
    
    def deleteItem(self, val):
        """
        Deletes an item from the tree

        preconditions: None
        postconditions: Item gets deleted from the tree
                        Returns True if deletion is done
        """
        succes = self.root.deleteItem(val)
        if succes:
            if len(self.root.values)==0:
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

class TwoThreeTreeTable(TwoThreeTree):
    #Initialisation 2-3 tree Table
    def __init__(self) -> None:
        super().__init__()
    
    #Checks if the table is empty
    def tableIsEmpty(self):
        """
        Checks if the table is empty

        preconditions: None
        postconditions: Returns True if the table is empty
        """
        return self.isEmpty()
    
    #Inserts a TreeItem to the table
    def tableInsert(self, treeItem):
        """
        Inserts a TreeItem to the table

        TreeItem is of type twoThreeNode

        preconditions: None
        postconditions: The treeItem gets inserted to the table
        """
        return self.insertItem(treeItem)

    #Retrieves an item from the table
    def tableRetrieve(self, item):
        """
        Retrieves an item from the table

        preconditions: None
        postconditions: Returns a tuple (retrievedItem = item/None, done = True/False)
        """
        return self.retrieveItem(item)

    #Prints the table inorder
    def traverseTable(self,print):
        """
        Prints the table inorder

        preconditions: None
        postconditions: prints the table inorder
        """
        self.inorderTraverse(print)
    
    #Deletes an item from the table
    def tableDelete(self,item):
        """
        Deletes an item from the table

        item is the target for deletion

        preconditions: None
        postconditions: The given item gets deleted from the table
        """
        return self.deleteItem(item)