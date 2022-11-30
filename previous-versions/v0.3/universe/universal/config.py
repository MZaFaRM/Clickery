from json import load as listify

# lists and dictionaries used
record = []
keyboardinput = ""
loop_final = {}
id = 1
replace_final = {}

# actions = ["move", "click", "drag", "write", "image", "sleep", "hotkey", "key", "screenshot"]

f = open(r"universal\actions.json")
actions_list = listify(f)
replace_list = actions_list.copy()
replace_list.pop(6)
