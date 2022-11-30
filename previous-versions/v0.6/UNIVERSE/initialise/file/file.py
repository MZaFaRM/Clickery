from json import load, JSONDecodeError
from helpers.dir import folder
from helpers.menu import newline_tab
from rich import print

import universal.config as config

def file_input():
    # Gets file
    ftypes = [("json files", "*.json"), ("All files", "*")]
    location = folder(ftypes)
    return test_file(location)


def test_file(location):
    
    # Validate file
    try:
        f = open(location)
        print("[italic #790252]File opened...:dizzy::dizzy::dizzy:")
        config.record = load(f)
        print("[italic #AF0171]File successfully parsed...:dizzy::dizzy::dizzy:")
        file_format(config.record)
        print("[italic #E80F88]File Successfully Initialized...:dizzy::dizzy::dizzy:")
        return 1

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
