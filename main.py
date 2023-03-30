from kinepolis.Kinepolis import Kinepolis

def main():
    kinepolis = Kinepolis()
    kinepolis.load("system.txt")
    kinepolis.save("log.html")

if __name__ == "__main__":
    main()