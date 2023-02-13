from sys import argv
from rich import print
from rich.align import Align


def main():

    print(
        Align(
            "This application uses emoji characters which may not be displayed correctly in terminals without Unicode support. For optimal experience, use a Unicode-supported terminal."
        , align="center")
    )
    # program checks tries to install all modules required to run the program
    try:
        # imports the program
        from sample.core import initialise

        # starts the program
        initialise(argv)

        print(Align("Made with :heart:  by Zafar\n", align="center"))

    except ModuleNotFoundError:

        print("\nPlease first run setup.py .")


if __name__ == "__main__":
    main()
