from json import load, JSONDecodeError
from helpers.dir import folder
from helpers.menu import newline_tab
from rich import print

import universal.config as config


def file_input():
    # Gets file
    ftypes = [("json files", "*.json"), ("All files", "*")]
    # creates a dialogue box for getting the file
    location = folder(ftypes)
    # returns location for file
    return test_file(location)


def test_file(location):

    # Validate file
    try:
        f = open(location)
        print("[italic #B6E2A1]File opened...:dizzy::dizzy::dizzy:")
        # checks for json format and assignes it to config.record
        config.record = load(f)
        print("[italic #B6E2A1]File successfully parsed...:dizzy::dizzy::dizzy:")
        # calls 'file_format' to check for 'record' format
        file_format(config.record)
        print("[italic #B6E2A1]File Successfully Initialized...:dizzy::dizzy::dizzy:")
        return 1

    # Possible exceptions
    except FileNotFoundError:
        print(
            "[italic #CC3636]No file provided...:Heavy_exclamation_mark::Heavy_exclamation_mark::Heavy_exclamation_mark:",
        )
    except JSONDecodeError:
        print(
            "[italic #CC3636]JSON Decode Error, please check your json file...:Heavy_exclamation_mark::Heavy_exclamation_mark::Heavy_exclamation_mark:",
        )
    except UnicodeDecodeError:
        print(
            "[italic #CC3636]Error opening file...:Heavy_exclamation_mark::Heavy_exclamation_mark::Heavy_exclamation_mark:"
        )
    except ValueError:
        print(
            "[italic #CC3636]Format error, check out the documentation on how to format your json file...:Heavy_exclamation_mark::Heavy_exclamation_mark::Heavy_exclamation_mark:"
        )
        newline_tab(1, "https://github.com/MZaFaRM/Clicker")


def file_format(record):
    # checks the keys in the file
    actions = [
        "move",
        "click",
        "drag",
        "write",
        "image",
        "sleep",
        "hotkey",
        "key",
        "screenshot",
        "id",
    ]
    for key, value in record:
        if key not in actions:
            raise ValueError
    return 1
