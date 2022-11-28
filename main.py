from sys import argv
from setup import install


def main():
    # program checks tries to install all modules required to run the program
    try:
        # imports the program
        from sample.core import initialise
        # starts the program
        initialise(argv)

    except ModuleNotFoundError:
        # If not installed already install all packages
        install()

        print("\nPlease re-run the program")


if __name__ == "__main__":
    main()
