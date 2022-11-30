from tabulate import tabulate
import universal.config as config
from json import dump
import sqlite3
from rich import print


def print_menu():
    # Menu for manual input
    menu_items = []
    single_item = {}
    for item in config.actions_list:
        single_item["ID"] = item["id"]
        single_item["DESCRIPTION"] = item["description"]
        single_item["CALL"] = '"' + item["call"] + '"'
        menu_items.append(single_item)
        single_item = {}

    newline_tab(1, sentence="[#F0EBCE italic]Initialized...:dizzy::dizzy::dizzy:")
    newline_tab(1, sentence="Usage:")
    newline_tab(
        1,
        sentence="[#ECDBBA]\tHover over the screen and press the apropriate call \n\t\tto perform the related operation",
    )
    newline_tab(1, sentence="Supported Operations:")
    print(tabulate(menu_items, "keys", "rounded_grid"), end="\n\n")
    newline_tab(
        1, sentence="Finally, [italic #F0A500]ESC[/italic #F0A500] to Start operation"
    )


def newline_tab(n, sentence=""):
    print(sentence)
    for i in range(n):
        print()


def SaveJSON():
    add_id()
    with open(r"assets\json\history.json", "w") as save:
        dump(config.record, save, indent=4)


def add_id():
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
    print(f"\n[#FFCCB3]Recorded actions:[/#FFCCB3]\n")
    print(config.record)
