import pyautogui

from rich import print as rich_print
from time import sleep
from keyboard import read_key, send, press, release, wait
from PIL import Image
from rich.align import Align
from rich.panel import Panel
import time
from threading import Thread
from playsound import playsound

import sample.universal.config as config

from .pre_record.file_input import file_input
from .pre_record.manual_input import manual_input
from .pre_record.operations.general import egg
from .post_record.post_record import looper, replacer
from .helpers.dir import clarity

from .helpers import menu

from rich.table import Table

rich_print()
rich_print(Align("[#F9ED69]            ,---.'|                                ,--.                           |          ", align="center"))
rich_print(Align("[#F9ED69]               ,--,                                                              - -         ", align="center"))
rich_print(Align("[#F9ED69]  ,----..   |   | :       ,---,   ,----..      ,--/  /|     ,---,. ,-.----.       |          ", align="center"))
rich_print(Align("[#F9ED69] /   /   \  :   : |    ,`--.' |  /   /   \  ,---,': / '   ,'  .' | \    /  \           ,---, ", align="center"))
rich_print(Align("[#F08A5D]|   :     : |   ' :    |   :  : |   :     : :   : '/ /  ,---.'   | ;   :    \         /_ ./| ", align="center"))
rich_print(Align("[#F08A5D].   |  ;. / ;   ; '    :   |  ' .   |  ;. / |   '   ,   |   |   .' |   | .\ :   ,---, |  ' : ", align="center"))
rich_print(Align("[#F08A5D].   ; /--`  '   | |__  |   :  | .   ; /--`  '   |  /    :   :  |-, .   : |: |  /___/ \.  : | ", align="center"))
rich_print(Align("[#F08A5D];   | ;     |   | :.'| '   '  ; ;   | ;     |   ;  ;    :   |  ;/| |   |  \ :   .  \  \ ,' ' ", align="center"))
rich_print(Align("[#B83B5E]|   : |     '   :    ; |   |  | |   : |     :   '   \   |   :   .' |   : .  /    \  ;  `  ,' ", align="center"))
rich_print(Align("[#B83B5E].   | '___  |   |  ./  '   :  ; .   | '___  |   |    '  |   |  |-, ;   | |  \     \  \    '  ", align="center"))
rich_print(Align("[#B83B5E]'   ; : .'| ;   : ;    |   |  ' '   ; : .'| '   : |.  \ '   :  ;/| |   | ;\  \     '  \   |  ", align="center"))
rich_print(Align("[#B83B5E]'   | '/  : |   ,/     '   :  | '   | '/  : |   | '_\.' |   |    \ :   ' | \.'      \  ;  ;  ", align="center"))
rich_print(Align("[#6A2C70] \   \ .'              '---'     \   \ .'   ;   |,'     |   | ,'   |   |.'            \  ' ; ", align="center"))
rich_print(Align("[#6A2C70]|   :    /  '---'      ;   |.'  |   :    /  '   : |     |   :   .' :   : :-'         :  \  \ ", align="center"))
rich_print(Align("[#6A2C70]  `---`                           `---`     '---'       `----'     `---'               `--`  ", align="center"))

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
            menu.print_recorded()
            error("Input Error")
            return
    # For manual input
    elif keyboardinput in ["right shift", "shift"]:
        print()
        menu.print_menu()
        manual_input()

    # If actions record is empty the process quits
    if not len(config.record):
        menu.print_recorded()
        error("No Actions Input")
        return

    # Adds ids and prints everything that is recorded
    menu.add_id()
    menu.print_recorded()

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
    rich_print()
    text = Align(":Party_Popper: [bold #8D72E1] SUCCESS :Party_Popper: ", align="center")
    rich_print(Panel(text, subtitle="[#6D9886]The End", subtitle_align="right"))


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
                
                rich_print("[#7D9D9C italic]Moving to location...")
                
                i += 1
                
                pyautogui.moveTo(
                    position["x"],
                    position["y"],
                    config.Move_Speed,
                    pyautogui.easeOutQuad,
                )

                print("\033[A                    \033[A")
                
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]MOVED TO[/#829460 BOLD] {position}", f"{i}"
                )
                
            # For Clicking
            elif key == "click":
                
                rich_print(f" [#7D9D9C italic]Inserting {action['click']} click...")
                
                i += 1
                pyautogui.click(button=action['click'].lower())
                current_position = {}
                # Saves position
                x, y = pyautogui.position()
                current_position["x"] = x
                current_position["y"] = y

                print("\033[A                        \033[A")

                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]{action['click']} CLICKED AT [/#829460 BOLD]{current_position}".upper(), f"{i}"
                )
                
            # For dragging with cursor
            elif key == "drag":
                
                rich_print(" [#7D9D9C italic]Dragging cursor to location...")
                
                i += 1
                
                pyautogui.dragTo(position["x"], position["y"], config.Drag_Speed)
                print("\033[A                               \033[A")
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]DRAGGED TO[/#829460 BOLD] {position}", f"{i}"
                )
            # For text display
            elif key == "write":
                
                rich_print(" [#7D9D9C italic]Writing given text...")
                
                i += 1
                
                pyautogui.write(action["write"], interval=config.Type_Speed)
                print("\033[A                     \033[A")
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]WROTE[/#829460 BOLD] [italic #8D9EFF]{action['write']}", f"{i}"
                )
            # For screen search
            elif key == "image":
                
                i += 1
                
                rich_print(" [#7D9D9C italic]Searching for given image...")
                
                try:
                    Image.open(action["image"]).convert("RGB").save(
                        r"assets\images\images.png"
                    )
                except FileNotFoundError:
                    error("Image to wait for not found")
                    return
                
                detect_image(r"assets\images\images.png")
                print("\033[A                          \033[A")
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]FOUND[/#829460 BOLD] [italic #8D9EFF]{action['image']}", f"{i}"
                )
                
            # For wait
            elif key == "sleep":
                
                rich_print(" [#7D9D9C italic]Waiting for given time...")
                
                i += 1
                
                sleep(action["sleep"])
                print("\033[A                          \033[A")
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]WAITED FOR[/#829460 BOLD] [italic #8D9EFF]{action['sleep']}s", f"{i}"
                )
            # For hotkey input
            elif key == "hotkey":
                
                rich_print(" [#7D9D9C italic]Inserting given hotkey...")
                
                i += 1
                
                for current_key in action["hotkey"]:
                    press(current_key)
                for current_key in action["hotkey"]:
                    release(current_key)
                print("\033[A                          \033[A")
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]INSERTED HOTKEYS[/#829460 BOLD] [italic #F0A500]{action['hotkey']}", f"{i}"
                )
                
            # For key input
            elif key == "key":
                
                i += 1
                
                rich_print(" [#7D9D9C italic]Inserting given key...")
                
                # Clicks key
                time.sleep(0.3)
                send(action["key"])
                print("\033[A                       \033[A")
                
                key = action["key"]
                
                # For User
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key}", f"{i}"
                )
                
            # For key input
            elif key == "wait_key":
                
                rich_print(" [#7D9D9C italic]Waiting for given key input...")
                
                i += 1
                
                # waits for the given key
                wait(action["wait_key"])
                print("\033[A                              \033[A")
                
                key = action["wait_key"]
                
                # For User
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]WAITED FOR[/#829460 BOLD][italic #F0A500] {key}", f"{i}"
                )
                    
            elif key == "screenshot":
                
                rich_print(" [#7D9D9C italic]Taking a screenshot...")
                
                i += 1
                
                pyautogui.screenshot(action["screenshot"])
                print("\033[A                       \033[A")
                recorded.add_row(
                    ":palm_tree:",  f"[#829460 BOLD]SCREENSHOT SAVED AT[/#829460 BOLD] [italic #8D9EFF]{action['screenshot']}", f"{i}"
                )
                
            else:
                continue
                
            rich_print(recorded)
            thread = Thread(target=playing_sound)
            thread.start()
            


def playing_sound():
	playsound(r"assets\sounds\mixkit-arrow-whoosh-1491.wav")
                
                
def detect_image(path):
    while True:
        image_location = pyautogui.locateCenterOnScreen(path, confidence=0.9)
        if image_location:
            pyautogui.moveTo(image_location)
            return
        
def error(error=""):
    rich_print()
    text = Align(":cactus: [bold #8D72E1] FAILED [/] :cactus:", align="center")
    error = "[#6D9886]" + error
    rich_print(Panel(text, subtitle=error, subtitle_align="right"))
    
    
def release_all():
    keys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
    
    for key in keys:
        pyautogui.keyUp(key)
    


if __name__ == "sample.core":
    # Excecuted to increase the quality of ktinkter windows
    clarity()
