from DatatypesArne import struct_BST
from DatatypesArne import struct_234Tree

class Wrapper(object):
    def __init__(self, datatype, funcNames) -> None:
        self.datatype = datatype
        self.funcMap = funcNames
    
    def __getattr__(self, attr) -> any:
        if attr not in self.__dict__:
            return getattr(self.datatype, self.funcMap[attr])
        return super().__getattr__(attr)

bst = Wrapper(struct_BST.BST(), {"insert": "searchTreeInsert"})
print(bst.insert(5))

twotreefourTree = Wrapper(struct_234Tree.twoThreeFourTree(), {"insert": "insert"})
print(twotreefourTree.insert(5))

