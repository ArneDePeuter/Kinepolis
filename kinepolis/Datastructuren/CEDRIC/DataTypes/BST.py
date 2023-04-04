def createTreeItem(key, val):
    """
    Functie creëert een item voor een binaire boom terug

    Pre-conditions: \

    Post-conditions: Item van het type TreeItem is aangemaakt.

    :param key: De waarde van de key
    :param val: De waarde van de value
    :return: Geeft een item terug van het type TreeItem
    """
    return TreeItem(key, val)


class TreeItem:
    def __init__(self, key, value):
        """
        De container die wordt gebruikt in de klasse BST

        Pre-conditions: \

        Post-conditions: Een item van type TreeItem is aangemaakt

        :param key: De key van een item in een BST
        :param value: De value die aan een key gekoppeld is van een item in een BST
        """
        self.key = key
        self.value = value

    def __str__(self):
        """
        Functie die manier op hoe dat een TreeItem moet worden moet naar een string definieert.

        Pre-conditions: \

        Post-conditions: \

        :return: De correct geformatteerde string wordt terug gegeven
        """
        return str(self.value)


class BST:
    def __init__(self):
        """
        Creëert een Binary Search Tree (BST). item, leftBST en rightBST worden op None gezet, omdat geen waarden worden mee
        gegeven.

        Pre-conditions: \

        Post-conditions: Er is een binary search tree aangemaakt.

        """
        self.item = None
        self.leftBST = None
        self.rightBST = None

    def isEmpty(self):
        """
        Functie die kijkt of de BST leeg is of niet.

        Pre-conditions: \

        Post-conditions: \

        :return: De functie geeft een boolean terug, die true is als de BST leeg is, False als de BST item(s) bevat.
        """
        if self.item is None:
            return True
        else:
            return False

    def searchTreeInsert(self, item):
        """
        Functie die een item toe voegt aan de BST op de correcte plaats.

        Pre-conditions: \

        Post-conditions: Het meegeven item is toegevoegd aan de BST.


        :param item: Het item dat moet worden toegevoegd.
        :return: Als het item is toegevoegd geeft die functie True terug.
        """
        # if BST is empty
        if self.item is None:
            self.item = item
            return True

        # if BST has key that is bigger than key of item
        if item.key < self.item.key:
            if self.leftBST is None:
                self.leftBST = BST()
            self.leftBST.searchTreeInsert(item)
            return True

        # if BST has key that is smaller than key of item
        if item.key > self.item.key:
            if self.rightBST is None:
                self.rightBST = BST()
            self.rightBST.searchTreeInsert(item)
            return True

        # if BST key is equal to item key
        if self.item.key == item.key:
            self.item.value = item.value
            return True

    def searchTreeRetrieve(self, searchKey):
        """
        Functie die de value zoekt die bij een gegeven key hoort, als de key in de boom zit.

        Pre-conditions: \

        Post-conditions: \
        :param searchKey: De waarde van de key die moet worden gezocht.
        :return: De functie geeft een tuple terug, in het geval dat de key gevonden is, geeft de functie (value, True)
        terug, in het geval dat de key niet gevonden is (None, False).
        """
        if self.item is None:
            return tuple((None, False))

        # if searchKey is key of current BST
        if searchKey == self.item.key:
            return tuple((self.item, True))

        # if searchKey is smaller than current key of BST
        elif searchKey < self.item.key and self.leftBST is not None:
            return self.leftBST.searchTreeRetrieve(searchKey)

        # if searchKey is bigger than current key of BST
        elif searchKey > self.item.key and self.rightBST is not None:
            return self.rightBST.searchTreeRetrieve(searchKey)

        # if key is not found
        else:
            return tuple((None, False))

    def inorderTraverse(self, FunctionType):
        """
        Functie die een BST in inorder terug geeft.

        Pre-conditions: \

        Post-conditions: \

        :param FunctionType: Meegegeven functie, die inorderTraverse gebruikt.
        :return: \
        """

        if self.leftBST is not None:
            self.leftBST.inorderTraverse(FunctionType)

        FunctionType(self.item)

        if self.rightBST is not None:
            self.rightBST.inorderTraverse(FunctionType)

    def save(self):
        """
        Functie die een BST om zet naar een string.

        Pre-conditions: \

        Post-conditions: \

        :return: De functie geeft een string terug.
        """
        result = ""
        result += "{'root': " + str(self.item.key)

        if (self.leftBST is not None and self.leftBST.item is not None) or (
            self.rightBST is not None and self.rightBST.item is not None
        ):
            result += ",'children':["

            if self.leftBST is not None and self.leftBST.item is not None:
                result += self.leftBST.save()
            else:
                result += "None"

            result += ","

            if self.rightBST is not None and self.rightBST.item is not None:
                result += self.rightBST.save()
            else:
                result += "None"

            result += "]"

        result += "}"
        return result

    def searchTreeDelete(self, searchKey):
        """
        Functie verwijderd een item uit de BST met als key gelijk aan de searchKey.

        Pre-conditions: \

        Post-conditions: Als het item met als key gelijk aan searchKey in de BST zit wordt deze verwijderd uit de BST.
        De BST zal voldoen aan de voorwaarden van een BST.

        :param searchKey: De waarde van de key voor het item dat moet worden verwijderd.
        :return: De functie geeft een boolean terug, True als het item met de gegeven key gevonden werd en verwijderd
        werd, False als de gegeven key niet in de BST zit.
        """
        # if searchKey is smaller than current key of BST
        if searchKey < self.item.key and self.leftBST is not None:
            return self.leftBST.searchTreeDelete(searchKey)

        elif searchKey < self.item.key and self.leftBST is None:
            return False

        # if searchKey is bigger than current key of BST
        elif searchKey > self.item.key and self.rightBST is not None:
            return self.rightBST.searchTreeDelete(searchKey)

        elif searchKey > self.item.key and self.rightBST is None:
            return False

        # if searchKey is equal to current key of BST
        else:
            if self.leftBST is None and self.rightBST is None:
                # case 1: no children
                self.item = None
                return True

            if self.leftBST is None:
                # case 2: only right children
                self.item = self.rightBST.item
                self.leftBST = self.rightBST.leftBST
                self.rightBST = self.rightBST.rightBST
                return True

            if self.rightBST is None:
                # case 3: only left children
                self.item = self.leftBST.item
                self.rightBST = self.leftBST.rightBST
                self.leftBST = self.leftBST.leftBST
                return True

            # case 4: both children
            rightSuccessor = self.rightBST.__findMin()

            self.item = rightSuccessor
            if rightSuccessor is not None:
                self.rightBST.searchTreeDelete(rightSuccessor.key)

            return True

    def __findMin(self):
        """
        Functie die de kleinste key waarde zoekt in een BST.

        Pre-conditions: \

        Post-conditions: \

        :return: De functie geeft het item met de kleinste key terug.
        """
        if self.leftBST is not None:
            return self.leftBST.__findMin()
        else:
            return self.item

    def load(self, data):
        """
        Functie laadt een BST met items die in items zitten.

        Pre-conditions: \

        Post-conditions: De items die in items zitten worden ingeladen in de BST.

        :param data: Dictionary met de items er in die moeten worden ingeladen.
        :return: \
        """
        if data is None:
            return
        else:
            # self.item, self.leftBST, self.rightBST = None, BST, BST

            self.item = TreeItem(data.get("root"), data.get("root"))

            if data.get("children") is not None:
                if data.get("children")[0] is not None:
                    self.leftBST = BST()
                    self.leftBST.load(data.get("children")[0])
                else:
                    self.leftBST = None

                if data.get("children")[1] is not None:
                    self.rightBST = BST()
                    self.rightBST.load(data.get("children")[1])
                else:
                    self.rightBST = None


if __name__ == "__main__":
    t = BST()
    t.load(
        {
            "root": 100,
            "children": [
                {
                    "root": 50,
                    "children": [
                        {"root": 20},
                        {"root": 90, "children": [{"root": 70}, None]},
                    ],
                },
                {"root": 200, "children": [{"root": 120}, {"root": 210}]},
            ],
        }
    )
    t.searchTreeDelete(90)
    t.searchTreeDelete(70)
    t.searchTreeDelete(100)
    print(t.save())
