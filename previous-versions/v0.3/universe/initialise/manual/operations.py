from time import sleep
from rich import print
from PIL import Image
from re import search
from random import choices
from helpers.dir import folder
from keyboard import read_key
import universal.config as config
from rich import print

import pyautogui


def manual_input():

    # Used since a key press is being recorded twice (key down, key up)
    flag = 0

    # repeats until esc
    while True:

        # Stores keyboard input
        config.keyboardinput = read_key()

        # Filters duplicate key input
        if not flag:

            flag = 1

            # Checks user input and saves action
            for item in config.actions_list:
                if item["call"] == config.keyboardinput:

                    if item["function"] != "Pop()":

                        print(f"{config.id}   :point_right:  ", end="")
                        action = eval(item["function"])

                        if action:
                            config.record.append(action)
                            config.id += 1
                    else:
                        print(f"    :point_right:  ", end="")
                        eval(item["function"])

            # Stop recording
            if config.keyboardinput == "esc":
                break

        elif flag:
            flag = 0


def WaitForImage():

    # Declares dictionaries
    action = {}

    # Gets image to search location
    ftypes = [("png files", "*.png"), ("All files", "*")]
    location = folder(ftypes)

    # Saves action
    action["image"] = location

    # For user
    print(f"Search for [italic #8D9EFF]{action['image']}")

    return action


# For moving cursor
def MoveCursor():

    # Declares dictionaries
    action = {}
    current_position = {}

    # Saves position
    x, y = pyautogui.position()
    current_position["x"] = x
    current_position["y"] = y

    # Saves action
    action["move"] = current_position

    # For user
    print(f"Move to {current_position}")

    return action


def ClickCursor():

    # Declares dictionaries
    action = {}
    current_position = {}

    # Saves position
    x, y = pyautogui.position()
    current_position["x"] = x
    current_position["y"] = y

    # Saves action
    action["click"] = current_position

    # For user
    print(f"Click {current_position}")

    return action


def TextInput():

    # Declares dictionaries
    action = {}

    # Gets user text
    text = pyautogui.prompt("Enter text to write here", "Text input")

    # Saves action
    action["write"] = text

    # For user
    print(f"Write [italic #8D9EFF]{text} \t")

    return action


def KeyInput():

    # Declares dictionaries
    action = {}

    # Gets key to input
    pyautogui.alert("Enter the key to input", "Key Input")
    key = read_key()

    # Saves action
    action["key"] = key

    # For User
    print(f"hit [italic #F0A500]{key.upper()}\t")

    return action


def Wait():

    # Declares dictionaries
    action = {}

    # Checks for input
    try:
        seconds = int(pyautogui.prompt("Enter the time to wait", "Sleep"))
    except ValueError:
        print("[italic #FF6464]Value Error cancelling...")
        return

    # Saves action
    action["sleep"] = seconds

    # For user
    print(f"Wait for [italic #8D9EFF]{action['sleep']}s")

    return action


def Pop():

    # Delete last action
    try:
        delete = config.record.pop()
        config.id -= 1
        print(f":fire: {delete} removed :fire:")

    except IndexError:
        print(":Droplet: No actions to remove... :Droplet:")

    return


def DragCursor():

    # Declares dictionaries
    action = {}
    current_position = {}

    # Saves position
    x, y = pyautogui.position()
    current_position["x"] = x
    current_position["y"] = y

    # Saves action
    action["drag"] = current_position

    # For user
    print(f"Drag to {current_position}")

    return action


def InsertHotkey():

    # Declares dictionaries
    action = {}

    # Removes duplicate keys due to key up and down
    hots = 0

    # List of all keys in the hotkey
    hotkeys = []

    # Need to click okay to start recording
    hotkey = pyautogui.alert(
        "Enter keys one by one in the execution order\nfinally enter '9'",
        "Hot key input",
    )

    while True:

        # Every odd key doesn't get saved
        hotkey = read_key()

        # saves and displays recorded keys and exits when clicked 9 again
        if hotkey == "9":

            if hotkeys:
                # For User
                print(f"hit", end=" ")
                for key in hotkeys:
                    print(f"[italic #F0A500]{key.upper()}", end=" ")
                print()

            # Saves action
            action["hotkey"] = hotkeys
            return action

        # Filters odd keys
        elif not hots:

            # Saves even key
            hotkeys.append(hotkey)
            hots = 1

        elif hots:
            hots = 0


def DetectImage(path):
    while True:
        image_location = pyautogui.locateCenterOnScreen(path, confidence=0.9)
        if image_location:
            pyautogui.moveTo(image_location)
            return


def TakeScreenshot():
    # Declares dictionaries
    action = {}

    # Take screenshot and save it to images\screenshot.png
    action["screenshot"] = 1

    # For User
    print("Take a [italic #8D9EFF]screenshot")

    # Saving to config
    return action


def play_recorded():

    # Does what is recorded
    for action in config.record:
        for key, value in action.items():

            position = value

            # For moving
            if key == "move":
                pyautogui.moveTo(
                    position["x"], position["y"], 0.75, pyautogui.easeOutQuad
                )
                print(f"Moved to {position['x']}, {position['y']}")

            # For Clicking
            if key == "click":
                pyautogui.click(position["x"], position["y"])
                print(f"Clicked {position['x']}, {position['y']}")

            # For dragging with cursor
            if key == "drag":
                pyautogui.dragTo(position["x"], position["y"], 0.75)
                print(f"Dragged to {position['x']}, {position['y']}")

            # For text display
            if key == "write":
                pyautogui.write(action["write"], interval=0.15)
                print(f"Wrote [italic #8D9EFF]{action['write']}")

            # For screen search
            if key == "image":
                Image.open(action["image"]).convert("RGB").save(r"assets\images\images.png")
                DetectImage(r"assets\images\images.png")
                print(
                    f"Image [italic #8D9EFF]{action['image']}[/italic #8D9EFF] detected"
                )

            # For wait
            if key == "sleep":
                sleep(action["sleep"])
                print(f"Waited [italic #8D9EFF]{action['sleep']}s")

            # For hotkey input
            if key == "hotkey":
                for current_key in action["hotkey"]:
                    pyautogui.keyDown(current_key)
                for current_key in action["hotkey"]:
                    pyautogui.keyUp(current_key)

                print(f"Hot keys [italic #8D9EFF]pressed")

            # For key input
            if key == "key":
                pyautogui.press(action["key"])
                print(
                    f"[italic #8D9EFF]{action['key'].upper()}[/italic #8D9EFF] Key hit"
                )

            if key == "screenshot":
                pyautogui.screenshot(r"assets\images\screenshot.png")
                print("Took a [italic #8D9EFF]screenshot")


def eleos(argv):
    try:
        argv = argv[1].lower()
        thanks = search("^thanks", argv)
        thank = search("^thank*you", argv)
        ty = search("^ty", argv)
        if thanks or thank or ty:
            welcome = [
                "You're Welcome",
                "No Problem",
                "That made my day",
                "Gotchu Bro",
                "Sure thing!",
            ]
            welcome = choices(welcome)
            print(f"{welcome[0]} :sparkles:")
    except IndexError:
        pass