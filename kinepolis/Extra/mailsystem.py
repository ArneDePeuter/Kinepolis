from email.message import EmailMessage
import ssl
import smtplib
from time import sleep

class MailSystem:
    def __init__(self) -> None:
        self.email_sender = "kinepolisuantwerpen@gmail.com"
        self.email_password = "eopjjzzvmrtklauw"
        self.subject = "Kinepolis reservation"
        self.context = ssl.create_default_context()

    def createBody(self, moviename, time, places, reservationId):
        return f"""
        Geachte,

        U reservatie voor de film: {moviename} ( om {time} ) is geplaatst.
        U hebt {places} plaatsen gereserveerd.

        Dit is uw reservatienummer: {reservationId}

        Mvg,
        Team Kinepolis
        """

    def sendMailTo(self, emailadress, moviename, time, places, reservationId):
        em = EmailMessage()
        em["From"] = self.email_sender
        em["Subject"] = self.subject
        em["To"] = emailadress
        em.set_content(self.createBody(moviename, time, places, reservationId))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            returncode = smtp.sendmail(self.email_sender, emailadress, em.as_string())
            if type(returncode) != dict:
                print(returncode)