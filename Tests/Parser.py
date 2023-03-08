from Reservatiesysteem import *
def readFile(reservatiesysteem, fileName):
    """
    Leest een bestand met de geven naam in

    Preconditie: Het bestand moet bestaan
    Postconditie: Het bestand is ingelezen adhv de content worden er wijzigingen in het reservatiesysteem gedaan

    :param reservatiesysteem: Het reservatiesysteem dat gebruikt word in functie van de inputfile
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
                # Kijk of de regel start met gebruiker zo ja dan maak je een gebruiker aan
                if (line.startswith("gebruiker")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    id = int(id)
                    voornaam = parts[2]
                    achternaam = parts[3]
                    email = parts[4]
                    # Maak de gebruiker aan
                    reservatiesysteem.addUser(voornaam, achternaam, email, id)

                # Kijk of de regel start met zaal zo ja dan maak je een zaal aan
                if (line.startswith("zaal")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    zaalNummer = parts[1]
                    aantalPlaatsen = parts[2]
                    # Maak de zaal aan TODO
                    zaal = Zaal(zaalNummer, aantalPlaatsen)
                    tableItem = reservatiesysteem.rooms.createItem(zaal.roomNumber, zaal)
                    reservatiesysteem.rooms.tableInsert(tableItem)

                # Kijk of de regel start met film zo ja dan maak je een film aan
                if (line.startswith("film")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    id = int(id)
                    titel = parts[2] + " " + parts[3]
                    rating = parts[4]
                    # Maak de film aan
                    reservatiesysteem.addMovie(titel, rating, id)

                # Kijk of de regel start met vertoning zo ja dan maak je een vertoning aan
                if (line.startswith("vertoning")):
                    # split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    id = int(id)
                    zaalNummer = parts[2]
                    slot = parts[3]
                    datum = parts[4]
                    filmId = parts[5]
                    vrijePlaatsen = parts[6]
                    # Maak de vertoning aan
                    reservatiesysteem.addScreening(zaalNummer, slot, datum, filmId, vrijePlaatsen, id)

                # Kijk of de regel start met start zo ja dan start je het systeem op TODO
                if (line.startswith("start")):
                    """# split de regel in onderdelen en verwijder de witruimte
                    parts = [part.strip() for part in line.split(" ")]
                    id = parts[1]
                    zaalNummer = parts[2]
                    slot = parts[3]
                    datum = parts[4]
                    filmId = parts[5]
                    vrijePlaatsen = parts[6]
                    # Maak de vertoning aan
                    vertoning = Vertoning(id, zaalNummer, slot, datum, filmId, vrijePlaatsen)
                    tableItem = reservatiesysteem.screenings.createItem(vertoning.id, vertoning)
                    reservatiesysteem.screenings.tableInsert(tableItem)"""

    def outputSystem(reservatiesysteem, fileName):
        """
        Output het reservatiesysteem met de opgegeven naam

        Preconditie: De bestandsnaam moet nog niet bestaan
        Postconditie: Het reservatiesysteem werd weggeschreven naar een html file

        :param reservatiesysteem: Het reservatiesyteem dat zal moeten worden weggeschreven
        :param fileName: De naam van het in te lezen bestand
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """