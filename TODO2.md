### Vragen:
    MaterializedIndex klasse in orde voor gebruik? Of mogen we geen python dictionarys gebruiken

### To do:
    Error handleing GUI
    Uitgebreidere Log file?
    Tickets mag geen python list zijn
    NonUniqueTable kunnen implementeren:
        - dit betekend elke klasse krijgt een searchkey zodat we dynamisch kunnen aanpassen in een settings file ofzo wat de searchkey van elke klasse is
        - dit zorgt er dan voor dat we ipv .tableInsert(object.id, object) callen, callen we nu .tableInsert(object.searchKey, object) wat ervoor zorgt dat we makkelijk onze zoeksleutels ergens kunnen aanpassen
    NonUniqueTable volledig juist geimplementeerd
    Testen met je eigen datastructuren of je gewoon jou tables kan gebruiken binnen het systeem
    Bug testing (dit gaat makkelijk met de GUI nu)
    Documentatie bij elke klassen
    Nettere code 