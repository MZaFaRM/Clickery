from sys import argv


def main():
    # program checks tries to install all modules required to run the program
    try:
        # imports the program
        from sample.core import initialise
        # starts the program
        initialise(argv)

    except ModuleNotFoundError:

        print("\nPlease first run setup.py .")


if __name__ == "__main__":
    main()
