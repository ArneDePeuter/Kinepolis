import unittest
from Vertoning import *


class VertoningTests:
    def test_init(self):
        vertoning = Vertoning(56789, 87, 3, 5, 567, 20)
        assert vertoning.id == 56789
        assert vertoning.roomNumber == 87
        assert vertoning.slot == 3
        assert vertoning.date == 5
        assert vertoning.filmid == 567
        assert vertoning.reservedPlaces == 20
