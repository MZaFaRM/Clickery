from rich import print
from re import search
from random import choices
from sample.helpers.dir import folder
import sample.universal.config as config
from tkinter.filedialog import asksaveasfile
import os
import pyautogui
from sample.pre_record.operations.key_insert import return_key_input
from sample.pre_record.operations.hot_key_insert import return_hot_key_input
from sample.pre_record.operations.wait_seconds import return_wait
from sample.pre_record.operations.text_input import return_write
from rich.align import Align


def WaitForImage():

    # Declares dictionaries
    action = {}

    # Gets image to search location
    ftypes = [("png files", "*.png"), ("All files", "*")]
    location = folder(ftypes)

    if location:

        # Saves action
        action["image"] = location

        # For user
        print(Align(
            f" :Rose:  [#29C7AC BOLD]SEARCH FOR[/#29C7AC BOLD] [italic #8D9EFF]{action['image']}", align="center"
        ))

        return action

    return 0


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
    print(Align(f" :Rose:  [#29C7AC BOLD]MOVE TO[/#29C7AC BOLD] {current_position}", align="center"))

    return action


def LeftClickCursor():

    # Declares dictionaries
    action = {}

    # Saves action
    action["l-click"] = 1

    # For user
    print(Align(f" :Rose:  [#29C7AC BOLD]LEFT CLICK AT[/] [italic #8D9EFF]position", align="center"))

    return action


def RightClickCursor():

    # Declares dictionaries
    action = {}

    # Saves action
    action["r-click"] = 1

    # For user
    print(Align(f" :Rose:  [#29C7AC BOLD]RIGHT CLICK AT[/] [italic #8D9EFF]position", align="center"))

    return action


def TextInput():

    # Gets text
    text = return_write()
    action = {}

    if text:
        action["write"] = text
        # For user
        print(Align(
            f" :Rose:  [#29C7AC BOLD]WRITE[/#29C7AC BOLD] [italic #8D9EFF]{action['write']}", align="center"
        ))
        return action

    return 0


def KeyInput():

    # Declares dictionaries
    action = {}

    # Gets key to input
    key = return_key_input()

    if key:

        print(Align(f" :Rose:  [#29C7AC BOLD]HIT KEY[/#29C7AC BOLD][italic #F0A500] {key}", align="center"))
                  
        # Saves action
        action["key"] = key.replace(" ", "")

        return action

    return 0


def Wait():

    action = {}
    # gets input
    time = return_wait()
    if time != "-":
        action["sleep"] = time

        # For user
        print(Align(
            f" :Rose:  [#29C7AC BOLD]WAIT FOR[/#29C7AC BOLD] [italic #8D9EFF]{action['sleep']}s", align="center"
        ))

        return action
    else:
        return 0


def Pop(id=0):

    if not id:
        # Delete last action
        try:
            delete = config.record.pop()

        except IndexError:
            print(Align(":Cross_Mark:  [#D2001A italic]No actions to remove", align="center"))
            return
    else:
        delete = config.record.pop(id - 1)

    print(Align(f":Wilted_Flower: [#7D9D9C italic] {delete} removed", align="center"))


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
    print(Align(f" :Rose:  [#29C7AC BOLD]DRAG TO[/#29C7AC BOLD] {current_position}", align="center"))

    return action


def InsertHotkey():

    # Declares dictionaries
    action = {}

    # gets input hotkeys
    hotkeys, hotkeys_display = return_hot_key_input()

    if hotkeys and hotkeys_display:

        # Saves action
        action["hotkey"] = hotkeys

        # For User
        print(Align(
            f" :Rose:  [#29C7AC BOLD]INSERT HOTKEYS[/#29C7AC BOLD][italic #F0A500] {hotkeys_display}", align="center"
        ))

        return action

    return 0


def TakeScreenshot():
    # Declares dictionaries
    action = {}

    files = [("image files", "*.png")]
    file = asksaveasfile(filetypes=files, defaultextension=files)

    # Checks if the user provided a location
    if file:

        # 'file' is an io.TextWrapper
        # Take screenshot and save it to the given location
        location = file.name
        file.close()
        os.remove(location)
        action["screenshot"] = location

        # For User
        print(Align(f" :Rose:  [#29C7AC BOLD]SAVE A SCREENSHOT AT[/#29C7AC BOLD] [italic #8D9EFF]{location}", align="center"))

        # Saving to config
        return action

    else:
        return 0


def egg(argv):
    try:
        argv = argv[1].lower()
        thanks = search("^thanks", argv)
        thank = search("^thank*you", argv)
        ty = search("^ty", argv)
        if thanks or thank or ty:
            response = [
                "You're Welcome",
                "No Problem",
                "That made my day",
                "No worries",
                "Sure thing!",
            ]
            
        response = choices(response)
        
        print(f"{response[0]} ✨")
    except IndexError:
        pass
    except Exception:
        pass
