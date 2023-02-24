from Reservatiesysteem import Reservatiesysteem


def main():
    reservatieSysteem = Reservatiesysteem()
    reservatieSysteem.addMovie("Goth", 5)
    reservatieSysteem.addRoom(0, 100)

if __name__ == "__main__":
    main()