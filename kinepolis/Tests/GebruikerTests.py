import unittest
from Gebruiker import *


class GebruikerTest(unittest.TestCase):
    def test_init(self):
        gebruiker = Gebruiker(555, "Siebe", "Mees", "siebe.mees@student.uantwerpen.be")
        self.assertEqual(555, gebruiker.id)
        self.assertEqual("Siebe", gebruiker.firstname)
        self.assertEqual("Mees", gebruiker.lastname)
        self.assertEqual("siebe.mees@student.uantwerpen.be", gebruiker.emailadres)


if __name__ == "__main__":
    unittest.main()
