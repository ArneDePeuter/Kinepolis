from Datastructuren.ARNE.Datatypes.TwoThreeTree import TwoThreeTree, Item

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
    def tableInsert(self, item):
        """
        Inserts a TreeItem to the table

        TreeItem is of type twoThreeNode

        preconditions: None
        postconditions: The treeItem gets inserted to the table
        """
        return self.insertItem(item)

    #Retrieves an item from the table
    def tableRetrieve(self, key):
        """
        Retrieves an item from the table

        preconditions: None
        postconditions: Returns a tuple (done = True/False, retrievedItem = item/None)
        """
        dummyitem = self.createItem(key, "dummyVal")
        result = self.retrieveItem(dummyitem)
        if result[1]:
            for item in result[0].items:
                if item==dummyitem:
                    break
            return item.val, result[1]
        else:
            return None, False

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
        return self.deleteItem(item)

    def createItem(self, key, val):
        return Item(key, val)
    