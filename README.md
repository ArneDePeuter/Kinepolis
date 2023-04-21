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
- Go to Factories.py, comment out desired ADT
### Turn on/off mailsystem
- Go to Kinepolis.py, at this line "self.reservationSystem = ReservationSystem(self, False)"
the bool parameter represents if the mail system is turned on/off.
