class Parser:
    def __init__(self, system) -> None:
        self.system = system
    
    def readFile(self, fileName):
        """
        Leest een bestand met de geven naam in

        Preconditie: Het bestand moet bestaan
        Postconditie: Het bestand is ingelezen adhv de content worden er wijzigingen in het self.system gedaan

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
                    if line.startswith("gebruiker"):
                        # split de regel in onderdelen en verwijder de witruimte
                        parts = [part.strip() for part in line.split(" ")]
                        id = parts[1]
                        id = int(id)
                        voornaam = parts[2]
                        achternaam = parts[3]
                        email = parts[4]
                        # Maak de gebruiker aan
                        self.system.addUser(voornaam, achternaam, email, id)

                    # Kijk of de regel start met zaal zo ja dan maak je een zaal aan
                    if line.startswith("zaal"):
                        # split de regel in onderdelen en verwijder de witruimte
                        parts = [part.strip() for part in line.split(" ")]
                        zaalNummer = parts[1]
                        aantalPlaatsen = parts[2]
                        self.system.addRoom(zaalNummer, aantalPlaatsen)

                    # Kijk of de regel start met film zo ja dan maak je een film aan
                    if line.startswith("film"):
                        # split de regel in onderdelen en verwijder de witruimte
                        parts = [part.strip() for part in line.split(" ")]
                        id = parts[1]
                        id = int(id)
                        titel = parts[2] + " " + parts[3]
                        rating = parts[-1]
                        # Maak de film aan
                        self.system.addMovie(titel, rating, id)

                    # Kijk of de regel start met vertoning zo ja dan maak je een vertoning aan
                    if line.startswith("vertoning"):
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
                        self.system.addScreening(zaalNummer, slot, datum, filmId, vrijePlaatsen, id)

                    # Kijk of de regel start met start zo ja dan start je het systeem op TODO
                    if line.startswith("start"):
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
                        tableItem = self.system.screenings.createItem(vertoning.id, vertoning)
                        self.system.screenings.tableInsert(tableItem)"""

                    # Kijk of de regel start met reservatie zo ja dan voeg je een reservatie toe aan het systeem
                    if line.startswith("reservatie"):
                        # split de regel in onderdelen en verwijder de witruimte
                        parts = [part.strip() for part in line.split(" ")]
                        datum = parts[1]
                        tijd = parts[2]
                        gebruikersId = parts[3]
                        vertoningsId = parts[4]
                        aantalTickets = parts[5]
                        # Maak de reservatie aan
                        #  def enqueueReservation(self, userid, timestamp, vertoningid, aantalPlaatsenGereserveerd) TODO: Fix timestamp
                        self.system.reservationSystem.enqueueReservation(gebruikersId, tijd, vertoningsId, aantalTickets)

                    # Kijk of de regel start met komBinnen TODO: Timestamp gebruiken of niet?
                    if line.startswith("komBinnen"):
                        # split de regel in onderdelen en verwijder de witruimte
                        parts = [part.strip() for part in line.split(" ")]
                        datum = parts[1]
                        tijd = parts[2]
                        vertoningsId = parts[3]
                        aantalMensen = parts[5]
                        # komBinnen
                        self.system.komBinnen(vertoningsId, aantalMensen)


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