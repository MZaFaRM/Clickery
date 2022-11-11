import pyautogui
import keyboard
import json
import time
import config

# lists and dictionaries used
positions = []
current_position = {}
action = {}
keyboardinput = ""


def main():

    # Initialisation
    print("\nPress ctrl for file input...")
    print("Or Press shift for manual input...\n")

    while keyboardinput not in ["ctrl", "right shift", "shift"]:
        keyboardinput = keyboard.read_key()

    if keyboardinput == "ctrl":

        location = input("location of file: ")
        print()

        try:
            f = open(location)
            positions = json.load(f)
            print("File Initialized... \n")
        except FileNotFoundError:
            print("File Not Found... \n\n")

    elif keyboardinput in ["right shift", "shift"]:

        # Menu for manual input
        print("Initialized... \n\n")
        print(
            "Usage: \n\n Hover over the screen and press the apropriate key \n to perform the related operation \n\n"
        )
        print(
            "Supported Operations \n\n \t1. Move Cursor\n\t2. Click Position\n\t3. Enter Text"
        )
        print(
            "\t4. Search for Image _Under Work-Not currently usable_\n\t5. For Key Input\n\t6. Wait"
        )
        print(
            "\t7. Delete last action\n\t8. Drag cursor to\n\t9. Hotkey\n\nFinally, 'esc' to Start operation\n\n"
        )

        # Used since a key press is being recorded twice
        flag = 0

        # repeats until esc
        while True:

            # Stores keyboard input
            keyboardinput = keyboard.read_key()

            # Filters duplicate key input
            if flag == 0:

                flag = 1

                if keyboardinput == "1":
                    move_cursor()

                # For Clicking
                if keyboardinput == "2":
                    click_cursor()

                # For text input
                if keyboardinput == "3":
                    text_input()

                # For image search
                if keyboardinput == "4":
                    image_search()

                # For key input
                if keyboardinput == "5":
                    key_input()

                # For waiting
                if keyboardinput == "6":
                    wait()

                # For removing last action
                if keyboardinput == "7":
                    remove_last()

                # For Dragging cursor
                if keyboardinput == "8":
                    drag_cursor()

                # For hotkey
                if keyboardinput == "9":
                    insert_hotkey()

                # Stop recording
                if keyboardinput == "esc":
                    break

            else:
                flag = 0

    # Lists
    print(f"\nRecorded actions: {positions}")

    print("Press space to start...")
    keyboard.wait("space")
    play_recorded()

    print("\n__Success__")


def image_search():
    # Gets image to search location
    location = pyautogui.prompt("location of the image to search", "Screen search")

    # Saves action
    action["p"] = location
    positions.append(action)

    # For user
    print(f"Search for: {action['p']}")

    # Clears dictionaries for reuse
    action = {}


# For moving cursor
def move_cursor():

    # Saves position
    x, y = pyautogui.position()
    current_position["x"] = x
    current_position["y"] = y

    # Saves action
    action["m"] = current_position
    positions.append(action)

    # For user
    print(f"Move to: {current_position}")

    # Clears dictionary for reuse
    current_position = {}
    action = {}


def click_cursor():

    # Saves position
    x, y = pyautogui.position()
    current_position["x"] = x
    current_position["y"] = y

    # Saves action
    action["c"] = current_position
    positions.append(action)

    # For user
    print(f"Click: {current_position}")

    # Clears dictionaries for reuse
    current_position = {}
    action = {}


def text_input():
    # Gets user text
    text = pyautogui.prompt("Enter text to write here", "Text input")

    # Saves action
    action["w"] = text
    positions.append(action)

    # For user
    print(f"Write: {text}")

    # Clears dictionaries for reuse
    action = {}


def key_input():
    # Gets image to search location
    location = pyautogui.alert("Enter the key to input", "Key Input")
    key = keyboard.read_key()

    # Saves action
    action["k"] = key
    positions.append(action)

    # For User
    print(f"hit {key}")

    # Clears dictionaries for reuse
    action = {}


def wait():
    # Checks for input
    try:
        seconds = int(pyautogui.prompt("Enter the time to wait", "Sleep"))
    except ValueError:
        print("Value Error cancelling...")
        return

    # Saves action
    action["s"] = seconds
    positions.append(action)

    # For user
    print(f"Wait for {action['s']}s")

    # Clears dictionaries for reuse
    action = {}


def remove_last():
    # Delete last action
    try:
        delete = positions.pop()
        print(f"{delete} Removed")

    except IndexError:
        print("No actions to remove")


def drag_cursor():
    # Saves position
    x, y = pyautogui.position()
    current_position["x"] = x
    current_position["y"] = y

    # Saves action
    action["d"] = current_position
    positions.append(action)

    # For user
    print(f"Drag to: {current_position}")

    # Clears dictionary for reuse
    current_position = {}
    action = {}


def insert_hotkey():
    keys = []
    key = "null"

    while key != "9":
        key = keyboard.read_key()
        keys.append(key)

    # Saves action
    action["h"] = keys
    positions.append(action)

    # For User
    print(f"hit {keys}")

    # Clears dictionaries for reuse
    action = {}
    keys = []
    
def play_recorded():
    
    # Does what is recorded
    for action in positions:
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
                while True:
                    screen = pyautogui.locateOnScreen(action["p"])
                    print(screen)

                    if screen != "None":
                        break

            # For wait
            if key == "s":
                time.sleep(action["s"])

            # For hotkey input
            if key == "h":
                keyboard.play(action["h"])

            # For key input
            if key == "k":
                pyautogui.press(action["k"])

            if key == "d":
                pyautogui.dragTo(position["x"], position["y"], 1.5)

if __name__ == "__main__":
    main()
