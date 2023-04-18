from ..Datatypes.BST import BST, Item

class BSTTable:
    # Initialisation 2-3 tree Table
    def __init__(self) -> None:
        self.bst = BST()

    # Checks if the table is empty
    def tableIsEmpty(self):
        """
        Checks if the table is empty
        Pre-conditions: None
        Post-conditions: Returns True if the table is empty
        """
        return self.bst.isEmpty()

    # Inserts a TreeItem to the table
    def tableInsert(self, key, val):
        """
        Inserts a TreeItem to the table
        TreeItem is of type twoThreeNode
        Pre-conditions: None
        Post-conditions: The treeItem gets inserted to the table
        """
        return self.bst.searchTreeInsert(Item(key, val))

    # Retrieves an item from the table
    def tableRetrieve(self, key):
        """
        Retrieves an item from the table
        Pre-conditions: None
        Post-conditions: Returns a tuple (retrievedItem = item/None, done = True/False)
        """
        item, succes = self.bst.searchTreeRetrieve(Item(key,key))
        if succes:
            return item.item, succes
        return False, None
    
    # Prints the table inorder
    def traverseTable(self, func):
        """
        Prints the table inorder
        Pre-conditions: None
        Post-conditions: prints the table inorder
        """
        self.bst.inorderTraverse(func)

    # Deletes an item from the table
    def tableDelete(self, item):
        """
        Deletes an item from the table
        item is the target for deletion
        Pre-conditions: None
        Post-conditions: The given item gets deleted from the table
        """
        return self.bst.searchTreeDelete(item)