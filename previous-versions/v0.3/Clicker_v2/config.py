from json import load as listify

# lists and dictionaries used
positions = []
current_position = {}
action = {}
keyboardinput = ""
actions_list = []

f = open("actions.json")
actions_list = listify(f)