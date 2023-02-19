from sys import argv


def main():


    # program checks tries to install all modules required to run the program
    try:
        # imports the program
        from sample.core import initialise
        from rich.align import Align
        from rich import print as rich_print

        print("This application uses emoji characters which may not be displayed " 
            "correctly in terminals without Unicode support. For optimal " 
            "experience, use a Unicode-supported terminal.")
        
        # starts the program
        initialise(argv)

        rich_print(Align("Made with :heart:  by Zafar\n", align="center"))

    except ModuleNotFoundError:

        print("\nPlease first run setup.py.")


if __name__ == "__main__":
    main()
