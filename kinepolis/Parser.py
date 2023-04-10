from datetime import datetime

INPUTFOLDER = "./Input/"
OUTPUTFOLDER = "./Output/"


class Parser:
    def __init__(self, system) -> None:
        self.system = system

    def parseUserLine(self, line):
        parts = line.split()

        id = int(parts[1])
        voornaam = parts[2]
        achternaam = ""
        for i in range(2, len(parts) - 1):
            achternaam += parts[i]
            achternaam += " " if i != len(parts) - 1 else ""
        email = parts[-1]
        self.system.getUserSystem().addUser(voornaam, achternaam, email, id)

    def parseRoomLine(self, line):
        parts = line.split()
        zaalNummer = int(parts[1])
        aantalPlaatsen = int(parts[2])
        self.system.getRoomSystem().addRoom(zaalNummer, aantalPlaatsen)

    def parseMovieLine(self, line):
        parts = line.split()
        id = int(parts[1])
        titel = ""
        for i in range(2, len(parts) - 1):
            titel += parts[i]
            titel += " " if i != len(parts) - 1 else ""
        rating = float(parts[-1])
        self.system.getMovieSystem().addMovie(titel, rating, id)

    def parseScreeningLine(self, line):
        parts = line.split()
        id = parts[1]
        id = int(id)
        zaalNummer = int(parts[2])
        slot = int(parts[3])
        datum = parts[4]
        jaar, maand, dag = datum.split("-")
        jaar, maand, dag = int(jaar), int(maand), int(dag)
        datum = datetime(year=jaar, month=maand, day=dag)
        filmId = int(parts[5])
        vrijePlaatsen = int(parts[6])
        self.system.getScreeningSystem().addScreening(
            zaalNummer, slot, datum, filmId, vrijePlaatsen, id
        )

    def parseReservationLine(self, line):
        parts = line.split()
        datum = parts[0]
        jaar, maand, dag = datum.split("-")
        jaar, maand, dag = int(jaar), int(maand), int(dag)
        tijd = parts[1]
        uur, min = tijd.split(":")
        uur, min = int(uur), int(min)
        userId = int(parts[3])
        screeningId = int(parts[4])
        seats = int(parts[5])
        timestamp = datetime(jaar, maand, dag, uur, min, 0)
        self.system.getEventSystem().addReservationEvent(
            userId, timestamp, screeningId, seats
        )

    def parseKomBinnenLine(self, line):
        parts = line.split()
        datum = parts[0]
        jaar, maand, dag = datum.split("-")
        jaar, maand, dag = int(jaar), int(maand), int(dag)
        tijd = parts[1]
        uur, min = tijd.split(":")
        uur, min = int(uur), int(min)
        screeningId = int(parts[3])
        seats = int(parts[4])
        timestamp = datetime(jaar, maand, dag, uur, min, 0)
        self.system.getEventSystem().addTicketEvent(timestamp, screeningId, seats)

    def createLog(self, line):
        """
        Schrijft het systeem uit van een tijdstip in het verleden
        Preconditie: De datum en tijd vindt, plaatst in het verleden
        Postconditie: Het bestand is ingelezen a.d.h.v. de content worden er wijzigingen in het self.system gedaan
        :param fileName: De naam van het uit te schrijven bestand
        :param line: De lijn die werd gebruikt om deze methode aan te roepen
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        parts = line.split()
        datum = parts[0]
        jaar, maand, dag = datum.split("-")
        jaar, maand, dag = int(jaar), int(maand), int(dag)
        tijd = parts[1]
        uur, min = tijd.split(":")
        uur, min = int(uur), int(min)
        timestamp = datetime(jaar, maand, dag, uur, min, 0)
        minstr = str(min) if len(str(min)) == 2 else "0" + str(min)
        fileName = f"log_{jaar}-{maand}-{dag}_{uur}-{minstr}.html"

        self.system.getEventSystem().addLogEvent(timestamp, fileName)

    def readFile(self, fileName):
        """
        Leest een bestand met de geven naam in

        Pre-condition: Het bestand moet bestaan
        Post-condition: Het bestand is ingelezen adhv de content worden er wijzigingen in het self.system gedaan

        :param fileName: De naam van het in te lezen bestand
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # open het bestand
        self.events = False
        with open(INPUTFOLDER + fileName, "r") as file:
            # lees elke regel in het bestand
            for line in file.readlines():
                if line.startswith("#") or line.startswith("\n"):
                    continue

                if self.events:
                    # Kijk of de regel start met reservatie zo ja dan voeg je een reservatie toe aan het systeem
                    if line.split()[2] == "reserveer":
                        # split de regel in onderdelen en verwijder de witruimte
                        self.parseReservationLine(line)

                    # Kijk of de regel start met komBinnen TODO: Timestamp gebruiken of niet?
                    elif line.split()[2] == "ticket":
                        self.parseKomBinnenLine(line)

                    elif line.split()[2] == "log":
                        self.createLog(line)
                else:
                    # Kijk of de regel start met gebruiker zo ja dan maak je een gebruiker aan
                    if line.startswith("gebruiker"):
                        self.parseUserLine(line)

                    # Kijk of de regel start met zaal zo ja dan maak je een zaal aan
                    elif line.startswith("zaal"):
                        self.parseRoomLine(line)

                    # Kijk of de regel start met film zo ja dan maak je een film aan
                    elif line.startswith("film"):
                        # split de regel in onderdelen en verwijder de witruimte
                        self.parseMovieLine(line)

                    # Kijk of de regel start met vertoning zo ja dan maak je een vertoning aan
                    elif line.startswith("vertoning"):
                        # split de regel in onderdelen en verwijder de witruimte
                        self.parseScreeningLine(line)

                    # Kijk of de regel start met start zo ja dan start je het systeem op
                    elif line.startswith("start"):
                        self.events = True
