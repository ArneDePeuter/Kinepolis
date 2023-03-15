from Event import Event
from datetime import datetime

class Parser:
    def __init__(self, system) -> None:
        self.system = system

    def parseUserLine(self, line):
        parts = line.split()

        id = int(parts[1])
        voornaam = parts[2]
        achternaam = parts[3]
        email = parts[4]
        self.system.addUser(voornaam, achternaam, email, id)
    
    def parseRoomLine(self, line):
        parts = line.split()
        zaalNummer = int(parts[1])
        aantalPlaatsen = int(parts[2])
        self.system.addRoom(zaalNummer, aantalPlaatsen)
    
    def parseMovieLine(self, line):
        parts = line.split()
        id = int(parts[1])
        titel = ""
        for i in range(2, len(parts)-1):
            titel += parts[i]
            titel += " " if i!=len(parts)-1 else "" 
        rating = int(float(parts[-1]))
        self.system.addMovie(titel, rating, id)
    
    def parseScreeningLine(self, line):
        parts = line.split()
        id = parts[1]
        id = int(id)
        zaalNummer = parts[2]
        slot = parts[3]
        datum = parts[4]
        filmId = int(parts[5])
        vrijePlaatsen = int(parts[6])
        self.system.addScreening(zaalNummer, slot, datum, filmId, vrijePlaatsen, id)

    def parseReservationLine(self, line):
        parts = line.split()
        datum = parts[0]
        jaar, maand, dag = datum.split("-")
        jaar, maand, dag = int(jaar), int(maand), int(dag)
        tijd = parts[1]
        uur, min = tijd.split(":")
        uur, min = int(uur), int(min)
        gebruikersId = int(parts[3])
        vertoningsId = int(parts[4])
        aantalTickets = int(parts[5])

        func = lambda gebruikersId=gebruikersId,uur=uur,vertoningsId=vertoningsId,aantalTickets=aantalTickets: self.system.reservationSystem.enqueueReservation(gebruikersId, uur, vertoningsId, aantalTickets)
        time = datetime(jaar, maand, dag, uur, min, 0)
        ev = Event(time, func)
        self.system.events.enqueue(self.system.events.createItem(time, ev))

    def parseKomBinnenLine(self, line):
        parts = line.split()
        datum = parts[0]
        jaar, maand, dag = datum.split("-")
        jaar, maand, dag = int(jaar), int(maand), int(dag)
        tijd = parts[1]
        uur, min = tijd.split(":")
        uur, min = int(uur), int(min)
        vertoningsId = int(parts[3])
        aantalMensen = int(parts[4])

        func = lambda vertoningsId=vertoningsId, aantalMensen=aantalMensen:self.system.komBinnen(vertoningsId, aantalMensen)
        time = datetime(jaar, maand, dag, uur, min, 0)
        ev = Event(time, func)
        self.system.events.enqueue(self.system.events.createItem(time, ev))

    def readFile(self, fileName):
        """
        Leest een bestand met de geven naam in

        Preconditie: Het bestand moet bestaan
        Postconditie: Het bestand is ingelezen adhv de content worden er wijzigingen in het self.system gedaan

        :param fileName: De naam van het in te lezen bestand
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # open het bestand
        eventRead = False
        with open(fileName, "r") as file:
            # lees elke regel in het bestand
            for line in file.readlines():
                if line.startswith("#") or line.startswith("\n"):
                    continue

                if eventRead:
                    # Kijk of de regel start met reservatie zo ja dan voeg je een reservatie toe aan het systeem
                    if line.split()[2] == "reserveer":
                        # split de regel in onderdelen en verwijder de witruimte
                        self.parseReservationLine(line)

                    # Kijk of de regel start met komBinnen TODO: Timestamp gebruiken of niet?
                    elif line.split()[2] == "ticket":
                        self.parseKomBinnenLine(line)
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
                        eventRead = True

    def outputSystem(self, fileName):
        """
        Output het self.system met de opgegeven naam

        Preconditie: De bestandsnaam moet nog niet bestaan
        Postconditie: Het self.system werd weggeschreven naar een html file

        :param self.system: Het self.system dat zal moeten worden weggeschreven
        :param fileName: De naam van het in te lezen bestand
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # to open/create a new html file in the write mode
        f = open(fileName, 'w')

        # Datum/ titels
        datums = []
        titels = []

        for i in range(self.system.screeningSystem.count):
            if self.system.screeningSystem.datastruct.tableRetrieve(i)[0] is not None:
                datums.append(str(self.system.screeningSystem.datastruct.tableRetrieve(i)[0].date))
                filmid = int(self.system.screeningSystem.datastruct.tableRetrieve(i)[0].filmid)
                titels.append(self.system.movieSystem.datastruct.tableRetrieve(filmid)[0].title)

        # the html code which will go in the file GFG.html
        html_template = """<html>
        <head>
            <style>
                table {
                    border-collapse: collapse;
                }
        
                table, td, th {
                    border: 1px solid black;
                }
            </style>
            <title>Log</title>
        </head>
        <body>
            <h1>Log op """+str(self.system.clock)+"""</h1>
            <table>
                <thead>
                    <td>Datum</td>
                    <td>Film</td>"""
        for i in range(self.system.timestamps.getLength()):
            html_template += f"<td>{self.system.timestamps.retrieve(i+1)[0]}</td>"
        html_template += """</thead>
                <tbody>"""
        for i in range(len(datums)):
            html_template += """<tr>"""
            html_template += """<td>"""+datums[i]+"""</td>"""
            html_template += """<td>"""+titels[i]+"""</td>"""
            html_template += """</tr>"""

        html_template += """</tbody>
            </table>
        </body>
    </html>
        """
        # writing the code into the file
        f.write(html_template)
        # close the file
        f.close()