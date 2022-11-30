from time import sleep
from rich import print
from PIL import Image
from re import search
from random import choices
from helpers.dir import folder
from keyboard import read_key, send
import universal.config as config
from rich import print
import pyautogui
from initialise.manual.key_insert import return_key_input
from initialise.manual.hot_key import return_hot_key_input, display_hotkeys
from initialise.manual.wait_seconds import return_wait
from initialise.manual.text_input import return_write


def manual_input():

    # Used since a key press is being recorded twice (key down, key up)
    flag = 0

    # repeats until esc
    while True:

        # Stores keyboard input
        keyboardinput = read_key()

        # Filters duplicate key input
        if not flag:

            flag = 1

            # Checks user input and saves action
            for item in config.actions_list:
                if item["call"] == keyboardinput:

                    if item["function"] != "Pop()":

                        action = eval(item["function"])

                        if action:
                            config.record.append(action)
                            config.id += 1
                    else:
                        eval(item["function"])

            # Stop recording
            if keyboardinput == "esc":
                break

        elif flag:
            flag = 0


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
        print(f" :Rose:  [#29C7AC BOLD]SEARCH FOR[/#29C7AC BOLD] [italic #8D9EFF]{action['image']}")

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
    print(f" :Rose:  [#29C7AC BOLD]MOVE TO[/#29C7AC BOLD] {current_position}")

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
    print(f" :Rose:  [#29C7AC BOLD]CLICK AT[/#29C7AC BOLD] {current_position}")

    return action


def TextInput():

    # Gets text
    text = return_write()
    action = {}
    
    if text:
        action['write'] = text
        # For user
        print(f" :Rose:  [#29C7AC BOLD]WRITE[/#29C7AC BOLD] [italic #8D9EFF]{action['write']} \t")
        return action
    
    return 0


def KeyInput():

    # Declares dictionaries
    action = {}

    # Gets key to input
    key = return_key_input()
    
    if key:

        # Saves action
        action["key"] = key

        if len(key) == 2:
            # For User
            print(f" :Rose:  [#29C7AC BOLD]HIT KEY[/#29C7AC BOLD][italic #F0A500] {key}\t")
        else:
            # For User
            print(f" :Rose:  [#29C7AC BOLD]HIT KEY[/#29C7AC BOLD][italic #F0A500] {key.upper()}\t")
            
        return action
    
    return 0


def Wait():
    
    action = {}
    # gets input
    time = return_wait()
    if time != '-':
        action['sleep'] = time
        
        # For user
        print(f" :Rose:  [#29C7AC BOLD]WAIT FOR[/#29C7AC BOLD] [italic #8D9EFF]{action['sleep']}s")
    
        return action
    else:
        return 0


def Pop():

    # Delete last action
    try:
        delete = config.record.pop()
        config.id -= 1
        print(f":Wilted_Flower: [#082032 italic] {delete} removed")

    except IndexError:
        print(":Cross_Mark:  [#064663 italic]No actions to remove")

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
    print(f" :Rose:  [#29C7AC BOLD]DRAG TO[/#29C7AC BOLD] {current_position}")

    return action


def InsertHotkey():

    # Declares dictionaries
    action = {}

    # gets input hotkeys
    hotkeys = return_hot_key_input()
    
    if hotkeys:
        
        # Saves action
        action["hotkey"] = hotkeys

        hotkeys_display = display_hotkeys()

        # For User
        print(f" :Rose:  [#29C7AC BOLD]INSERT HOTKEYS[/#29C7AC BOLD][italic #F0A500] {hotkeys_display}")
        
        return action
    
    return 0


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
    print(" :Rose:  [#29C7AC BOLD]TAKE A[/#29C7AC BOLD] [italic #8D9EFF]screenshot")

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
                    position["x"], position["y"], config.Move_Speed, pyautogui.easeOutQuad
                )
                print(f" :palm_tree:  [#829460 BOLD]MOVED TO[/#829460 BOLD] {position}")

            # For Clicking
            if key == "click":
                pyautogui.click(position["x"], position["y"])
                print(f" :palm_tree:  [#829460 BOLD]CLICKED AT[/#829460 BOLD] {position}")


            # For dragging with cursor
            if key == "drag":
                pyautogui.dragTo(position["x"], position["y"], config.Drag_Speed)
                print(f" :palm_tree:  [#829460 BOLD]DRAGGED TO[/#829460 BOLD] {position}")

            # For text display
            if key == "write":
                pyautogui.write(action["write"], interval=config.Type_Speed)
                print(f" :palm_tree:  [#829460 BOLD]WROTE[/#829460 BOLD] [italic #8D9EFF]{action['write']} \t")

            # For screen search
            if key == "image":
                Image.open(action["image"]).convert("RGB").save(r"assets\images\images.png")
                DetectImage(r"assets\images\images.png")
                print(f" :palm_tree:  [#829460 BOLD]FOUND[/#829460 BOLD] [italic #8D9EFF]{action['image']}")


            # For wait
            if key == "sleep":
                sleep(action["sleep"])
                print(f" :palm_tree:  [#829460 BOLD]WAITED FOR[/#829460 BOLD] [italic #8D9EFF]{action['sleep']}s")

            # For hotkey input
            if key == "hotkey":
                for current_key in action["hotkey"]:
                    pyautogui.keyDown(current_key)
                for current_key in action["hotkey"]:
                    pyautogui.keyUp(current_key)
                    
                hotkeys_display = display_hotkeys()
                
                print(f" :palm_tree:  [#829460 BOLD]INSERTED HOTKEYS[/#829460 BOLD][italic #F0A500] {hotkeys_display}")

            # For key input
            if key == "key":
                pyautogui.press(action["key"])
                key = action["key"]
                
                if len(key) == 2:
                    # For User
                    print(f" :palm_tree:  [#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key}\t")
                else:
                    # For User
                    print(f" :palm_tree:  [#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key.upper()}\t")

            if key == "screenshot":
                pyautogui.screenshot(r"assets\images\screenshot.png")
                print(" :palm_tree:  [#829460 BOLD]TOOK A[/#829460 BOLD] [italic #8D9EFF]screenshot")
                print("assets\images\screenshot.png")


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
                "No worries",
                "Sure thing!",
            ]
            welcome = choices(welcome)
            print(f"{welcome[0]} :sparkles:")
    except IndexError:
        pass