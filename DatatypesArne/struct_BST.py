#Creates a TreeItem
def createTreeItem(key, value):
    """
    Creates a TreeItem

    key is the key of the node
    value is the value of the node

    preconditions: None
    postconditions: returns a Binary Search Tree Node
    """
    return BSTNode(key, value)

#Tree Node of Binary Search Tree
class BSTNode():
    #Initialisation Node
    def __init__(self, key=None, value=None) -> None:
        """
        Initialisation Node

        key is set to self.key, the default value is None
        value is set to self.value, the default value is None

        preconditions: None
        postconditions: A BSTNode is created
        """
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
    #Checks if the node is a leaf
    def isLeaf(self):
        """
        Checks if the node is a leaf

        preconditions: None
        postconditions: True if the node is a leaf, False if the node is not a leaf
        """
        return self.right==None and self.left==None
    
    #Checks if the node is empty
    def isEmpty(self):
        """
        Checks if the node is empty

        preconditions: None
        postconditions: True if the node is emtpy, False if the node is not empty
        """
        return self.value==None and self.key==None and self.left==None and self.right==None and self.parent==None

#Binary Search Tree
class BST():
    #Initialisation of Binary Search Tree
    def __init__(self) -> None:
        """
        Initialisation of Binary Search Tree
        
        Preconditions: None
        Postconditions: An empty BST is created
        """
        self.root = None
    
    #Checks if the Binary Search Tree is empty
    def isEmpty(self):
        """
        Checks if the Binary Search Tree is empty

        preconditions: None
        postconditions: True if the tree is emtpy, False if the tree is not empty
        """
        return self.root==None
    
    #Inserts a value to binary search Tree
    def searchTreeInsert(self, treeItem):
        """
        Inserts a value to binary search Tree

        treeItem is a Binary Search Tree Node

        preconditions: None
        postconditions: returns True if insertion worked
        """
        if self.isEmpty():
            self.root = treeItem
            return True
        return self._searchTreeInsert(treeItem, self.root)
    #Inserts a value to binary search Tree
    def _searchTreeInsert(self, treeItem, currentNode):
        """
        Inserts a value to binary search Tree

        treeItem is a Binary Search Tree Node
        currentNode is the node that is being processed

        preconditions: There is a root
        postconditions: returns True if insertion worked
        """
        if currentNode.value==treeItem.value:
            return True
        elif currentNode.value>treeItem.value:
            if currentNode.left==None:
                currentNode.left = treeItem
                currentNode.left.parent = currentNode
                return True
            else:
                self._searchTreeInsert(treeItem, currentNode.left)
        else:
            if currentNode.right==None:
                currentNode.right = treeItem
                currentNode.right.parent = currentNode
                return True
            else:
                self._searchTreeInsert(treeItem, currentNode.right)
    
    #Prints the Binary Search Tree inorder
    def inorderTraverse(self, print):
        """
        Prints the Binary Search Tree inorder

        print variable is unused but needed for Inginious

        preconditions: None
        postconditions: Prints the Binary Search Tree inorder
        """
        if self.root!=None:
            self._inorderTraverse(self.root)
    #Prints the Binary Search Tree inorder
    def _inorderTraverse(self, currentNode):
        """
        Prints the Binary Search Tree inorder

        print variable is unused but needed for Inginious
        currentNode is the node that is being processed

        preconditions: There is a root
        postconditions: Prints the Binary Search Tree inorder
        """
        if currentNode!=None:
            self._inorderTraverse(currentNode.left)
            print(currentNode.value)
            self._inorderTraverse(currentNode.right)
    
    #Searches a value in a Binary Search Tree
    def searchTreeRetrieve(self, value):
        """
        Searches a value in a Binary Search Tree

        preconditions: None
        postconditions: returns a tuple containing the value and a bool that is True when the value is found
        """
        if self.root!=None:
            return self._searchTreeRetrieve(value, self.root)
        else:
            return None, False
    #Searches a value in a Binary Search Tree
    def _searchTreeRetrieve(self, value, currentNode):
        """
        Searches a value in a Binary Search Tree

        currentNode is the node that is being processed

        preconditions: The root is not empty
        postconditions: returns a tuple containing the value and a bool that is True when the value is found
        """
        if currentNode.value==value:
            return value, True

        if value<currentNode.value and currentNode.left!=None:
            return self._searchTreeRetrieve(value, currentNode.left)
        elif value>currentNode.value and currentNode.right!=None:
            return self._searchTreeRetrieve(value, currentNode.right)
        return (None, False)
    
    #Saves the contents of a Binary Search Tree
    def save(self):
        """
        Saves the contents of a Binary Search Tree

        preconditions: None
        postconditions: returns a dictionary describing the root, children and its values of a Binary Search Tree
        """
        if self.root!=None:
            return self._save(self.root)
        return {}
    #Saves the contents of a Binary Search Tree
    def _save(self, currentNode):
        """
        Saves the contents of a Binary Search Tree
        
        currentNode is the node that is being processed

        preconditions: None
        postconditions: returns a dictionary describing the root, children and its values of a Binary Search Tree
        """
        d = {}
        d["root"] = currentNode.value
        if not currentNode.isLeaf():
            d["children"] = [None, None]
            if type(currentNode.left)==BSTNode:
                if not currentNode.left.isEmpty():
                    d["children"][0] = self._save(currentNode.left)
            if type(currentNode.right)==BSTNode:
                if not currentNode.right.isEmpty():
                    d["children"][1] = self._save(currentNode.right)
        return d

    #loads a new binary search tree
    def load(self, dictIn):
        """
        Loads a new binary search tree

        dictIn is a dictionary in the right format

        preconditions: None
        postconditions: Creates a new Binary Search Tree with the right elements
        """
        self.root = BSTNode()
        self._load(dictIn, self.root)
    def _load(self, dictIn, currentNode):
        """
        Loads a new binary search tree

        dictIn is a dictionary in the right format
        currentNode is the node that is being processed

        preconditions: None
        postconditions: Creates a new Binary Search Tree with the right elements
        """
        currentNode.value = dictIn["root"]
        if "children" in dictIn.keys():
            leftTree = dictIn["children"][0]
            rightTree = dictIn["children"][1]
            if type(leftTree)==dict:
                currentNode.left = BSTNode()
                currentNode.left.parent = currentNode
                self._load(leftTree, currentNode.left)
            else:
                currentNode.left = leftTree
            if type(rightTree)==dict:
                currentNode.right = BSTNode()
                currentNode.right.parent = currentNode
                self._load(rightTree, currentNode.right)
            else:
                currentNode.right = rightTree
    
    #Deletes a node from the binary search tree
    def searchTreeDelete(self, value):
        """
        Deletes a node from the binary search tree
        
        value is the value of the node that needs to be deleted

        preconditions: None
        postconditions: returns True if the value is deleted from the tree
        """
        node = self.find(value)
        if node!=None:
            self.deleteNode(node)
            return True
        return False
    #Deletes a node
    def deleteNode(self, node):
        """
        Deletes a node

        node is the node that needs to get deleted

        preconditions: the value has to be in the binary search tree
        postconditions: deletes a node from the binary search tree
        """
        #returns the node with the smallest value
        def getMinNode(n):
            """
            returns the node with the smallest value

            n is a node item

            preconditions: None
            postconditions: returns the node with the smallest value
            """
            min=n
            while min.left!=None:
                min=min.left
            return min
        #returns the amount of children a node has
        def childrenAmount(node):
            """
            returns the amount of children a node has

            node is the node that is being processed

            preconditions: None
            postconditions: returns the amount of children the given node has
            """
            amount = 0
            if node.left!=None: 
                amount+=1
            if node.right!=None:
                amount+=1
            return amount

        parent = node.parent
        children = childrenAmount(node)
        if node.isLeaf():
            if parent.left==node:
                parent.left=None
            else:
                parent.right=None
                
        if children==1:
            if node.left!=None:
                child = node.left
            else:
                child = node.right
            if parent.left==node:
                parent.left=child
            else:
                parent.right=child
            child.parent = parent

        if children==2:
            successor = getMinNode(node.right)
            node.value = successor.value
            self.deleteNode(successor)

    #finds a value in the binary search tree
    def find(self, value):
        """
        finds a value in the binary search tree

        value is the value that is being searched

        preconditions:  None
        postconditions: returns the node if the value is in the tree, else returns None
        """
        if self.root!=None:
            return self._find(value, self.root)
        return None
    #finds a value in the binary search tree
    def _find(self, value, currentNode):
        """
        finds a value in the binary search tree

        value is the value that is being searched
        currentNode is the node that is being processed

        preconditions:  None
        postconditions: returns the node if the value is in the tree, else returns None
        """
        if value==currentNode.value:
            return currentNode

        if value<currentNode.value and currentNode.left!=None:
            return self._find(value, currentNode.left)
        elif value>currentNode.value and currentNode.right!=None:
            return self._find(value, currentNode.right)
        return None