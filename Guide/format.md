
# Formatting File Input

This is a guide on how to properly format your file for file input.


## A Reminder

It is always better to first record your actions, through manual input and save it in a different file for later use. Irrespective of which you can manually write a file through these steps if you wish to do so.
## General guidelines
Your file input must be a list of dictionaries, where each dictionary represents an action, each dictionary may or may not contain an ID with it.

* #### Move Cursor
```{'move': {'x': 935, 'y': 697}}```

The key must be ```move``` and the ```x``` and ```y``` positions must be mentioned as shown in the example. The top-left corner of the screen being the ```(0,0)``` region, ```x``` increases going right and ```y``` increases going down.

* #### Left Click Position
`
The key must be ```l-click``` but the value can be anything, since it is ignored by program.

* #### Right Click Position
```{'r-click': 1}```

The key must be ```r-click``` but the value can be anything, since it is ignored by program.

* #### Drag Cursor
```{'drag': {'x': 1031, 'y': 955}}```

The key must be ```drag``` and the ```x``` and ```y``` positions must be mentioned as shown in the example. The top-left corner of the screen being the ```(0,0)``` region, ```x``` increases going right and ```y``` increases going down.


* #### Enter Text 
```{'write': 'Hello World'}```

The key must be ```write``` and the value must be the text you would like to write.

* #### Wait For Image 
```{'image': 'C:/Users/images/image-to-search.png'}```

The key must be ```image``` and the value must be the address of the image you would like to search for / wait to appear / move to.

* #### Insert Key 
```{'key': 'shift'}```

The key must be ```key``` and the value must be the key you want to insert in lowercase without whitespaces.

* #### Wait Time
```{'sleep': 1}```

The key must be ```sleep``` and the value must be the time you would like to wait for in seconds.

* #### Insert Hotkey
```{'hotkey': ['ctrl', 'C']}```

The key must be ```hotkey``` and the value must be the list of keys you would like to enter in lowercase.

* #### Screenshot
```{'screenshot': 'C:/Users/images/Screenshot.png'}```

The key must be ```screenshot``` and the value must be the location of where you would like to save your screenshot.


## Example
```
[
    {'move': {'x': 1008, 'y': 863}, 'id': 1},
    {'l-click': 1, 'id': 2},
    {'r-click': 1, 'id': 3},
    {'drag': {'x': 1007, 'y': 864}, 'id': 4},
    {'write': 'He110 W0r1D', 'id': 5},
    {'image': 'C:/Users/images/image-to-search.png', 'id': 6},
    {'key': 'shift', 'id': 7},
    {'sleep': 3, 'id': 8},
    {'hotkey': ['ctrl', 'x'], 'id': 9},
    {'screenshot': ''C:/Users/images/Screenshot.png'', 'id': 10}
]
```

