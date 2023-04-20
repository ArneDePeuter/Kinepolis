class TableItem:
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

    def __str__(self):
        """
        Functie die manier op hoe dat een TableItem moet worden moet naar een string definieert.

        Pre-conditions: \

        Post-conditions: \

        :return: De correct geformatteerde string wordt terug gegeven
        """
        return str(self.value)
