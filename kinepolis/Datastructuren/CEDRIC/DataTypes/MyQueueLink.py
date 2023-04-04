class QueueItemType:
    def __init__(self, value, next_value):
        """
        De container die gebruikt wordt voor de MyQueue klasse.

        :param value: De waarde die moet worden opgeslagen.
        :param next_value: De pointer naar de volgende waarde.
        """
        self.value = value
        self.next_value = next_value


class MyQueue:
    def __init__(self):
        """
        Creëert een lege stack.

        Pre-conditions:

        Post-conditions: Lege lijst is gecreëerd.
        """
        self.front = None
        self.back = None

    def isEmpty(self):
        """
        Bepaalt of een queue leeg is.

        Pre-conditions:

        Post-conditions: Lijst blijft ongewijzigd.

        :return:
        """
        if self.front is None:
            return True
        else:
            return False

    def getFront(self):
        """
        Plaatst de op van de queue in queueFront en laat de queue ongewijzigd.

        Pre-conditions: De queue moet minstens één element bevatten.

        Post-conditions: Lijst blijft ongewijzigd.

        :return: De functie geeft een tuple terug met respectievelijk de front value en een boolean die True terug geeft
         als de operatie gelukt is, False als de operatie niet gelukt is.
        """
        if self.front is None:
            return tuple((None, False))
        return tuple((self.front.value, True))

    def enqueue(self, newItem):
        """
        Voegt het element 'newItem' toe aan het eind van de queue.

        Pre-conditions:

        Post-conditions: 'newItem' is toegevoegd aan het einde van de queue.

        :param newItem: Het elmement dat moet worden toegevoegd aan de queue.
        :return: De funtie geeft True terug als de operatie succesvol is gelukt.
        """
        queueItem = QueueItemType(newItem, None)
        # Queue is niet leeg
        if self.back is not None:
            self.back.next_value = queueItem
        self.back = queueItem
        # Queue is leeg
        if self.front is None:
            self.front = self.back
        return True

    def dequeue(self):
        """
        Plaatst de kop van de queue in queueFront en verwijderd deze kop.

        Pre-conditions: De queue moet minstens een element bevatten.

        Post-conditions: De kop van de queue is vewijderd.

        :return: De functie geeft een tuple terug met respectievelijk de queueFront en een boolean die True is als de
        operatie is gelukt, False als de operatie is mislukt.
        """
        # Queue is leeg
        if self.front is None:
            return tuple((None, False))

        queueFront = self.front.value

        # Queue bevat één element
        if self.front == self.back:
            self.front = None
            self.back = None
            return tuple((queueFront, True))
        # Queue bevat meer dan één element
        self.front = self.front.next_value
        return tuple((queueFront, True))

    def save(self):
        """
        De queue wordt omgezet naar een list.

        Pre-conditions:

        Post-conditions: De lijst blijft ongewijzigd.

        :return: De functie geeft al de waarden van de queue terug in vorm van een lijst.
        """
        if self.front is None:
            return []
        search_element = self.front
        list_of_values = []
        while search_element is not None:
            list_of_values.append(search_element.value)
            search_element = search_element.next_value
        list_of_values.reverse()
        return list_of_values

    def load(self, list_to_queue):
        """
        De vorige waarden in de queue worden verwijderd in de lijst en de gegeven lijst wordt geladen in de queue.

        Pre-conditions:

        Post-conditions: De waarden van in de gegeven lijst zijn geladen in de queue.

        :param list_to_queue: De lijst met gegeven elementen die moeten geladen worden in de queue.
        """
        list_to_queue.reverse()
        self.front = None
        self.back = None
        for element in list_to_queue:
            self.enqueue(element)


if __name__ == "__main__":
    q = MyQueue()
    print(q.isEmpty())
    print(q.getFront()[1])
    print(q.dequeue()[1])
    print(q.enqueue(2))
    print(q.enqueue(4))
    print(q.isEmpty())
    print(q.dequeue()[0])
    q.enqueue(5)
    print(q.save())

    q.load(["a", "b", "c"])
    print(q.save())
    print(q.dequeue()[0])
    print(q.save())
    print(q.getFront()[0])
    print(q.save())
