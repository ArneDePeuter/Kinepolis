def readFile(self, fileName):
    """
    Leest een bestand met de geven naam in

    Preconditie: Het bestand moet bestaan
    Postconditie: Het bestand is ingelezen adhv de content worden er wijzigingen in het reservatiesysteem gedaan

    :param fileName: De naam van het in te lezen bestand
    :return: True als de operatie is gelukt, False als het niet gelukt is.
    """
    # open het bestand
    with open(fileName, "r") as file:
        # lees elke regel in het bestand
        for line in file:
            # als de regel begint met '#' sla de regel over
            if line.startswith("#"):
                continue
            else:
                # Kijk of de regel start met init zo ja dan maak je aan
                if (line.startswith("gebruiker")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    voornaam = parts[2]
                    achternaam = parts[3]
                    email = parts[4]
                    # Maak de gebruiker aan
                    gebruiker = Gebruiker(id, voornaam, achternaam, email)
                    tableItem = self.users.createItem(gebruiker.id, gebruiker)
                    self.users.tableInsert(tableItem)