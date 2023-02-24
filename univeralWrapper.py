wrapper_insert = "insert"
wrapper_retrieve = "retrieve"


twoThreeTree_dict = {
    wrapper_insert : "searchTreeInsert",
    wrapper_retrieve : "searchTreeRetrieve"
}

bst_dict = {
    wrapper_insert : "searchTreeInsert",
    wrapper_retrieve : "searchTreeRetrieve"
}

class Wrapper(object):
    def __init__(self, datatype, funcNames) -> None:
        self.datatype = datatype
        self.funcMap = funcNames
    
    def __getattr__(self, attr) -> any:
        if attr not in self.__dict__:
            return getattr(self.datatype, self.funcMap[attr])
        return super().__getattr__(attr)