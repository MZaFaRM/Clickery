from keyboard import read_key

import sample.universal.config as config
from sample.pre_record.operations.general import *


def manual_input():
    
    # Used since a key press is being recorded twice (key down, key up)
    flag = 0

    # repeats until esc
    while True:

        # Stores keyboard input
        keyboardinput = read_key()

        # Filters duplicate key input
        if not flag:

            flag = 1

            # Checks user input and saves action
            for item in config.actions_list:
                if item["call"] == keyboardinput:

                    action = eval(item["function"])

                    if item["function"] != "Pop()":

                        if action:
                            config.record.append(action)

            # Stop recording
            if keyboardinput == "esc":
                break

        elif flag:
            flag = 0
