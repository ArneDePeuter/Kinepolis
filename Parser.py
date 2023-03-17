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

        func = lambda gebruikersId=gebruikersId,vertoningsId=vertoningsId,aantalTickets=aantalTickets: self.system.reservationSystem.reservate(gebruikersId, vertoningsId, aantalTickets)
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
        minstr = str(min) if len(str(min)) == 2 else "0"+str(min)
        fileName = f"Tests/Output/log_{jaar}-{maand}-{dag}_{uur}-{minstr}.html" 

        func = lambda fileName=fileName, timestamp=timestamp:self.outputSystem(fileName, timestamp)
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
        self.events = False
        with open(fileName, "r") as file:
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

    def outputSystem(self, fileName, timestamp):
        """
        Output het self.system met de opgegeven naam

        Preconditie: De bestandsnaam moet nog niet bestaan
        Postconditie: Het self.system werd weggeschreven naar een html file

        :param self.system: Het self.system dat zal moeten worden weggeschreven
        :param fileName: De naam van het in te lezen bestand
        :param timestamp: De tijd waarop het systeem een log aanmaakt
        :return: True als de operatie is gelukt, False als het niet gelukt is.
        """
        # to open/create a new html file in the write mode
        f = open(fileName, 'w')

        # the html code which will go in the file log_..._.html
        # Head tag, styling,...
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
            <title>Kinepolis - Log</title>
        </head>
        """
        # Table head: Datum, film en tijdsloten
        html_template += """<body>
            <h1>Log op """+str(timestamp)+"""</h1>
            <table>
                <thead>
                    <td>Datum</td>
                    <td>Film</td>"""
        for i in range(self.system.timestamps.getLength()):
            html_template += f"<td>{self.system.timestamps.retrieve(i+1)[0]}</td>"
        html_template += """</thead>"""

        # Table body/content
        html_template += """<tbody>"""
        # table rows
        for movie in range(self.system.movieSystem.count):
            if self.system.movieSystem.datastruct.tableRetrieve(movie)[0] is not None:
                filmid = int(self.system.movieSystem.datastruct.tableRetrieve(movie)[0].id)
                movieAdded = False
                movieRowNotComplete = False
                # Kijk in screeningsystem voor de film kijkt of we een vertoning hebben voor de film op bepaalde datum die we willen
                for screening in range(self.system.screeningSystem.count):
                    if self.system.screeningSystem.datastruct.tableRetrieve(screening)[0] is not None and int(self.system.screeningSystem.datastruct.tableRetrieve(screening)[0].filmid) == filmid:
                        # Film op die datumm is nog niet toegevoegd
                        if not movieAdded:
                            html_template += """<tr>"""
                            # Datum
                            html_template += """<td>"""+str(self.system.screeningSystem.datastruct.tableRetrieve(screening)[0].date)+"""</td>"""
                            # Film
                            html_template += """<td>""" +self.system.movieSystem.datastruct.tableRetrieve(movie)[0].title+"""</td>"""
                            movieAdded = True
                        # TODO: Bepaal voor elke film welke voor de sloten van toepassing is G, F of W en maak onderscheid tussen films met een andere datum
                        elif movieAdded and not movieRowNotComplete:
                            for i in range(self.system.screeningSystem.count):
                                if self.system.screeningSystem.datastruct.tableRetrieve(i)[0] is not None and int(self.system.screeningSystem.datastruct.tableRetrieve(i)[0].filmid) == filmid:
                                    html_template += """<td>"""+str(self.system.screeningSystem.datastruct.tableRetrieve(i)[0].freePlaces)+"""</td>"""
                            html_template += """</tr>"""
                            movieRowNotComplete = True


        #for i in range(self.system.screeningSystem.count):
        #    if self.system.screeningSystem.datastruct.tableRetrieve(i)[0] is not None:
        #        html_template += """<tr>"""
                #Datum
        #        html_template += """<td>"""+str(self.system.screeningSystem.datastruct.tableRetrieve(i)[0].date)+"""</td>"""
                #Film
        #        filmid = int(self.system.screeningSystem.datastruct.tableRetrieve(i)[0].filmid)
        #        html_template += """<td>""" +self.system.movieSystem.datastruct.tableRetrieve(filmid)[0].title+ """</td>"""
        #        html_template += """</tr>"""
                # Bepaal voor elke film welke voor de sloten van toepassing is G, F of W
        #        oldClock = self.system.clock
        #        self.system.clock = timestamp



        html_template += """</tbody>
            </table>
        </body>
        </html>
        """
        # writing the code into the file
        f.write(html_template)
        # close the file
        f.close()