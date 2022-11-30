from rich import print
from keyboard import read_key, send
from initialise.file.file import file_input
from helpers.menu import newline_tab, print_menu, add_id, SaveJSON, SaveToDB, PrintRecorded
from initialise.manual.operations import play_recorded, manual_input
from conclusion.conclusion import looper, replacer
from initialise.manual.operations import eleos
from helpers.dir import clarity
from pyautogui import FailSafeException

import universal.config as config

def initialise(argv):
    try:
        startup(argv)
    except KeyboardInterrupt:
        newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED [KEYBOARD INTERRUPT]")
        pass


def startup(argv):
    
    eleos(argv)

    # Initialisation
    print("\n\tPress [italic #F0A500]CTRL[/italic #F0A500] for File input...")
    print("\t\tOr Press [italic #F0A500]SHIFT[/italic #F0A500] for  Manual input...\n")
    
    keyboardinput = ""

    while keyboardinput not in ["ctrl", "right ctrl", "right shift", "shift"]:
        keyboardinput = read_key()
        send("ctrl")
        send("right ctrl")

    if keyboardinput in ["ctrl", "right ctrl"]:
        status = file_input()
        if not status:
            newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED")
            return

    elif keyboardinput in ["right shift", "shift"]:
        print_menu()
        manual_input()
        
    if not len(config.record):
        newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED [NO ACTIONS INPUT]")
        return

    # Lists
    add_id()
    PrintRecorded()
    
    result = 1

    while True:
        
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

        # Saves recorded actions to a file
        SaveJSON()

    SaveToDB()
    try:
        play_recorded()
    except FailSafeException:
        newline_tab(1, "\n:Cross_Mark: [#DC3535] Operation Cancelled")
        return

    newline_tab(1, "\n:Party_Popper: [bold #8D72E1] SUCCESS")
    
def replace_menu():
    
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
    clarity()