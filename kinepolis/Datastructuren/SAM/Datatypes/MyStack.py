# Implementatie van een arraybased stack
class StackItemType:
    def __int__(self, value):
        self.value = value


class MyStack:
    def __init__(self, max):
        """
        Lege stack maken
        Pre-condition : maximum grote groter dan 0
        Post-condition : lege stack aangemaakt
        :param max: maximum grootte van de stack
        """
        self.items = [None] * max
        self.size = 0

    def push(self, NieuwElement):
        """
        Pre-condition : Een leeg plaatstje in de stack
        Post-condition : Het nieuwe element op de eerste vrije plek in de stack plaatsen.
        :param NieuwElement: Het toe te voegen element
        """
        if self.size == len(self.items):
            return False
        else:
            self.items[self.size] = NieuwElement
            self.size += 1
            return True

    def isEmpty(self):
        """
        geen condities
        :return: True indien stack leeg is, false indien stack niet leeg is
        """
        if self.size == 0:
            return True
        else:
            return False

    def getTop(self):
        """
        Pre-conditions : geen lege stack
        Post-conditions : waarde op laatste plek gegeven
        :return:
        """
        if self.size == 0:
            return False, False
        else:
            return self.items[self.size - 1], True

    def pop(self):
        """
        Pre-conditions: De stack mag niet leeg zijn.
        Post-conditions: Laatste element moet verwijderd zijn.
        """
        if self.size == 0:
            return False, False
        else:
            x = self.items[self.size - 1]
            self.items[self.size - 1] = None
            self.size = self.size - 1
            return x, True

    def save(self):
        l = self.items[0 : self.size]
        return l

    def load(self, stack):
        self.items = stack
        self.size = len(stack)
