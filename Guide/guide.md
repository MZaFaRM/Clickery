
# Guide

## Getting started

execute the given command in the terminal

```
py setup.py
```

which would install all the required libraries to run the project, then execute this command in the terminal to start the program.

```
py main.py
```

## Mode of Input

After running the program you will be asked to prompted to input the the mode of input 

### File Input

if you choose to proceed with ```file input``` please refer the [```format.md```](https://github.com/MZaFaRM/CLICKERY/blob/main/Guide/format.md) to understand how to properly format your JSON file and jump to the [Post Recording Actions](guide.md#post-recording-actions) section.

*Note: only json files are supported for file input*

<details>
<summary>

### Manual Input

If you choose to proceed with the ```manual input``` provide the required calls to invoke the function responsible to record your request.
  </summary>

- #### Move Cursor

Hover over the location you want to move the cursor to and input ```1``` to record the action of moving the cursor to that location.

- #### Left Click Position

Input ```2``` and the program would record that you want to click on the current location. It is best suited to use when it is paired to use with [Move Cursor](guide.md#move-cursor) or [Wait for Image](guide.md#wait-for-image).

- #### Right Click Position

Input ```3``` and the program would record that you want to right click on the current location, useful to invoke pop ups. Similar to [Left Click Position](guide.md#left-click-position) is it best when paired with [Move Cursor](guide.md#move-cursor) or [Wait for Image](guide.md#wait-for-image).

- #### Drag Cursor

Hover over the location you want to drag the cursor to and input ```4``` to record the action of moving the cursor to that location. The cursor would click and hold it's current location and move to the drag location to finally release it.

- #### Enter Text

Input ```5``` and enter the text you want to insert in the dailogue box that appears.

- #### Wait For Image

Input ```6``` and select the location of the image you want to wait to appear on screen, this function contains a number of additional features that you might find helpful.

- It automatically moves the cursor to the center of the image if found on screen.
- As the name suggests it waits until the image appears on screen.
- Combining it with [Left Click Position](guide.md#left-click-position) / [Right Click Position](guide.md#right-click-position) may be a good idea.

- #### Insert Key

Input ```7``` and enter the key you would like to insert from you keyboard, clicking on the submit button then would record your action of inserting that key.

For entering multiple keys together refer [Hotkeys Input](guide.md#insert-hotkey).

- #### Wait Time

Input ```8``` and enter the number of seconds you would like to wait, for it to be recorded.

- #### Delete Last Action / Delete Action

Input ```9``` and the last action you recorded would be removed while in Manual Input, although in [Replace Action](guide.md#replacing) section ie. after you have recorded all your actions, the element with the ID you input would be removed.

- #### Insert Hotkey

Input ```0``` and enter all the keys you would like to input together **one by one** after which click on submit, useful for doing actions like ```ctrl+C``` , ```ctrl+w```.

- #### Take a Screenshot

Input ```-``` and provide the location you would like to save your screenshot at.
  
 </details>

## Post Recording actions

If you input ```esc``` all actions upto that point would be saved in [```history.json```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/json/history.json), it could be further modifed by

### Looping

Requested portions of the action's record can be repeated any number of times, after requesting for it in the dialogue box that appears after you input ```ctrl``` key.

### Replacing

An action can be replaced with another one if you enter the ID of the action to be replaced and the [call](guide.md#manual-input) of the action you would like to replace it with.

#### Tip:
Combining Replacing and Looping allows you to insert actions in your record.

## Finalization

After recording and modifying the actions it can be started by inserting ```space``` key.

#### Things to be noted

- A started excecution can be exited with ```ctrl+c``` ie. *Keyboard Interrupt*
- It can also be exited by moving the cursor to the corner of the screen.
- Other methods include the common methods to exit a program.

## Saving the input

Every successful execution from the last reset.py is saved in the [```assets/database/history.db```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/database/history.db) in table history, while the last recorded action is saved in the [```assets/json/history.json```](https://github.com/MZaFaRM/CLICKERY/blob/main/assets/json/history.json). 


## Modifying Input Speed

Clicking speed, Dragging speed, Typing speed can be modified through [```sample/universal/config.py```](https://github.com/MZaFaRM/CLICKERY/blob/main/sample/universal/config.py).
