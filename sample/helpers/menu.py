from tabulate import tabulate
import sample.universal.config as config
from json import dump
import sqlite3
from rich import print as rich_print
from rich.align import Align
from rich.bar import Bar
from rich.panel import Panel
from rich.console import Group
from rich.progress_bar import ProgressBar
from rich.table import Table


def print_menu():

    # Menu for manual input
    menu_items = []
    single_item = {}
    # configures the table to be displayed at menu
    for item in config.actions_list:
        # capitalises all headings
        single_item["ID"] = item["id"]
        single_item["DESCRIPTION"] = item["description"]
        single_item["CALL"] = '"' + item["call"] + '"'
        menu_items.append(single_item)
        single_item = {}

    # for user
    initiation = "[#F0EBCE italic]Initialized...:dizzy::dizzy::dizzy:"
    panel_group = Group(initiation, ProgressBar(total=3, completed=3))
    print(Panel(panel_group))

    panel_group = Group(
        Align("\nUsage:", align="center"),
        Align(
            "[#ECDBBA]Hover over the screen and press the appropriate call",
            align="center",
        ),
        Align("[#ECDBBA]to perform the related operation", align="center"),
        Align("\n[#FF7777]Supported Operations:", align="center"),
        Align(tabulate(menu_items, "keys", "rounded_grid"), align="center"),
        "\n",
    )

    rich_print()

    print(
        Panel(
            panel_group,
            title="[#FF731D]Main Menu",
            subtitle="Finally, [italic #F0A500]ESC[/italic #F0A500] to Start operation",
            expand=True,
            highlight=True,
        )
    )
    rich_print()

    # starts recording


def SaveJSON():
    # saves recorded actions to json
    add_id()
    with open(r"assets\history\history.json", "w") as save:
        dump(config.record, save, indent=4)


def add_id():
    # adds id to the recorded actions before adding them to json/db
    id = 1
    new_list = []
    for value in config.record:
        new_dict = value.copy()
        new_dict["id"] = id
        id += 1
        new_list.append(new_dict)

    config.record = new_list


def SaveToDB():
    # Connects to the database
    history = sqlite3.connect(r"assets\history\history.db")
    # Sets cursor
    cursor = history.cursor()
    # Converts the dictionary into an string
    text = str(config.record)
    # Gets ready to save it to database
    cursor.execute("INSERT INTO history(JSON) VALUES (?)", (text,))
    # Saves it to database
    history.commit()
    # Terminates connection
    history.close()


def print_recorded():

    # prints all recorded actions
    rich_print()
    text = JSON_lingualizer(config.record)

    heading = Panel(
        Align("[#FFCCB3]Recorded actions:", align="center"),
        highlight=True,
        subtitle="[#6D9886]Step 2",
        subtitle_align="right",
    )

    rich_print(heading)
    
    for i, line in enumerate(text):
        
        i += 1
        # Table to print data in
        recorded = Table(expand=True, box=None, highlight=True)
        recorded.add_column(justify="right")
        recorded.add_column(justify="center")
        recorded.add_column(justify="left")
        
        recorded.add_row(":evergreen_tree:", line, f"{i}")

        rich_print(recorded)


def print(text="", action="Align"):

    if action == "Align":
        rich_print(Align(text, align="center"))
    elif action == "Bar":
        rich_print(Bar(100, 0, 100))
    elif action == "Table":
        rich_print(text, highlight=True)
    elif action == "Pre-Menu":
        rich_print(
            Panel(
                Align(text, align="center"),
                title="[#DC3535]Mode Of Input",
                title_align="center",
                subtitle="[#6D9886]Step 1",
                highlight=True,
                subtitle_align="right",
            )
        )

    elif action == "Post-Menu":
        rich_print(
            Panel(
                Align(text, align="center"),
                title="[#C147E9]Action Modifications",
                title_align="center",
                subtitle="[#6D9886]Step 3",
                highlight=True,
                subtitle_align="right",
            )
        )


def JSON_lingualizer(actions) -> list:

    text = []

    for action in actions:
        for (key, value) in action.items():
            position = value
            # For moving
            if key == "move":

                text.append(f"""[#CF4DCE BOLD]MOVE TO [/]{position}""")

            elif key == "click":

                text.append(f"""[#CF4DCE BOLD]{action["click"].upper()} CLICK AT[/] [italic #8D9EFF]position""")

            elif key == "drag":

                text.append(f"""[#CF4DCE BOLD]DRAG TO [/]{position}""")

            elif key == "write":

                text.append(f'''[#CF4DCE BOLD]WRITE [/][italic #8D9EFF]{action["write"]}[/]''')

            elif key == "image":

                text.append(f'''[#CF4DCE BOLD]SEARCH FOR [/][italic #8D9EFF]{action["image"]}[/]''')

            elif key == "sleep":

                text.append(f"""[#CF4DCE BOLD]WAIT FOR [/][italic #8D9EFF]{action["sleep"]}s[/]""")

            elif key == "hotkey":

                text.append(f'''[#CF4DCE BOLD]INSERT HOTKEYS [/][italic #F0A500]"{" + ".join(action['hotkey'])}"[/]''')

            elif key == "key":

                text.append(f'''[#CF4DCE BOLD]HIT KEY [/][italic #F0A500]{action["key"]}[/]''')

            elif key == "wait_key":

                text.append(f'''[#CF4DCE BOLD]WAIT FOR KEY [/][italic #F0A500]{action["wait_key"]}[/]''')

            elif key == "id":
                pass

            else:
                raise Exception(ValueError)

    return text
