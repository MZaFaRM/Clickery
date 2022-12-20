# CLICKERLY

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![edX](https://img.shields.io/badge/edX-%2302262B.svg?style=for-the-badge&logo=edX&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


This is an AUTOGUI software designed to make it easier to use AUTOGUI without coding.


# Getting started

execute the given command in the terminal

```
py setup.py
```

which would install all the required libraries to run the project, then execute this command in the terminal to start the program.

```
py main.py
```

# Mode of Input

After running the program you will be asked to prompted to input the the mode of input 

## File Input

For file input your json file must be formatted in the said way for it to be read by the program, nonetheless it is not recommended to write this from scratch It is always better to first record your actions, through manual input and copy paste it from ```history.json``` or ```history.db``` later,  Irrespective of which you can manually write a file through these steps if you wish to do so.


#### General guidelines
Your file input must be a list of dictionaries, where each dictionary represents an action, each dictionary may or may not contain an ID with it.

#### Move Cursor
```{'move': {'x': 935, 'y': 697}}```

The key must be ```move``` and the ```x``` and ```y``` positions must be mentioned as shown in the example. The top-left corner of the screen being the ```(0,0)``` region, ```x``` increases going right and ```y``` increases going down.

#### Left Click Position
```{'l-click': 1}```

The key must be ```l-click``` but the value can be anything, since it is ignored by program.

#### Right Click Position
```{'r-click': 1}```

The key must be ```r-click``` but the value can be anything, since it is ignored by program.

#### Drag Cursor
```{'drag': {'x': 1031, 'y': 955}}```

The key must be ```drag``` and the ```x``` and ```y``` positions must be mentioned as shown in the example. The top-left corner of the screen being the ```(0,0)``` region, ```x``` increases going right and ```y``` increases going down.

#### Enter Text 
```{'write': 'Hello World'}```

The key must be ```write``` and the value must be the text you would like to write.

#### Wait For Image 
```{'image': 'C:/Users/images/image-to-search.png'}```

The key must be ```image``` and the value must be the address of the image you would like to search for / wait to appear / move to.

#### Insert Key 
```{'key': 'shift'}```

The key must be ```key``` and the value must be the key you want to insert in lowercase without whitespaces.

#### Wait Time
```{'sleep': 1}```

The key must be ```sleep``` and the value must be the time you would like to wait for in seconds.

#### Insert Hotkey
```{'hotkey': ['ctrl', 'C']}```

The key must be ```hotkey``` and the value must be the list of keys you would like to enter in lowercase.

#### Screenshot
```{'screenshot': 'C:/Users/images/Screenshot.png'}```

The key must be ```screenshot``` and the value must be the location of where you would like to save your screenshot.


### Example
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

*Note: only json files are supported for file input*

## Manual Input

If you choose to proceed with the ```manual input``` provide the required calls to invoke the function responsible to record your request.

#### Move Cursor

Hover over the location you want to move the cursor to and input ```1``` to record the action of moving the cursor to that location.

#### Left Click Position

Input ```2``` and the program would record that you want to click on the current location. It is best suited to use when it is paired to use with [Move Cursor](guide.md#move-cursor) or [Wait for Image](guide.md#wait-for-image).

#### Right Click Position

Input ```3``` and the program would record that you want to right click on the current location, useful to invoke pop ups. Similar to [Left Click Position](guide.md#left-click-position) is it best when paired with [Move Cursor](guide.md#move-cursor) or [Wait for Image](guide.md#wait-for-image).

 Drag Cursor

Hover over the location you want to drag the cursor to and input ```4``` to record the action of moving the cursor to that location. The cursor would click and hold it's current location and move to the drag location to finally release it.

Enter Text

Input ```5``` and enter the text you want to insert in the dailogue box that appears.

#### Wait For Image

Input ```6``` and select the location of the image you want to wait to appear on screen, this function contains a number of additional features that you might find helpful.

- It automatically moves the cursor to the center of the image if found on screen.
- As the name suggests it waits until the image appears on screen.
- Combining it with [Left Click Position](guide.md#left-click-position) / [Right Click Position](guide.md#right-click-position) may be a good idea.

#### Insert Key

Input ```7``` and enter the key you would like to insert from you keyboard, clicking on the submit button then would record your action of inserting that key.

For entering multiple keys together refer [Hotkeys Input](guide.md#insert-hotkey).

#### Wait Time

Input ```8``` and enter the number of seconds you would like to wait, for it to be recorded.

#### Delete Last Action / Delete Action

Input ```9``` and the last action you recorded would be removed while in Manual Input, although in [Replace Action](guide.md#replacing) section ie. after you have recorded all your actions, the element with the ID you input would be removed.

#### Insert Hotkey

Input ```0``` and enter all the keys you would like to input together **one by one** after which click on submit, useful for doing actions like ```ctrl+C``` , ```ctrl+w```.

#### Take a Screenshot

Input ```-``` and provide the location you would like to save your screenshot at.
  

# Post Recording actions

If you input ```esc``` all actions upto that point would be saved in [```history.json```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/json/history.json), it could be further modifed by

## Looping

Requested portions of the action's record can be repeated any number of times, after requesting for it in the dialogue box that appears after you input ```ctrl``` key.

## Replacing

An action can be replaced with another one if you enter the ID of the action to be replaced and the [call](guide.md#manual-input) of the action you would like to replace it with.

#### Tip:
Combining Replacing and Looping allows you to insert actions in your record.

# Finalization

After recording and modifying the actions it can be started by inserting ```space``` key.

#### Things to be noted

- A started excecution can be exited with ```ctrl+c``` ie. *Keyboard Interrupt*
- It can also be exited by moving the cursor to the corner of the screen.
- Other methods include the common methods to exit a program.

# Saving the input

Every successful execution from the last reset.py is saved in the [```assets/database/history.db```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/database/history.db) in table history, while the last recorded action is saved in the [```assets/json/history.json```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/json/history.json). 


# Modifying Input Speed

Clicking speed, Dragging speed, Typing speed can be modified through [```sample/universal/config.py```](https://github.com/MZaFaRM/CLICKERY/blob/main/sample/universal/config.py).

# Developing

#### Built with
Python version - Python [```3.11.0```](https://www.python.org/downloads/)

Given below are all the libraries required to run the project

- keyboard ```0.13.5```
- Pillow ```9.3.0```
- PyAutoGUI ```0.9.53```
- rich ```12.6.0```
- tabulate ```0.9.0```
- opencv-python ```4.6.0.66```
- pyclean ```2.2.0```

# File Reference

## setup.py

This python file helps in downloading ans installing all the required libraries to run the program successfully.

## reset.py

This python file helps in clearing the history, database, pycache files, converted images etc.

## requirements.txt

Used by `setup.py` to get the list of libraries

## main.py

The main program, execute it only after `setup.py` .

## sample

Containes all the sub program files

    ### helpers
        
        files that handles dialogue boxes, saving recorded input, clarity of dialogue boxes etc.
        
    ### post_record
    
        files that handles `loop` and `replace`
        
    ### pre_record
        
        files that helps in recording user requests
        
    ### universal
    
        constant data and configurations, possible user requests
        
    ### core.py
    
        the second main file helps in overall working of the program


# Configurations

Typing speed, Clicking speed, Dragging speed can be modified from [```sample\universal\config.py```](https://github.com/MZaFaRM/CLICKERY/blob/main/sample/universal/config.py).
 
# Database

This project uses ```sqlite3``` as the database to store all the successful executions starting from the last ```reset.py```,

schema of the database used in the project located at [```assets\database\history.db```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/database/history.db) is
```
CREATE TABLE history (
    actions_id INTEGER NOT NULL,
    JSON TEXT NOT NULL,
    PRIMARY KEY (actions_id)
);
```

[```sqlite3```](https://www.sqlite.org/index.html) can be downloaded from

https://www.sqlite.org/download.html

Although, downloading is not necessary for successful execution of the software, not doing so may make certain features inaccessible.


# Additional Features

- The very last successful execution is saved at [```assets\json\history.json```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/json/history.json).
- All successful actions starting from the last ```reset.py``` is saved in a database, refer [Database](README.md#database) section for details.


# Screenshots

<img width="960" alt="homescreen" src="https://user-images.githubusercontent.com/98420006/205716839-640ca13c-61e9-4c49-8995-d77bf1d2a77f.png">


<img width="960" alt="working" src="https://user-images.githubusercontent.com/98420006/205962224-f0971a03-3155-4465-b6cf-b67ffd6dd8c7.png">



# License

#### MIT License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/MZaFaRM/CLICKERY/blob/main/LICENSE)
*Copyright (c) 2022 Muhammed Zafar M. M.*

# Feedback

If you have any feedback, please reach out to me at muhammedzafar.mm@gmail.com

