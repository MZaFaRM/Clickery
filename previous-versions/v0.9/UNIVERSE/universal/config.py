from json import load as listify

# Change value to adjust cursor speed while moving [default 0.75]
Move_Speed = 0.75

# Change value to adjust cursor speed while draggging [default 0.75]
Drag_Speed = 0.75

# Change value to adjust typing speed [default 0.15]
Type_Speed = 0.15

# lists and dictionaries used
record = []
loop_final = {}
id = 1
replace_final = {}

# actions = ["move", "click", "drag", "write", "image", "sleep", "hotkey", "key", "screenshot"]

f = open(r"universal\actions.json")
actions_list = listify(f)
f.close()

f = open(r"universal\replace.json")
replace_list = listify(f)
f.close()
