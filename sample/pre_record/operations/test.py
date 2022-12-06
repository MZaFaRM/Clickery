from json import load, dumps

f = open(r"C:\Users\thinkpad\Desktop\Clickery-main\sample\universal\actions.json")

lists = load(f)

id = 1

new_list = []
new_dict = {}

for item in lists:
    item["id"] = id
    item["call"] = str(id)
    id += 1
    
    new_dict = item
    new_list.append(new_dict)
    new_dict = {}
    
f.close()
f = open(r"C:\Users\thinkpad\Desktop\Clickery-main\sample\universal\actions.json", "w")

new_list = dumps(new_list, indent=4)

f.write(new_list)