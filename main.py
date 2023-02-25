from Reservatiesysteem import Reservatiesysteem

def main():
    reservatieSysteem = Reservatiesysteem()
    for x in range(10):
        reservatieSysteem.addMovie(f"movie{x}", x)
    reservatieSysteem.movies.inorderTraverse(print)

if __name__ == "__main__":
    main()
