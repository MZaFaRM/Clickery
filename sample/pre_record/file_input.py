from json import load, JSONDecodeError
from rich import print

import sample.universal.config as config
from sample.helpers.dir import folder
from sample.helpers.menu import newline_tab


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
            ":x: [italic #CC3636]No file provided...",
        )
    except JSONDecodeError:
        print(
            ":x: [italic #CC3636]JSON Decode Error, please check your json file...",
        )
    except UnicodeDecodeError:
        print(
            ":x: [italic #CC3636]Error parsing file..."
        )
    except ValueError:
        print(
            ":x: [italic #CC3636]Format error, check out the documentation on how to format your json file..."
        )
        newline_tab(1, "https://github.com/MZaFaRM/CLICKERY/blob/main/Guide/format.md")


def file_format(record):
    # checks the keys in the file
    actions = [
        "move",
        "l-click",
        "r-click",
        "drag",
        "write",
        "image",
        "sleep",
        "hotkey",
        "key",
        "screenshot",
        "id",
    ]
    for item in record:
        for key, value in item.items():
            if key not in actions:
                raise ValueError
    return 1
