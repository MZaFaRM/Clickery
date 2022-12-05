from tabulate import tabulate
import sample.universal.config as config
from json import dump, dumps
import sqlite3
from rich import print as richPrint
from rich.align import Align
from rich.bar import Bar
from rich.panel import Panel
from rich.json import JSON
from rich.console import Group
from rich.progress_bar import ProgressBar


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
            "[#ECDBBA]Hover over the screen and press the apropriate call",
            align="center",
        ),
        Align("[#ECDBBA]to perform the related operation", align="center"),
        Align("\n[#FF7777]Supported Operations:", align="center"),
        Align(tabulate(menu_items, "keys", "rounded_grid"), align="center"),
        "\n",
    )
    
    richPrint()

    print(
        Panel(
            panel_group,
            title="[#FF731D]Main Menu",
            subtitle="Finally, [italic #F0A500]ESC[/italic #F0A500] to Start operation",
            expand=True,
            highlight=True,
        )
    )
    richPrint()

    # starts recording


def SaveJSON():
    # saves recorded actions to json
    add_id()
    with open(r"assets\json\history.json", "w") as save:
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
    history = sqlite3.connect(r"assets\database\history.db")
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


def PrintRecorded():
    # prints all recorded actions
    richPrint()
    text = JSON(dumps(config.record), indent=4)
    text = Align(text, align="center")
    text = Panel(
        text,
        title="[#FFCCB3]Recorded actions:",
        highlight=True,
        subtitle="[#6D9886]Step 2",
        subtitle_align="right",
    )
    richPrint(text)


def print(text="", action="Align"):
    if action == "Align":
        richPrint(Align(text, align="center"))
    elif action == "Bar":
        richPrint(Bar(100, 0, 100))
    elif action == "Table":
        richPrint(text, highlight=True)
    elif action == "Pre-Menu":
        richPrint(
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
        richPrint(
            Panel(
                Align(text, align="center"),
                title="[#C147E9]Action Modifications",
                title_align="center",
                subtitle="[#6D9886]Step 3",
                highlight=True,
                subtitle_align="right",
            )
        )
