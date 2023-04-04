class MyStack:
    def __init__(self, max_size):
        """
        Creëert een lege stack met grote max_size.

        Preconditions: max_size > 0

        Postconditions: Er is een lege stack aangemaakt met groote 'max_size'

        :param max_size: De grootte van de stack
        """
        self.items = [None] * max_size
        self.size = 0
        self.stackTop = None

    def isEmpty(self):
        """
        Bepaalt of een stack leef is.

        Preconditions: /

        Postconditions: De stack is ongewijzigd.

        :return: De functie geeft 'True' terug als de stack leeg is, en 'False' als de stack niet leef is
        """
        if self.size == 0:
            return True
        else:
            return False

    def push(self, newItem):
        """
        Voegt het element 'newItem' toe op de top van een stack.

        Preconditions: De stack zit niet vol.

        Postconditions: Het element 'newItem' is toegevoegd aan de stack.

        :param newItem: De item die op de top van de stack moet geplaatst worden.
        :return: Functie geeft True terug als 'newItem' aan de stack is toegevoegd
        """
        if self.size == len(self.items):
            return False
        self.items[self.size] = newItem
        self.size += 1
        return True

    def pop(self):
        """
        Verwijdert de top van een stack, d.i. het laatste toegevoegde element.

        Preconditions: De stack moet meer dan 1 element bevatten.

        Postconditions: De top van de stack is verwijderd.

        :return: De functie geeft een tuple terug met respectievelijk de stackTop en een Boolean, True als de operatie
        gelukt is, false als er geen elementen kan verwijderd worden.
        """
        if self.size == 0:
            return tuple((self.stackTop, False))
        self.stackTop = self.items[self.size - 1]
        self.items[self.size - 1] = None
        self.size -= 1
        return tuple((self.stackTop, True))

    def getTop(self):
        """
        Plaatst de top van een stack in 'stackTop' en laat de stack ongewijzigd.

        Preconditions: De stack moet minstens een element bevatten.

        Postconditions: De stack is ongewijzigd

        :return: De functie geeft een tuple terug met respectievelijk de stackTop en een boolean, True als de operatie
        gelukt is, false als er geen elementen kan verwijderd worden.
        """
        if self.size == 0:
            return tuple((self.stackTop, False))
        self.stackTop = self.items[self.size - 1]
        return tuple((self.stackTop, True))

    def save(self):
        """
        De functie geeft al de elementen in de stack terug in vorm van een lijst.

        Preconditie:

        Postconditie: De lijst is ongewijzigd.

        :return: De functie geeft al de elementen in de stack terug in vorm van een lijst.
        """
        return self.items[0 : self.size]

    def load(self, list_to_stack):
        """
        De functie steekt een gegeven lijst in de stack.

        Preconditie:

        Postconditie: De gegeven lijst zit in de stack.

        :param list_to_stack: De gegeven lijst die in de stack wordt gestoken.
        :return: De functie geeft de stack terug met de gegeven lijst er in vorm van een lijst.
        """
        self.items = list_to_stack
        self.size = len(self.items)
        return self.items


if __name__ == "__main__":
    s = MyStack(2)
    print(s.isEmpty())
    print(s.getTop()[1])
    print(s.pop()[1])
    print(s.push(2))
    print(s.push(4))
    print(s.push(1))
    print(s.isEmpty())
    print(s.pop()[0])
    s.push(5)
    print(s.save())

    s.load(["a", "b", "c"])
    print(s.save())
    print(s.pop()[0])
    print(s.save())
    print(s.getTop()[0])
    print(s.save())

# Verwacht:
#
# True
# False
# False
# True
# True
# False
# False
# 4
# [2,5]
# ['a','b','c']
# c
# ['a','b']
# b
# ['a','b']
