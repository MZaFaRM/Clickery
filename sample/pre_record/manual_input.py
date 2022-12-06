from keyboard import read_key, send
from pyautogui import keyUp

import sample.universal.config as config
import sample.pre_record.operations.general as general
import keyboard


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
            
            keyUp(keyboardinput)

            # Checks user input and saves action
            for item in config.actions_list:
                if item["call"] == keyboardinput:

                    action = eval(f"general.{item['function']}")

                    if item["function"] != "Pop()":

                        if action:
                            config.record.append(action)

            # Stop recording
            if keyboardinput == "esc":
                break

        elif flag:
            flag = 0
