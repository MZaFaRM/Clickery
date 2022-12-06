import pyautogui

from rich import print as richPrint
from time import sleep
from keyboard import read_key
from PIL import Image
from rich.align import Align
from rich import get_console
from rich.panel import Panel
from rich.progress_bar import ProgressBar


import sample.universal.config as config

from sample.pre_record.file_input import file_input
from sample.pre_record.manual_input import manual_input
from sample.pre_record.operations.general import egg
from sample.post_record.post_record import looper, replacer
from sample.helpers.dir import clarity

import sample.helpers.menu as menu

import time

from rich.live import Live
from rich.table import Table

richPrint()
richPrint(Align("[#F9ED69]            ,---.'|                                ,--.                           |          ", align="center"))
richPrint(Align("[#F9ED69]               ,--,                                                              - -         ", align="center"))
richPrint(Align("[#F9ED69]  ,----..   |   | :       ,---,   ,----..      ,--/  /|     ,---,. ,-.----.       |          ", align="center"))
richPrint(Align("[#F9ED69] /   /   \  :   : |    ,`--.' |  /   /   \  ,---,': / '   ,'  .' | \    /  \           ,---, ", align="center"))
richPrint(Align("[#F08A5D]|   :     : |   ' :    |   :  : |   :     : :   : '/ /  ,---.'   | ;   :    \         /_ ./| ", align="center"))
richPrint(Align("[#F08A5D].   |  ;. / ;   ; '    :   |  ' .   |  ;. / |   '   ,   |   |   .' |   | .\ :   ,---, |  ' : ", align="center"))
richPrint(Align("[#F08A5D].   ; /--`  '   | |__  |   :  | .   ; /--`  '   |  /    :   :  |-, .   : |: |  /___/ \.  : | ", align="center"))
richPrint(Align("[#F08A5D];   | ;     |   | :.'| '   '  ; ;   | ;     |   ;  ;    :   |  ;/| |   |  \ :   .  \  \ ,' ' ", align="center"))
richPrint(Align("[#B83B5E]|   : |     '   :    ; |   |  | |   : |     :   '   \   |   :   .' |   : .  /    \  ;  `  ,' ", align="center"))
richPrint(Align("[#B83B5E].   | '___  |   |  ./  '   :  ; .   | '___  |   |    '  |   |  |-, ;   | |  \     \  \    '  ", align="center"))
richPrint(Align("[#B83B5E]'   ; : .'| ;   : ;    |   |  ' '   ; : .'| '   : |.  \ '   :  ;/| |   | ;\  \     '  \   |  ", align="center"))
richPrint(Align("[#B83B5E]'   | '/  : |   ,/     '   :  | '   | '/  : |   | '_\.' |   |    \ :   ' | \.'      \  ;  ;  ", align="center"))
richPrint(Align("[#6A2C70] \   \ .'              '---'     \   \ .'   ;   |,'     |   | ,'   |   |.'            \  ' ; ", align="center"))
richPrint(Align("[#6A2C70]|   :    /  '---'      ;   |.'  |   :    /  '   : |     |   :   .' :   : :-'         :  \  \ ", align="center"))
richPrint(Align("[#6A2C70]  `---`                           `---`     '---'       `----'     `---'               `--`  ", align="center"))

def initialise(argv):
    # Starts execution and handles keyboard interruption
    try:
        startup(argv)
    except KeyboardInterrupt:
        error("Keyboard Interrupt")
        pass


def startup(argv):
    egg(argv)

    # The main part of the code
    # Initialisation
    print()
    Input_type = """\nPress [italic #F0A500]ENTER[/italic #F0A500] for File input...
    Or Press [italic #F0A500]SHIFT[/italic #F0A500] for  Manual input...\n"""

    menu.print(Input_type, action="Pre-Menu")

    keyboardinput = ""

    # Stores keyboard input
    while keyboardinput not in ["enter", "right shift", "shift"]:
        keyboardinput = read_key()
    # For file input
    if keyboardinput == "enter":
        pyautogui.keyUp("enter")
        status = file_input()
        if not status:
            menu.PrintRecorded()
            error("Input Error")
            return
    # For manual input
    elif keyboardinput in ["right shift", "shift"]:
        print()
        menu.print_menu()
        manual_input()

    # If actions record is empty the process quits
    if not len(config.record):
        menu.PrintRecorded()
        error("No Actions Input")
        return

    # Adds ids and prints everything that is recorded
    menu.add_id()
    menu.PrintRecorded()

    result = 1

    # For replace and repeat *finalise*
    while len(config.record):

        if result:
            post_record_menu()
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
            menu.SaveJSON()
            break

        # If actions record is empty the process quits
        if not len(config.record):
            error("No Actions Input")
            return

        # Saves recorded actions to a assets/json/history.json
        menu.SaveJSON()

    try:
        # plays recorded
        play_recorded()
    # Execution of actions can be stopped by moving the cursor to the corner of the screen
    except pyautogui.FailSafeException:
        error("Execution Cancelled")
        return

    # Saves recorded actions to assets/database/history.db in table HISTORY
    menu.SaveToDB()

    # If all goes well...
    richPrint()
    text = Align(":Party_Popper: [bold #8D72E1] SUCCESS :Party_Popper: ", align="center")
    richPrint(Panel(text, subtitle="[#6D9886]The End", subtitle_align="right"))


def post_record_menu():
    # The post record menu...
    print()
    
    MENU = """\nPress [italic #332FD0]CTRL[/] to repeat a set of actions...
        Or Press [italic #332FD0]SHIFT[/] to replace any action...
                Or Press [italic #332FD0]SPACE[/] to start execution...\n"""

    menu.print(MENU, action="Post-Menu")

def play_recorded():
    
    i = 0

    # Does what is recorded
    for action in config.record:
        for key, value in action.items():
            
            recorded = Table(expand=True, box=None, highlight=True)
            recorded.add_column(justify="right")
            recorded.add_column(justify="center")
            recorded.add_column(justify="left")
    
            position = value
            # For moving
            if key == "move":
                
                i += 1
                
                pyautogui.moveTo(
                    position["x"],
                    position["y"],
                    config.Move_Speed,
                    pyautogui.easeOutQuad,
                )
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]MOVED TO[/#829460 BOLD] {position}", f"{i}"
                )
                
            # For left Clicking
            elif key == "l-click":
                
                i += 1
                pyautogui.click(button="left")
                current_position = {}
                # Saves position
                x, y = pyautogui.position()
                current_position["x"] = x
                current_position["y"] = y
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]LEFT CLICKED AT [/#829460 BOLD]{current_position}", f"{i}"
                )
            # For right Clicking
            elif key == "r-click":
                
                i += 1
                pyautogui.click(button="right")
                current_position = {}
                # Saves position
                x, y = pyautogui.position()
                current_position["x"] = x
                current_position["y"] = y
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]RIGHT CLICKED AT [/#829460 BOLD]{current_position}", f"{i}"
                )
                
            # For dragging with cursor
            elif key == "drag":
                
                i += 1
                
                pyautogui.dragTo(position["x"], position["y"], config.Drag_Speed)
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]DRAGGED TO[/#829460 BOLD] {position}", f"{i}"
                )
            # For text display
            elif key == "write":
                
                i += 1
                
                pyautogui.write(action["write"], interval=config.Type_Speed)
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]WROTE[/#829460 BOLD] [italic #8D9EFF]{action['write']}", f"{i}"
                )
            # For screen search
            elif key == "image":
                
                i += 1
                
                try:
                    Image.open(action["image"]).convert("RGB").save(
                        r"assets\images\images.png"
                    )
                except FileNotFoundError:
                    error("Image to wait for not found")
                DetectImage(r"assets\images\images.png")
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]FOUND[/#829460 BOLD] [italic #8D9EFF]{action['image']}", f"{i}"
                )
                
            # For wait
            elif key == "sleep":
                
                i += 1
                
                sleep(action["sleep"])
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]WAITED FOR[/#829460 BOLD] [italic #8D9EFF]{action['sleep']}s", f"{i}"
                )
            # For hotkey input
            elif key == "hotkey":
                
                i += 1
                
                for current_key in action["hotkey"]:
                    pyautogui.keyDown(current_key)
                for current_key in action["hotkey"]:
                    pyautogui.keyUp(current_key)
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]INSERTED HOTKEYS[/#829460 BOLD] [italic #F0A500]{action['hotkey']}", f"{i}"
                )
                
            # For key input
            elif key == "key":
                
                i += 1
                
                pyautogui.press(action["key"])
                key = action["key"]
                if len(key) == 2:
                    # For User
                    recorded.add_row(
                        ":palm_tree:",  f"[#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key}", f"{i}"
                    )
                else:
                    # For User
                    recorded.add_row(
                        ":palm_tree:",  f"[#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key.upper()}", f"{i}"
                    )
                    
            elif key == "screenshot":
                
                i += 1
                
                pyautogui.screenshot(action["screenshot"])
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]SCREENSHOT SAVED AT[/#829460 BOLD] [italic #8D9EFF]{action['screenshot']}", f"{i}"
                )
                
            else:
                continue
                
            richPrint(recorded)
                
                
def DetectImage(path):
    while True:
        image_location = pyautogui.locateCenterOnScreen(path, confidence=0.9)
        if image_location:
            pyautogui.moveTo(image_location)
            return
        
def error(error=""):
    richPrint()
    text = Align(":cactus: [bold #8D72E1] FAILED [/] :cactus:", align="center")
    error = "[#6D9886]" + error
    richPrint(Panel(text, subtitle=error, subtitle_align="right"))
    


if __name__ == "sample.core":
    # Excecuted to increase the quality of ktinkter windows
    clarity()
