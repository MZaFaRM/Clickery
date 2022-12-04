import pyautogui

from rich import print as richPrint
from time import sleep
from keyboard import read_key, send
from PIL import Image
from rich.align import Align
from rich import get_console
from rich.panel import Panel


import sample.universal.config as config

from sample.pre_record.file_input import file_input
from sample.pre_record.manual_input import manual_input
from sample.pre_record.operations.general import egg
from sample.post_record.post_record import looper, replacer
from sample.helpers.dir import clarity

import sample.helpers.menu as menu


def initialise(argv):
    # Starts execution and handles keyboard interruption
    try:
        startup(argv)
    except KeyboardInterrupt:
        richPrint(
            "\n\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:\n\n[#082032]{  keyboard interrupt  }"
        )
        pass


def startup(argv):
    egg(argv)

    # The main part of the code
    # Initialisation
    print()
    Input_type = """\nPress [italic #F0A500]CTRL[/italic #F0A500] for File input...
    Or Press [italic #F0A500]SHIFT[/italic #F0A500] for  Manual input...\n"""

    menu.print(Input_type, action="Pre-Menu")

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
            menu.print("\n:cactus: [bold #8D72E1] FAILED  :cactus:")
            return
    # For manual input
    elif keyboardinput in ["right shift", "shift"]:
        print()
        menu.print_menu()
        manual_input()

    # If actions record is empty the process quits
    if not len(config.record):
        menu.PrintRecorded()
        menu.print(":cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:")
        menu.print("\n[#082032]{  No actions input  }")
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
            menu.print("\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:")
            menu.print("\n[#082032]{  no actions input  }")
            return

        # Saves recorded actions to a assets/json/history.json
        menu.SaveJSON()

    try:
        # plays recorded
        play_recorded()
    # Execution of actions can be stopped by moving the cursor to the corner of the screen
    except pyautogui.FailSafeException:
        menu.print("\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:")
        menu.print("\n[#082032]{  execution cancelled  }")
        return

    # Saves recorded actions to assets/database/history.db in table HISTORY
    menu.SaveToDB()

    # If all goes well...
    richPrint()
    text = Align(":Party_Popper: [bold #8D72E1] SUCCESS :Party_Popper: ", align="center")
    richPrint(Panel(text, subtitle="[#001253]The end", subtitle_align="right"))


def post_record_menu():
    # The post record menu...
    print()
    
    MENU = """\nPress [italic #083AA9]CTRL[/italic #083AA9] to repeat a set of actions...
 Or Press [italic #083AA9]SHIFT[/italic #083AA9] to replace any action...
  Or Press [italic #083AA9]SPACE[/italic #083AA9] to start execution...\n"""

    menu.print(MENU, action="Post-Menu")
    print()

def play_recorded():

    # Does what is recorded
    for action in config.record:
        for key, value in action.items():

            position = value
            # For moving
            if key == "move":
                pyautogui.moveTo(
                    position["x"],
                    position["y"],
                    config.Move_Speed,
                    pyautogui.easeOutQuad,
                )
                menu.print(
                    f" :palm_tree:  [#829460 BOLD]MOVED TO[/#829460 BOLD] {position}"
                )

            # For left Clicking
            if key == "l-click":

                pyautogui.click(button="left")

                current_position = {}

                # Saves position
                x, y = pyautogui.position()
                current_position["x"] = x
                current_position["y"] = y

                menu.print(
                    f" :palm_tree:  [#829460 BOLD]LEFT CLICKED AT [/#829460 BOLD]{current_position}"
                )

            # For right Clicking
            if key == "r-click":

                pyautogui.click(button="right")

                current_position = {}

                # Saves position
                x, y = pyautogui.position()
                current_position["x"] = x
                current_position["y"] = y

                menu.print(
                    f" :palm_tree:  [#829460 BOLD]RIGHT CLICKED AT [/#829460 BOLD]{current_position}"
                )

            # For dragging with cursor
            if key == "drag":
                pyautogui.dragTo(position["x"], position["y"], config.Drag_Speed)
                menu.print(
                    f" :palm_tree:  [#829460 BOLD]DRAGGED TO[/#829460 BOLD] {position}"
                )

            # For text display
            if key == "write":
                pyautogui.write(action["write"], interval=config.Type_Speed)
                menu.print(
                    f" :palm_tree:  [#829460 BOLD]WROTE[/#829460 BOLD] [italic #8D9EFF]{action['write']} \t"
                )

            # For screen search
            if key == "image":
                Image.open(action["image"]).convert("RGB").save(
                    r"assets\images\images.png"
                )
                DetectImage(r"assets\images\images.png")
                menu.print(
                    f" :palm_tree:  [#829460 BOLD]FOUND[/#829460 BOLD] [italic #8D9EFF]{action['image']}"
                )

            # For wait
            if key == "sleep":
                sleep(action["sleep"])
                menu.print(
                    f" :palm_tree:  [#829460 BOLD]WAITED FOR[/#829460 BOLD] [italic #8D9EFF]{action['sleep']}s"
                )

            # For hotkey input
            if key == "hotkey":
                for current_key in action["hotkey"]:
                    pyautogui.keyDown(current_key)
                for current_key in action["hotkey"]:
                    pyautogui.keyUp(current_key)

                menu.print(
                    f" :palm_tree:  [#829460 BOLD]INSERTED HOTKEYS[/#829460 BOLD] [italic #F0A500]{action['hotkey']}"
                )

            # For key input
            if key == "key":
                pyautogui.press(action["key"])
                key = action["key"]

                if len(key) == 2:
                    # For User
                    menu.print(
                        f" :palm_tree:  [#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key}\t"
                    )
                else:
                    # For User
                    menu.print(
                        f" :palm_tree:  [#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key.upper()}\t"
                    )

            if key == "screenshot":
                pyautogui.screenshot(action["screenshot"])
                menu.print(
                    " :palm_tree:  [#829460 BOLD]TOOK A[/#829460 BOLD] [italic #8D9EFF]screenshot"
                )


def DetectImage(path):
    while True:
        image_location = pyautogui.locateCenterOnScreen(path, confidence=0.9)
        if image_location:
            pyautogui.moveTo(image_location)
            return


if __name__ == "sample.core":
    # Excecuted to increase the quality of ktinkter windows
    clarity()
