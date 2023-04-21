# REQUIREMENTS

## Libs installed:
### GUI
- Flask
- jinja2
### Movie webscraper
- requests
- BeautifulSoup
### Mail system
- EmailMessage
- ssl
- smtplib

## How to use:
### GUI
- Run mainGUI.py
### Main
- Run main.py
### Change ADT
- Go to factories
- Change desired ADT object, behind every ADT there is a comment on what type ADT is expects
- If you just want to exchange the ADT's we provided, comment out the ADT that is used and uncomment the ADT you want to use
### IO stream
- Kinepolis.load expects a filename of a file that is inside the "Input" directory
- Kinepolis.save generates a log file with the givenfilename inside the "Output" directory
### Turn on/off mailsystem
- Go to Kinepolis.py, at this line "self.reservationSystem = ReservationSystem(self, False)"
the bool parameter represents if the mail system is turned on/off.
### Non unique searchkeys
- Change the searchkey in the Factories.py file, choose a valid Object.get operand
- IF YOU CHANGED IT TO A NON UNIQUE SEARCHKEY, YOU SHOULD PUT THE "NONUNIQUEWRAP" AROUND A TABLE OBJECT