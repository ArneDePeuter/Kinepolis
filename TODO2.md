### To do:

## Meeting 10/04
- [ ] Documentatie in orde
- [ ] Datastructuren checken
- [ ] Engels
- [ ] Niet unieke zoeksleutel testen
 
Als je zin hebt:
- [ ] GUI stoerder maken
 


## Extra:
-[ ] Error handling GUI
-[ ] Uitgebreidere Log file?
-[ ] Tickets mag geen python list zijn

## Nodig:
- [ ] NonUniqueTable kunnen implementeren: -> Sam
    - dit betekent elke klasse krijgt een searchkey zodat we dynamisch kunnen aanpassen in een settings file ofzo wat de searchkey van elke klasse is
    - dit zorgt er dan voor dat we ipv tableInsert(object.id, object) callen, callen we nu .tableInsert(object.searchKey, object) wat ervoor zorgt dat we makkelijk onze zoeksleutels ergens kunnen aanpassen

- [X] EventSystem toevoegen top.update in elke event klasse, ipv if type(...) then.... -> Arne
- [X] Achternaam parsen User -> Siebe

## -> Allemaal
  TALEN ALLES BEST ENGELS IPV SOEP
  PARAMETERS ALLEMAAL ZELFDE NAAM OVERAL 
  Documentatie bij elke klassen
  Nettere code 
  Testen met je eigen datastructuren of je gewoon jou tables kan gebruiken binnen het systeem
  Bug testing (dit gaat makkelijk met de GUI nu)
  
## Notes
- EventSystem: (__init__(self, system) -> bool) init functie geeft zogezegt bool terug maar zou volgens ide None moeten
terug geven, geeft uiteindelijk ook geen bool terug.