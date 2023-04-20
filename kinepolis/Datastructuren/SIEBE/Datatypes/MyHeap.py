"""
    Implementatie van een Linked Based Heap
"""

def createItem(key, val):
    return Item(key, val)

class Item:
    """"
        cfr. heap Arne toegevoeging in fuctie van item met key and valkey, val
    """
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


class heapItem:
    def __init__(self, item=None):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een heapItemType, dit is het type van de elementen
            in de heap. Een element van dit type heeft een zoeksleutel
        -------------------------------------------------------
        Pre-condition:
            /
        Post-condition:
            Een heapItem is aangemaakt
        -------------------------------------------------------
        """
        self.left = None
        self.right = None
        self.item = item
        self.parent = None

    """
    -------------------------------------------------------
    Beschrijving:
        Alle helpfuncties die worden gebruikt voor het 
        bewerkingscontract te kunnen nakom.
    -----
    """

    def isLeaf(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een heapItem een blad is.
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            Returns True als het heapItem een blad is, zo niet False.
        -------------------------------------------------------
        """
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def getLastHeapItem(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Zoek naar het meest rechtse item onderaan.
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            Het laatste heapItem wordt ge returned
        -------------------------------------------------------
        """
        if self.isLeaf():
            return self
        if self.right:
            return self.right.getLastHeapItem()
        else:
            return self.left.getLastHeapItem()

    def swap(self, other):
        """
        -------------------------------------------------------
        Beschrijving:
            Wisselt 2 heap items van plaats
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            De 2 heap items werden van plaats verwisselt
        -------------------------------------------------------
        """
        heapItemKey = self.item
        otherKey = other.item
        self.item = otherKey
        other.item = heapItemKey

    def fix(self, lastHeapItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze functie is verantwoordelijk voor het behouden van de heap-eigenschappen
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            De heap bevat alle heap-eigenschappen
        -------------------------------------------------------
        """
        if lastHeapItem.parent is not None:
            lastHeapItem.parent.removeChild(lastHeapItem)
        newTreeItem = heapItem(lastHeapItem.item)
        newTreeItem.parent = self
        if self.left is None:
            self.left = newTreeItem
        elif self.right is None:
            self.right = newTreeItem

    def heapifyUp(self, operator):
        """
        -------------------------------------------------------
        Beschrijving:
            Wordt gebruik na het invoegen van een item in de heap, om
            de heap zijn heap-eigenschappen te laten behouden
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            De heap bevat alle eigenschappen van een heap
        -------------------------------------------------------
        """
        if self.parent is not None:
            if operator(self, self.parent) == self:
                self.swap(self.parent)
                self.parent.heapifyUp(operator)

    def __lt__(self, other):
        return self.item.key < other.item.key

    def __gt__(self, other):
        return self.item.key > other.item.key

    def heapifyDown(self, operator):
        """
        -------------------------------------------------------
        Beschrijving:
            Wordt gebruik na het invoegen van een item in de heap, om
            de heap zijn heap-eigenschappen te laten behouden
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            De heap bevat alle eigenschappen van een heap
        -------------------------------------------------------
        """
        if self.left is not None:
            if operator(self.left, self) == self.left:
                self.swap(self.left)
                self.left.heapifyDown(operator)
        if self.right is not None:
            if operator(self.right, self) == self.right:
                self.swap(self.right)
                self.right.heapifyDown(operator)

    def insertComplete(self, item):
        """
        -------------------------------------------------------
        Beschrijving:
            Hulp functie die word gebruikt bij het inserten van een item in de heap
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            De heap bevat alle eigenschappen van een heap
        -------------------------------------------------------
        """
        newNode = heapItem(item)
        newNode.parent = self
        if self.left is None:
            self.left = newNode
        elif self.right is None:
            self.right = newNode
        elif self.left is not None:
            return self.left.insertComplete(item)
        elif self.right is not None:
            return self.right.insertComplete(item)
        return newNode

    def removeChild(self, child):
        """
        -------------------------------------------------------
        Beschrijving:
            Verwijderd een kind
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            Het kind werd verwijderd
        -------------------------------------------------------
        """
        if child == self.left:
            self.left = None
        else:
            self.right = None


class Heap:
    def __init__(self, maxHeap=True):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege min-/ max-heap a.d.h.v. de opgegeven
            :param maxHeap
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            Er is een heap aangemaakt
        -------------------------------------------------------
        """
        self.root = heapItem()
        self.maxHeap = maxHeap

    def get_comparison_operator(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of we moeten kijken voor groter of kleiner dan
        -------------------------------------------------------
        Preconditite:
            Er is een heap aangemaakt
        Post-conditions:
            We kunnen een min- of max heap maken
        -------------------------------------------------------
        """
        if self.maxHeap:
            return max
        else:
            return min

    def heapIsEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een heap leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            Returns True als de BST leeg is, zo niet False.
        -------------------------------------------------------
        """
        if self.root.item is None:
            return True
        else:
            return False

    def heapInsert(self, newItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Voegt newItem toe aan eenheap met items met unieke zoeksleutels
            verschillend van de zoeksleutel van newItem
        -------------------------------------------------------
        Preconditite:
            Er moet eerst een heap aangemaakt zijn
        Post-conditions:
            Het newItem wordt aan de heap toegevoegd, gesorteerd
            volgens het type van de heap.
        -------------------------------------------------------
        Return : True geeft weer dat het toevoegen gelukt is anders False
        -------------------------------------------------------
        """
        if self.heapIsEmpty():
            self.root.item = newItem
            return True
        newNode = self.root.insertComplete(newItem)
        comparisonOperator = self.get_comparison_operator()
        newNode.heapifyUp(comparisonOperator)
        return True

    def heapDelete(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Verwijderd rootItem uit de heap
            Het element met de grootste zoeksleutel (bij een max-heap) of
            het element met de kleinste zoeksleutel (bij een min-heap)
            wordt verwijderd.
        -------------------------------------------------------
        Preconditite:
            Er moet eerst een heap aangemaakt zijn
        Post-conditions:
            Het root wordt uit de heap verwijderd, afhankelijk van max of min heap
        -------------------------------------------------------
        Return : True geeft weer dat het verwijderen gelukt is anders False
        -------------------------------------------------------
        """
        # Kijkt of de heap leeg is
        if self.heapIsEmpty():
            return (None, False)
        if self.root.isLeaf():
            rootItem = self.root.item
            self.root = heapItem()
            return (rootItem, True)
        # Slaagt de key van de root op
        rootItem = self.root.item
        # Zoek het meest rechtse item onderaan
        lastItem = self.root.getLastHeapItem()
        # Plaats het meest rechtse item in de root
        self.root.swap(lastItem)
        # Kijkt of het meest rechtse item een parent heeft
        if lastItem.parent is not None:
            # Zo ja dan verwijder je
            lastItem.parent.removeChild(lastItem)
        comparisonOperator = self.get_comparison_operator()
        self.root.heapifyDown(comparisonOperator)
        if lastItem.parent is not None and self.root.left is not None and self.root.right is not None:
            temp = self.root.getLastHeapItem().parent
            l = temp.left
            r = temp.right
            comparisonOperator = self.get_comparison_operator()
            if l == None:
                lastItem.parent.fix(r)
            elif r == None:
                lastItem.parent.fix(l)
            elif comparisonOperator(l, r) == l:
                lastItem.parent.fix(r)
            elif comparisonOperator(l, r) == r:
                lastItem.parent.fix(l)
                temp.left = r
                temp.right = None
        return (rootItem, True)

    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode stelt een heap voor als een dict.
        -------------------------------------------------------
        Preconditite:
            De heap mag niet leeg zijn
        Post-conditions:
            De waarden van de zoeksleutels worden weergegeven in een dict.
        -------------------------------------------------------
        """

        def save_heap(heapItem):
            data = {}
            if heapItem is None:
                return None
            data["root"] = heapItem.key
            if heapItem.left is not None or heapItem.right is not None:
                data["children"] = []
                if heapItem.left is not None:
                    data["children"].append(save_heap(heapItem.left))
                else:
                    data["children"].append(None)
                if heapItem.right is not None:
                    data["children"].append(save_heap(heapItem.right))
                else:
                    data["children"].append(None)
            return data

        return save_heap(self.root)

    def load(self, data):
        """
        -------------------------------------------------------
        Beschrijving:
            Deze methode laad een dict. in als een heap
        -------------------------------------------------------
        Preconditite:
            /
        Post-conditions:
            De dict. wordt ingeladen als een heap, met voor elke heapItem
            de key gelijk aan de val van de 'root' key
        -------------------------------------------------------
        """

        def load_bst(dict, parent):
            # Checkt of de dict niet leeg is
            if dict is None:
                return None
            # Maakt een knoop aan voor de root, met als key de value die de root key heeft
            node = heapItem(dict["root"])
            node.parent = parent
            # Kijk of er kinderen zijn
            if "children" in dict:
                # Kijkt op linker kinderen
                if dict["children"][0] is not None:
                    node.left = load_bst(dict["children"][0], node)
                else:
                    None
                # Kijkt op rechter kinderen
                if len(dict["children"]) > 1 and dict["children"][1] is not None:
                    node.right = load_bst(dict["children"][1], node)
                else:
                    None
            return node

        # Zet de ingeladen BST gelijk aan onze self.root
        self.root = load_bst(data, None)