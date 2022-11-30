import pyautogui, keyboard, config

from json import load as listify
from time import sleep
from tabulate import tabulate
from rich import print


def main():

    # Initialisation
    print("\n\tPress [italic #F0A500]CTRL[/italic #F0A500] for File input...")
    print("\t\tOr Press [italic #F0A500]SHIFT[/italic #F0A500] for  Manual input...\n")

    while config.keyboardinput not in ["ctrl", "right shift", "shift"]:
        config.keyboardinput = keyboard.read_key()

    if config.keyboardinput == "ctrl":

        location = input("location of file: ")
        print()

        try:
            f = open(location)
            config.positions = listify(f)
            newline_tab(1, "[italic #1A4D2E]File Initialized...:dizzy::dizzy::dizzy:")
        except FileNotFoundError:
            print(1, "[italic #FF5F00]File Not Found...:Heavy_exclamation_mark::Heavy_exclamation_mark::Heavy_exclamation_mark:")
            return

    elif config.keyboardinput in ["right shift", "shift"]:

        # Print menu
        print_menu()

        # Used since a key press is being recorded twice (key down, key up)
        flag = 0

        # repeats until esc
        while True:

            # Stores keyboard input
            config.keyboardinput = keyboard.read_key()

            # Filters duplicate key input
            if flag == 0:

                flag = 1

                # Checks user input and saves action
                for item in config.actions_list:
                    if item["call"] == config.keyboardinput:
                        print(":point_right:  ", end="")
                        eval(item["function"])

                # Stop recording
                if config.keyboardinput == "esc":
                    break

            else:
                flag = 0

    # Lists
    print(f'\nRecorded actions: {config.positions}\n')

    newline_tab(1,"Press [italic #F0A500]SPACE[/italic #F0A500] to start...")
    keyboard.wait("space")
    play_recorded()

    newline_tab(1,":Party_Popper: [bold #8D72E1] SUCCESS")


def image_search():
    # Gets image to search location
    location = pyautogui.prompt("location of the image to search", "Screen search")

    # Saves action
    config.action["p"] = location
    config.positions.append(config.action)

    # For user
    print(f"Search for [italic #8D9EFF]{config.action['p']}")

    # Clears dictionaries for reuse
    config.action = {}


# For moving cursor
def move_cursor():

    # Saves position
    x, y = pyautogui.position()
    config.current_position["x"] = x
    config.current_position["y"] = y

    # Saves action
    config.action["m"] = config.current_position
    config.positions.append(config.action)

    # For user
    print(f"Move to {config.current_position}")

    # Clears dictionary for reuse
    config.current_position = {}
    config.action = {}


def click_cursor():

    # Saves position
    x, y = pyautogui.position()
    config.current_position["x"] = x
    config.current_position["y"] = y

    # Saves action
    config.action["c"] = config.current_position
    config.positions.append(config.action)

    # For user
    print(f"Click {config.current_position}")

    # Clears dictionaries for reuse
    config.current_position = {}
    config.action = {}


def text_input():
    # Gets user text
    text = pyautogui.prompt("Enter text to write here", "Text input")

    # Saves action
    config.action["w"] = text
    config.positions.append(config.action)

    # For user
    print(f"Write [italic #8D9EFF]{text} \t")

    # Clears dictionaries for reuse
    config.action = {}


def key_input():
    # Gets image to search location
    location = pyautogui.alert("Enter the key to input", "Key Input")
    key = keyboard.read_key()

    # Saves action
    config.action["k"] = key
    config.positions.append(config.action)

    # For User
    print(f"hit [italic #F0A500]{key.upper()}\t")

    # Clears dictionaries for reuse
    config.action = {}


def wait():
    # Checks for input
    try:
        seconds = int(pyautogui.prompt("Enter the time to wait", "Sleep"))
    except ValueError:
        print("[italic #FF6464]Value Error cancelling...")
        return

    # Saves action
    config.action["s"] = seconds
    config.positions.append(config.action)

    # For user
    print(f"Wait for [italic #8D9EFF]{config.action['s']}s")

    # Clears dictionaries for reuse
    config.action = {}


def remove_last():
    # Delete last action
    try:
        delete = config.positions.pop()
        print(f":fire: {delete} removed :fire:")

    except IndexError:
        print(":Droplet: No actions to remove... :Droplet:")


def drag_cursor():
    # Saves position
    x, y = pyautogui.position()
    config.current_position["x"] = x
    config.current_position["y"] = y

    # Saves action
    config.action["d"] = config.current_position
    config.positions.append(config.action)

    # For user
    print(f"Drag to {config.current_position}")

    # Clears dictionary for reuse
    config.current_position = {}
    config.action = {}


def insert_hotkey():
    keys = []
    key = "null"

    while key != "9":
        key = keyboard.read_key()
        keys.append(key)

    # Saves action
    config.action["h"] = keys
    config.positions.append(config.action)

    # For User
    print(f"hit {keys}")

    # Clears dictionaries for reuse
    config.action = {}
    keys = []


def play_recorded():

    # Does what is recorded
    for action in config.positions:
        for key, value in action.items():

            position = value

            # For moving
            if key == "m":
                pyautogui.moveTo(
                    position["x"], position["y"], 0.75, pyautogui.easeOutQuad
                )

            # For Clicking
            if key == "c":
                pyautogui.click(position["x"], position["y"])

            # For text display
            if key == "w":
                pyautogui.write(action["w"], interval=0.15)

            # For screen search
            if key == "p":
                    pass

            # For wait
            if key == "s":
                sleep(action["s"])

            # For hotkey input
            if key == "h":
                keyboard.play(action["h"])

            # For key input
            if key == "k":
                pyautogui.press(action["k"])

            if key == "d":
                pyautogui.dragTo(position["x"], position["y"], 1.5)


def print_menu():
    # Menu for manual input
    menu_items = []
    single_item = {}
    for item in config.actions_list:
        single_item["ID"] = item["id"]
        single_item["DESCRIPTION"] = item["description"]
        single_item["CALL"] = '"' + item["call"] + '"'
        menu_items.append(single_item)
        single_item = {}
        
    newline_tab(1, sentence="Initialized...:dizzy::dizzy::dizzy:")
    newline_tab(1, sentence="Usage:")
    newline_tab(1, sentence="[#ECDBBA]\tHover over the screen and press the apropriate call \n\t\tto perform the related operation")
    newline_tab(1, sentence="Supported Operations:")
    print(tabulate(menu_items, "keys", "rounded_grid"), end="\n\n")
    newline_tab(1, sentence="Finally, [italic #F0A500]ESC[/italic #F0A500] to Start operation")

def newline_tab(n, sentence=""):
    print(sentence)
    for i in range(n):
        print()


if __name__ == "__main__":
    main()