from sys import executable
from subprocess import check_call


def install():
    # Takes the list of modules to be installed from requirements.txt and installs them
    check_call([executable, "-m", "pip", "install", "-r", "requirements.txt"])


if __name__ == "__main__":
    install()

# recommended to run this file if it is the first time running the program
# although main do 'try' to take care of this if you haven't already run setup.py