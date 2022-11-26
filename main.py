from sys import argv
from setup import install
from subprocess import check_call
from sys import executable


def main():
    
    try:
        # Starting program
        from sample.core import initialise

        initialise(argv)

    except ModuleNotFoundError:
        # If not installed already install all packages
        install()
        
        print("\nPlease re-run the program")


if __name__ == "__main__":
    main()
