from email.message import EmailMessage
import ssl
import smtplib

class MailSystem:
    def __init__(self, sys) -> None:
        self.sys = sys
        self.email_sender = "kinepolisuantwerpen@gmail.com"
        self.email_password = "eopjjzzvmrtklauw"
        subject = "Kinepolis reservation"

        self.em = EmailMessage()
        self.em["From"] = self.email_sender
        self.em["Subject"] = subject
        self.context = ssl.create_default_context()

    def createBody(self, reservatie):
        # vertoning = self.sys.vertoningen.tableRetrieve(reservatie.vertoningid)
        # film = self.sys.films.tableRetrieve(vertoning.filmid)

        # return f"""
        # Geachte,

        # U reservatie voor de film: {film} (om {vertoning.slot})is geplaatst.
        # U hebt {reservatie.amountOfReservedSeats} plaatsen gereserveerd.

        # Dit is u reservatieId : {reservatie.id}.

        # Mvg,
        # Team Kinepolis
        # """
        return f"""
        Geachte,

        U reservatie voor de film: {"The matrix"} (om {"15:00"}) is geplaatst.
        U hebt {"10"} plaatsen gereserveerd.

        Dit is u reservatieId : {"558"}.

        Mvg,
        Team Kinepolis
        """

    def sendMailTo(self, emailadress, reservation):
        self.em["To"] = emailadress
        self.em.set_content(self.createBody(reservation))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, emailadress, self.em.as_string())

mailsys = MailSystem("s")
mailsys.sendMailTo("arne@depeuter.org", "")