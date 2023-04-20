from kinepolis.Kinepolis import Kinepolis


def testSearchkey():
    kine = Kinepolis()
    kine.getUserSystem().addUser("Sam", "De Smet", "samdesmet@tkt.be", 5)
    kine.getUserSystem().addUser("Mark", "Beton", "mark@tkt.be",10)
    kine.getUserSystem().addUser("Sam", "Beton", "sambeton@tkt.be", 6)
    print(kine.getUserSystem().retrieve("Sam")[0].getLastName())

def main():
    kinepolis = Kinepolis()
    kinepolis.load("system.txt")
    kinepolis.runSim()

if __name__ == "__main__":
    main()
