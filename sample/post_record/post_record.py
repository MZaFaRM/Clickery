from keyboard import read_key
from tabulate import tabulate
from rich.align import Align
from rich.panel import Panel
from rich.console import Group
import sample.post_record.replacer as replace
import sample.post_record.looper as loop
import sample.pre_record.operations.general as general
import sample.universal.config as config
from sample.helpers.menu import add_id, print_recorded
from sample.helpers.menu import print as menu_print
from rich import print


def replacer():

    # shows the replace_window
    replace.replace_window()

    # Checks if the user input any value
    if not replace.replace_id:
        return 0

    # For getting user input
    print_menu_replace()
    keyboardinput = read_key()

    # Stop recording
    if keyboardinput == "esc":
        pass

    for item in config.replace_list:

        # Becomes true when key input is in replace functions list
        Hades = False

        if item["call"] == keyboardinput:

            Hades = True

            if item["function"] == "delete_action()":
                # replace ID does't correspond to the index therefore it must be decremented by one before use
                # decrementing done by 'delete_action' function
                general.delete_action(replace.replace_id)
                break

            # actions is the dictionary of the action
            action = eval(f"general.{item['function']}")

            if action:
                # replaced the element at ReplaceIndex with action
                config.record[(replace.replace_id) - 1] = action
                break

    if not Hades:
        # Executed if the user input is not present in replace functions list
        print(Align(":Cross_Mark: [#DC3535] Invalid Input", align="center"))

    # re-adds id after modification
    add_id()
    # Lists all recorded actions
    print_recorded()

    # reset replace_id for reuse
    replace.replace_id = 0

    return 1


def print_menu_replace():
    # Menu for manual input
    menu_items = []
    single_item = {}
    for item in config.replace_list:
        single_item["ID"] = item["id"]
        single_item["DESCRIPTION"] = item["description"]
        single_item["CALL"] = '"' + item["call"] + '"'
        menu_items.append(single_item)
        single_item = {}

    panel_group = Group(
        Align("\nUsage:", align="center"),
        Align(
            "[#ECDBBA]Hover over the screen and press the apropriate call",
            align="center",
        ),
        Align("[#ECDBBA]to perform the related operation", align="center"),
        Align("\n[#FF7777]Supported Operations:", align="center"),
        Align(tabulate(menu_items, "keys", "rounded_grid"), align="center"),
        "\n",
    )

    menu_print(
        Panel(
            panel_group,
            title="[#FF731D]Replace Menu",
            highlight=True,
        )
    )

    print()


def looper():

    # initiates looper process
    loop.loop_window()

    # Checks if the user input any value
    if not loop.loop_final:
        return 0

    # else extract data
    loops = loop.loop_final["LoopCount"]
    start = loop.loop_final["LoopStart"]
    end = loop.loop_final["LoopEnd"]
    InsertAfter = loop.loop_final["InsertAfter"]

    # Gets the loop to multiply
    looper_list = config.record[start - 1 : end]

    # Multiplies the loop
    looper_list = looper_list * loops

    # Adds the elements back to list
    for action in reversed(looper_list):
        config.record.insert(InsertAfter, action)

    # re-adds id after modification
    add_id()

    # Lists all recorded actions
    print_recorded()

    # reset loop_final for reuse
    loop.loop_final = []

    return 1
