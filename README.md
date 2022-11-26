# CLICKERY

This is an AUTOGUI software designed to make it easier to use AUTOGUI without coding.


## Getting started

execute the given command in the terminal

```py install.py```

which would install all the required libraries to run the project, then execute the given command in the terminal to start the program.

```py main.py```
#### Mode of Input

After which you will be provided with two choice for manual input and file input, if choosing file input please refer the ```format.txt``` to understand how to properly format your json file

 *Note: only json files are supported for file input*

 For manual input insert the required calls to record yout action, eg:
 
  ```"1"``` for move

   ```"0"``` for screenshot

   after recording insert ```esc``` to go to the next step

   #### Post Input
   After you have recorded the actions, it can be then further modified through *looping* or *replacing* before execution. If you have no modifications to make, start execution with ```space```.

   *Note: deeper details regarding each function and their usage is provided in the ```guide```*

## Developing

#### Built with
Python version - Python ```3.11.0```

Given below are all the libraries required to run the project

- keyboard ```0.13.5```
- Pillow ```9.3.0```
- PyAutoGUI ```0.9.53```
- rich ```12.6.0```
- tabulate ```0.9.0```
- opencv-python ```4.6.0.66```
- pyclean ```2.2.0```


## Configurations

Typing speed, Clicking speed, Dragging speed can be modified from the ```sample\universal\config.py```.
## Navigation

 Checkout ```\structure``` for help in navigating through the project directory.
 
 
 ![Directory Structure](https://raw.githubusercontent.com/MZaFaRM/CLICKERY/5b1a869ad83411e924052c6d1e7e95460556fb4b/structure/structure.dot.svg)
 
## Database

This project uses sqlite3 as the database to store all the successful executions from the last ```reset.py``` upto this point,

https://www.sqlite.org/download.html

schema of the database used in the project located at ```assets\database\history.db``` is
```
CREATE TABLE history (
    actions_id INTEGER NOT NULL,
    JSON TEXT NOT NULL,
    PRIMARY KEY (actions_id)
);
```
## License

#### [MIT License](https://github.com/MZaFaRM/CLICKERY/blob/main/LICENSE)
*Copyright (c) 2022 Muhammed Zafar M. M.*
## Documentation

[Guide](https://linktodocumentation)

[File Input formatting](guide.json)


## Additional Features

- The very last successful execution is saved at ```assets\json\history.json```.
- All successful actions from the last ```reset.py``` to the current date is saved in the database, refer [Database](https://github.com/MZaFaRM/CLICKERY/blob/main/README.md#database) section for details.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Feedback

If you have any feedback, please reach out to me at muhammedzafar.mm@gmail.com

