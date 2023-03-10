from Datastructuren.ARNE.Datatypes.BST import BST, Item

class BSTTable(BST):
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
    def tableInsert(self, key):
        """
        Inserts a TreeItem to the table

        TreeItem is of type twoThreeNode

        preconditions: None
        postconditions: The treeItem gets inserted to the table
        """

        return self.searchTreeRetrieve(self.createItem(key, " ")).value

    #Retrieves an item from the table
    def tableRetrieve(self, item):
        """
        Retrieves an item from the table

        preconditions: None
        postconditions: Returns a tuple (retrievedItem = item/None, done = True/False)
        """
        return self.searchTreeRetrieve(item)

    #Prints the table inorder
    def traverseTable(self,print):
        """
        Prints the table inorder

        preconditions: None
        postconditions: prints the table inorder
        """
        self.inorderTraverse(print)
    
    #Deletes an item from the table
    def tableDelete(self, item):
        """
        Deletes an item from the table

        item is the target for deletion

        preconditions: None
        postconditions: The given item gets deleted from the table
        """
        return self.searchTreeDelete(item)

    def createItem(self, key, val):
        return Item(key, val)
    