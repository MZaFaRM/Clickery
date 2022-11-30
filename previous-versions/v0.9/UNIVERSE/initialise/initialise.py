from rich import print
from keyboard import read_key, send
from initialise.file.file import file_input
from initialise.manual.operations import play_recorded, manual_input
from conclusion.conclusion import looper, replacer
from initialise.manual.operations import eleos
import universal.config as config
from helpers.dir import clarity
from pyautogui import FailSafeException
from helpers.menu import (
    newline_tab,
    print_menu,
    add_id,
    SaveJSON,
    SaveToDB,
    PrintRecorded,
)


def initialise(argv):
    # Starts execution and handles keyboard interruption
    try:
        startup(argv)
    except KeyboardInterrupt:
        newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1][#082032 italic]keyboard interrupt")
        pass


def startup(argv):
    # The main part of the code
    eleos(argv)

    # Initialisation
    print("\n\tPress [italic #F0A500]CTRL[/italic #F0A500] for File input...")
    print("\t\tOr Press [italic #F0A500]SHIFT[/italic #F0A500] for  Manual input...\n")

    keyboardinput = ""

    # Stores keyboard input
    while keyboardinput not in ["ctrl", "right ctrl", "right shift", "shift"]:
        keyboardinput = read_key()
        send("ctrl")
        send("right ctrl")
    # For file input
    if keyboardinput in ["ctrl", "right ctrl"]:
        status = file_input()
        if not status:
            newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED")
            return
    # For manual input
    elif keyboardinput in ["right shift", "shift"]:
        print_menu()
        manual_input()
    # If actions record is empty the process quits
    if not len(config.record):
        PrintRecorded()
        newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1][#082032 italic]no actions input")
        return

    # Adds ids and prints everything that is recorded
    add_id()
    PrintRecorded()

    result = 1

    # For replace and repeat *finalise*
    while len(config.record):

        if result:
            replace_menu()
        else:
            result = 1

        AfterRecord = ""

        while AfterRecord not in [
            "ctrl",
            "right ctrl",
            "right shift",
            "shift",
            "space",
        ]:
            AfterRecord = read_key()

        if AfterRecord in ["ctrl", "right ctrl"]:
            result = looper()

        if AfterRecord in ["right shift", "shift"]:
            result = replacer()

        if AfterRecord in ["space"]:
            # Saves recorded actions to a file
            SaveJSON()
            break
        
        # If actions record is empty the process quits
        if not len(config.record):
            newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1][#082032 italic]no actions input")
            return
        
        # Saves recorded actions to a assets/json/history.json
        SaveJSON()

    # Saves recorded actions to assets/database/history.db in table HISTORY
    SaveToDB()
    try:
        # plays recorded
        play_recorded()
    # Execution of actions can be stopped by moving the cursor to the corner of the screen
    except FailSafeException:
        newline_tab(1, "\n:Cross_Mark: [#DC3535] Operation Cancelled")
        return

    # If all goes well...
    newline_tab(1, "\n:Party_Popper: [bold #8D72E1] SUCCESS")


def replace_menu():
    # The replace menu...

    print(
        "\n\tPress [italic #083AA9]CTRL[/italic #083AA9] to repeat a set of actions..."
    )
    print(
        "\t\tOr Press [italic #083AA9]SHIFT[/italic #083AA9] to replace any action..."
    )
    print(
        "\t\t\tOr Press [italic #083AA9]SPACE[/italic #083AA9] to start execution...\n"
    )


if __name__ == "initialise.initialise":
    # Excecuted to increase the quality of ktinkter windows
    clarity()