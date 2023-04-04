import unittest
from Reservatie import Reservatie
from Kinepolis import Kinepolis


class ReservatieTest(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_init(self):
        t = Reservatie(1, 2, 3, 4, 5)
        self.assertEqual(1, t.id)
        self.assertEqual(2, t.userid)
        self.assertEqual(3, t.timestamp)
        self.assertEqual(4, t.screeningid)
        self.assertEqual(5, t.amountOfReservedSeats)

    def test_enqueue(self):
        t = Kinepolis()
        screeningId = 50
        t.addScreening(1, 1, 1, 1, 1, screeningId)
        t.enqueueReservation(1, 2, screeningId, 4)
        self.assertEqual(True, t.reservationSystem.datastruct.isEmpty())


if __name__ == "__main__":
    unittest.main()
