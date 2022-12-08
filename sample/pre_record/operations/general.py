from rich import print
from re import search
from random import choices
from sample.helpers.dir import folder
import sample.universal.config as config
from tkinter.filedialog import asksaveasfile
from keyboard import normalize_name
from playsound import playsound
from threading import Thread
import os
import pyautogui
from sample.pre_record.operations.key_insert import return_key_input
from sample.pre_record.operations.hot_key_insert import return_hot_key_input
from sample.pre_record.operations.wait_seconds import return_wait
from sample.pre_record.operations.text_input import return_write
from sample.pre_record.operations.wait_for_key import return_wait_key
from rich.table import Table


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
        align_text("SEARCH FOR", f"[italic #8D9EFF]{action['image']}")

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
    align_text(description="MOVE TO", parameter=current_position)

    return action


def LeftClickCursor():

    # Declares dictionaries
    action = {}

    # Saves action
    action["l-click"] = 1

    # For user
    align_text(description="LEFT CLICK AT", parameter="[italic #8D9EFF]position")

    return action


def RightClickCursor():

    # Declares dictionaries
    action = {}

    # Saves action
    action["r-click"] = 1

    # For user
    align_text(description="RIGHT CLICK AT", parameter="[italic #8D9EFF]position")

    return action


def TextInput():

    # Gets text
    text = return_write()
    action = {}

    if text:
        action["write"] = text
        # For user
        align_text("WRITE", f"[italic #8D9EFF]{action['write']}")

        return action

    return 0


def KeyInput():

    # Declares dictionaries
    action = {}

    # Gets key to input
    key = return_key_input()

    if key:
        
        # For user
        align_text("HIT KEY", f"[italic #F0A500]{key}")
                  
        # Saves action
        action["key"] = normalize_name(key)

        return action

    return 0

def WaitForKey():

    # Declares dictionaries
    action = {}

    # Gets key to input
    key = return_wait_key()

    if key:
        
        # For user
        align_text("WAIT FOR KEY", f"[italic #F0A500]{key}")
                  
        # Saves action
        action["wait-key"] = normalize_name(key)

        return action

    return 0


def Wait():

    action = {}
    # gets input
    time = return_wait()
    if time != "-":
        action["sleep"] = time
        
        # For user
        align_text("WAIT FOR", f"[italic #8D9EFF]{action['sleep']}s")

        return action
    else:
        return 0


def Pop(id=0):

    if not id:
        # Delete last action
        try:
            delete = config.record.pop()

        except IndexError:
            align_text("[#D2001A italic]No actions to remove", "", ":cross_mark:", increment="None")

            return
    else:
        delete = config.record.pop(id - 1)
        
    align_text(f"[#7D9D9C italic]{delete}", "removed", ":wilted_flower:", description_style=False, increment="Negative")


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
    align_text("DRAG TO", current_position)

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
        align_text("INSERT HOTKEYS", f"[italic #F0A500]{hotkeys}")

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
        # os.remove(location)
        action["screenshot"] = location

        # For User
        align_text("SAVE A SCREENSHOT AT", f"[italic #8D9EFF]{location}")

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

def align_text(description="", parameter="", emoji=":rose:", description_style=True, increment="True"):
    
    global index
    
    try:
        index += 1
    except NameError:
        index = 1
        
    id = index
        
    if increment == "None":
        thread = Thread(target = recording_action, args=("none", ))
        thread.start()
        index -= 1
        id = ""
    elif increment == "Negative":
        thread = Thread(target = recording_action, args=("pop", ))
        thread.start()
        index -= 2
        id = ""
    else:
        thread = Thread(target = recording_action, args=("", ))
        thread.start()
    
    recorded = Table(expand=True, box=None, highlight=True)
    recorded.add_column(justify="right")
    recorded.add_column(justify="center")
    recorded.add_column(justify="left")
    
    if description_style:
        description = "[#29C7AC BOLD]" + str(description) + "[/] " + str(parameter)
    else:
        description = str(description) + " " + str(parameter)

    
    recorded.add_row(emoji, description, str(id))
    
    print(recorded)
    
def recording_action(function=""):
    
    if function == "pop":
	    playsound(r"assets\sounds\the-rustle-of-a-bush-106001.mp3")

    elif function == "none":
	    playsound(r"assets\sounds\mixkit-small-wood-plank-pile-drop-3141.wav")
     
    else:
	    playsound(r"assets\sounds\mixkit-tree-branch-brake-2943.wav")
