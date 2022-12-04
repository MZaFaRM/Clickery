from json import load, JSONDecodeError
from rich import print
from rich.progress_bar import ProgressBar
from rich.console import Group

import sample.universal.config as config
from sample.helpers.dir import folder

from rich.layout import Layout
from rich.panel import Panel
from rich.align import Align
from rich.live import Live
import time
from rich.console import Console


def file_input():
    # Gets file
    ftypes = [("json files", "*.json"), ("All files", "*")]
    # creates a dialogue box for getting the file
    location = folder(ftypes)
    # returns location for file
    return test_file(location)


def test_file(location):
    
    print()

    steps_for_verification = [
        {
            "output": "[italic #B6E2A1]File opened...:dizzy::dizzy::dizzy:",
            "action": "open(location)",
        },
        {
            "output": "[italic #B6E2A1]File successfully parsed...:dizzy::dizzy::dizzy:",
            "action": "load(open(location))",
        },
        {
            "output": "[italic #B6E2A1]File Successfully Initialized...:dizzy::dizzy::dizzy:",
            "action": "file_format(load(open(location)))",
        },
    ]

    try:
        for i, step in enumerate(steps_for_verification, start=1):
            eval(step["action"])
            panel_group = Group(step["output"], ProgressBar(total=3, completed=3))
            print(Panel(panel_group))
            
        config.record = file_format(load(open(location)))
        
        return config.record

    # Possible exceptions
    except FileNotFoundError:
        print(Panel(Align("[#CC3636]No File Provided...", align="center")))
    except JSONDecodeError:
        print(
            Panel(Align("[#CC3636]JSON Decode Error, Please Check Your JSON File..."))
        )
    except UnicodeDecodeError:
        print(Panel(Align("[#CC3636]Error Parsing File...")))
    except ValueError:
        print(
            Panel(
                Align(
                    "[#CC3636]Format Error, Check Out The Documentation On How To Format Your JSON File...\nhttps://github.com/MZaFaRM/CLICKERY/blob/main/Guide/format.md"
                )
            )
        )


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
    return record
