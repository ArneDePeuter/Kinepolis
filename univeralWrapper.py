wrapper_empty           = "isEmpty"
wrapper_insert          = "insert"
wrapper_retrieve        = "retrieve"
wrapper_delete          = "delete"
wrapper_inorderTraverse = "inorderTraverse"
wrapper_load            = "load"
wrapper_save            = "save"
wrapper_createItem      = "createItem"

twoThreeTree_dict = {
    wrapper_empty : "isEmpty",
    wrapper_insert : "insertItem",
    wrapper_retrieve : "retrieveItem",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "",
    wrapper_createItem : "createTreeItem"
}

twoThreeFourTree_dict = {
    wrapper_empty : "isEmpty",
    wrapper_insert : "insertItem",
    wrapper_retrieve : "retrieveItem",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "",
    wrapper_createItem : "createTreeItem"
}

bst_dict = {
    wrapper_empty : "isEmpty",
    wrapper_insert : "searchTreeInsert",
    wrapper_retrieve : "searchTreeRetrieve",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "",
    wrapper_createItem : "createTreeItem"
}

hashmap_dict = {
    wrapper_empty : "isEmpty",
    wrapper_insert : "insertItem",
    wrapper_retrieve : "retrieveItem",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "",
    wrapper_createItem : "createTreeItem"
}

heap_dict = {
    wrapper_empty : "isEmpty", 
    wrapper_insert : "insertItem",
    wrapper_retrieve : "retrieveItem",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "",
    wrapper_createItem : "createTreeItem"
}

linkedList_dict = {
    wrapper_empty : "isEmpty", 
    wrapper_insert : "insertItem",
    wrapper_retrieve : "retrieveItem",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "", 
    wrapper_createItem : "createTreeItem"
}

queue_dict = {
    wrapper_empty : "isEmpty", 
    wrapper_insert : "insertItem",
    wrapper_retrieve : "retrieveItem",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "",
    wrapper_createItem : "createTreeItem"
}

stack_dict = {
    wrapper_empty : "isEmpty", 
    wrapper_insert : "insertItem",
    wrapper_retrieve : "retrieveItem",
    wrapper_delete : "",
    wrapper_inorderTraverse : "",
    wrapper_load : "",
    wrapper_save : "",
    wrapper_createItem : "createTreeItem"
}

class UniversalWrapper(object):
    def __init__(self, datatype, funcNames) -> None:
        self.datatype = datatype
        self.funcMap = funcNames
    
    def __getattr__(self, attr) -> any:
        if attr not in self.__dict__:
            return getattr(self.datatype, self.funcMap[attr])
        return super().__getattr__(attr)