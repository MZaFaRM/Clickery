import pyautogui

from rich import print
from time import sleep
from keyboard import read_key, send
from PIL import Image


import sample.universal.config as config

from sample.pre_record.file_input import file_input
from sample.pre_record.manual_input import manual_input
from sample.pre_record.operations.general import eleos
from sample.post_record.post_record import looper, replacer
from sample.pre_record.operations.hot_key_insert import display_hotkeys
from sample.helpers.dir import clarity
from sample.helpers.menu import (
    newline_tab,
    print_menu,
    add_id,
    SaveJSON,
    SaveToDB,
    PrintRecorded,
)


def initialise(argv):
    # Starts execution and handles keyboard interruption
    try:
        startup(argv)
    except KeyboardInterrupt:
        newline_tab(
            1,
            "\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:\n\n[#082032]{  keyboard interrupt  }",
        )
        pass


def startup(argv):
    # The main part of the code
    eleos(argv)

    # Initialisation
    print("\n\tPress [italic #F0A500]CTRL[/italic #F0A500] for File input...")
    print("\t\tOr Press [italic #F0A500]SHIFT[/italic #F0A500] for  Manual input...\n")

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
            newline_tab(1, "\n:cactus: [bold #8D72E1] FAILED  :cactus:")
            return
    # For manual input
    elif keyboardinput in ["right shift", "shift"]:

        print_menu()
        manual_input()

    # If actions record is empty the process quits
    if not len(config.record):
        PrintRecorded()
        newline_tab(
            1,
            "\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:\n\n[#082032]{  No actions input  }",
        )
        return

    # Adds ids and prints everything that is recorded
    add_id()
    PrintRecorded()

    result = 1

    # For replace and repeat *finalise*
    while len(config.record):

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

        # If actions record is empty the process quits
        if not len(config.record):
            newline_tab(
                1,
                "\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:\n\n[#082032]{  no actions input  }",
            )
            return

        # Saves recorded actions to a assets/json/history.json
        SaveJSON()
        
    try:
        # plays recorded
        play_recorded()
    # Execution of actions can be stopped by moving the cursor to the corner of the screen
    except pyautogui.FailSafeException:
        newline_tab(
            1,
            "\n:cactus: [bold #8D72E1] FAILED [/bold #8D72E1] :cactus:\n\n[#082032]{  execution cancelled  }",
        )
        return
    
    # Saves recorded actions to assets/database/history.db in table HISTORY
    SaveToDB()

    # If all goes well...
    newline_tab(1, "\n:Party_Popper: [bold #8D72E1] SUCCESS :Party_Popper: ")


def replace_menu():
    # The replace menu...

    print(
        "\n\tPress [italic #083AA9]CTRL[/italic #083AA9] to repeat a set of actions..."
    )
    print(
        "\t\tOr Press [italic #083AA9]SHIFT[/italic #083AA9] to replace any action..."
    )
    print(
        "\t\t\tOr Press [italic #083AA9]SPACE[/italic #083AA9] to start execution...\n"
    )


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
                print(f" :palm_tree:  [#829460 BOLD]MOVED TO[/#829460 BOLD] {position}")

            # For left Clicking
            if key == "l-click":
                
                pyautogui.click(button='left')
                                
                current_position = {}

                # Saves position
                x, y = pyautogui.position()
                current_position["x"] = x
                current_position["y"] = y
                
                print(
                    f" :palm_tree:  [#829460 BOLD]LEFT CLICKED AT[/#829460 BOLD]{current_position}"
                )
                
            # For right Clicking
            if key == "r-click":
                
                pyautogui.click(button='right')
                
                current_position = {}

                # Saves position
                x, y = pyautogui.position()
                current_position["x"] = x
                current_position["y"] = y
                
                print(
                    f" :palm_tree:  [#829460 BOLD]RIGHT CLICKED AT [/#829460 BOLD]{current_position}"
                )

            # For dragging with cursor
            if key == "drag":
                pyautogui.dragTo(position["x"], position["y"], config.Drag_Speed)
                print(
                    f" :palm_tree:  [#829460 BOLD]DRAGGED TO[/#829460 BOLD] {position}"
                )

            # For text display
            if key == "write":
                pyautogui.write(action["write"], interval=config.Type_Speed)
                print(
                    f" :palm_tree:  [#829460 BOLD]WROTE[/#829460 BOLD] [italic #8D9EFF]{action['write']} \t"
                )

            # For screen search
            if key == "image":
                Image.open(action["image"]).convert("RGB").save(
                    r"assets\images\images.png"
                )
                DetectImage(r"assets\images\images.png")
                print(
                    f" :palm_tree:  [#829460 BOLD]FOUND[/#829460 BOLD] [italic #8D9EFF]{action['image']}"
                )

            # For wait
            if key == "sleep":
                sleep(action["sleep"])
                print(
                    f" :palm_tree:  [#829460 BOLD]WAITED FOR[/#829460 BOLD] [italic #8D9EFF]{action['sleep']}s"
                )

            # For hotkey input
            if key == "hotkey":
                for current_key in action["hotkey"]:
                    pyautogui.keyDown(current_key)
                for current_key in action["hotkey"]:
                    pyautogui.keyUp(current_key)

                print(
                    f" :palm_tree:  [#829460 BOLD]INSERTED HOTKEYS[/#829460 BOLD][italic #F0A500]{action['hotkey']}"
                )

            # For key input
            if key == "key":
                pyautogui.press(action["key"])
                key = action["key"]

                if len(key) == 2:
                    # For User
                    print(
                        f" :palm_tree:  [#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key}\t"
                    )
                else:
                    # For User
                    print(
                        f" :palm_tree:  [#829460 BOLD]INSERTED KEY[/#829460 BOLD][italic #F0A500] {key.upper()}\t"
                    )

            if key == "screenshot":
                pyautogui.screenshot(action["screenshot"])
                print(
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
