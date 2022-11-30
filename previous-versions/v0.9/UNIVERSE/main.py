from sys import argv
from installation import install


def main():
    try:
        # Starting program
        from initialise.initialise import initialise

        initialise(argv)
    except ModuleNotFoundError:
        # If not installed already install all packages
        install()


if __name__ == "__main__":
    main()
