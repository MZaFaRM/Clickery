![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![edX](https://img.shields.io/badge/edX-%2302262B.svg?style=for-the-badge&logo=edX&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

# CLICKERY

This is an AUTOGUI software designed to make it easier to use AUTOGUI without coding.


## Getting started

execute the given command in the terminal

```py install.py```

which would install all the required libraries to run the project, then execute this command in the terminal to start the program.

```py main.py```
#### Mode of Input

After which you will be provided with two choice for manual input and file input, if choosing file input please refer the [```Guide\format```](https://github.com/MZaFaRM/CLICKERY/blob/main/Guide/format) to understand how to properly format your json file.

 *Note: only json files are supported for file input*

 For manual input insert the required calls to record your action, eg:
 
  ```"1"``` for move

   ```"0"``` for screenshot

   After recording insert ```esc``` to go to the next step.

   #### Post Input
   After you have recorded the actions, it can be then further modified through *looping* or *replacing* before execution. If you have no modifications to make, start execution with ```space```.

   *Note: deeper details regarding each function and their usage is provided in the* [```guide```](https://github.com/MZaFaRM/CLICKERY/blob/main/Guide/guide)

## Developing

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


## Configurations

Typing speed, Clicking speed, Dragging speed can be modified from the [```sample\universal\config.py```](https://github.com/MZaFaRM/CLICKERY/blob/main/sample/universal/config.py).
## Navigation

 Checkout [```\structure```](https://github.com/MZaFaRM/CLICKERY/tree/main/structure) for help in navigating through the project directory.
 
 
 ![Directory Structure](https://raw.githubusercontent.com/MZaFaRM/CLICKERY/5b1a869ad83411e924052c6d1e7e95460556fb4b/structure/structure.dot.svg)
 
## Database

This project uses sqlite3 as the database to store all the successful executions from the last ```reset.py``` upto this point,

schema of the database used in the project located at [```assets\database\history.db```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/database/history.db) is
```
CREATE TABLE history (
    actions_id INTEGER NOT NULL,
    JSON TEXT NOT NULL,
    PRIMARY KEY (actions_id)
);
```

sqlite3 can be downloaded from

https://www.sqlite.org/download.html

Although, downloading is not necessary for successful execution of the software, not doing so may make certain features may be inaccessible.


## Additional Features

- The very last successful execution is saved at [```assets\json\history.json```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/json/history.json).
- All successful actions from the last ```reset.py``` to the current date is saved in a database, refer [Database](https://github.com/MZaFaRM/CLICKERY/blob/main/README.md#database) section for details.


## Screenshots

<img width="960" alt="Clickery_2" src="https://user-images.githubusercontent.com/98420006/204109098-2293428f-6807-495e-aeec-723ad2aac875.png">

<img width="960" alt="Clickery" src="https://user-images.githubusercontent.com/98420006/204109092-a2f0f8bf-0a0a-4f59-a683-99f43ac544d7.png">


## Documentation

[Guide](https://github.com/MZaFaRM/CLICKERY/blob/main/Guide/guide)

[Format](https://github.com/MZaFaRM/CLICKERY/blob/main/Guide/format)

## License

#### MIT License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/MZaFaRM/CLICKERY/blob/main/LICENSE)
*Copyright (c) 2022 Muhammed Zafar M. M.*

## Feedback

If you have any feedback, please reach out to me at muhammedzafar.mm@gmail.com

