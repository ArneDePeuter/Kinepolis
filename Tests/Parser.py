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

    :param reservatiesysteem: Het reservatiesysteem dat zal moeten worden weggeschreven
    :param fileName: De naam van het in te lezen bestand
    :return: True als de operatie is gelukt, False als het niet gelukt is.
    """
    # to open/create a new html file in the write mode
    f = open(fileName, 'w')

    datums = []
    titels = []
    for i in range(reservatiesysteem.screeningCount):
        if reservatiesysteem.screenings.tableRetrieve(i)[0] is not None:
            datums.append(str(reservatiesysteem.screenings.tableRetrieve(i)[0].date))
            filmid = int(reservatiesysteem.screenings.tableRetrieve(i)[0].filmid)
            titels.append(reservatiesysteem.movies.tableRetrieve(filmid)[0].title)


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
        <h1>Log op """+str(reservatiesysteem.clock)+"""</h1>
        <table>
            <thead>
                <td>Datum</td>
                <td>Film</td>
                <td>14:30</td>
                <td>17:00</td>
                <td>20:00</td>
                <td>22:30</td>
            </thead>
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