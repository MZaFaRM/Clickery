from keyboard import hook, unhook_all
import tkinter
from sample.helpers.dir import InputDialogueBox

keys_clicked = []
keys_clicked_display = ""
tyr = 1


def _Inserted_hot_key_window():
    
    global hot_keys
    
    tkwindow = InputDialogueBox()

    main_window = tkwindow.initialise_window(title="Insert Hotkey")
    hotkey_frame, frame = tkwindow.main_frame(main_window, heading="  ENTER HOTKEY")

    # label for text box
    hot_keys_label = tkinter.Label(hotkey_frame, text="ENTER KEYS :- ")
    hot_keys_label.configure(justify="center")
    hot_keys = tkinter.Entry(hotkey_frame)

    hot_keys_label.grid(row=1, column=2, pady=10, padx=75, columnspan=3)
    hot_keys.grid(row=2, column=2, padx=75)
    hot_keys.configure(background=tkwindow.ContentColor, foreground=tkwindow.TextColor)
    hot_keys_label.configure(background=tkwindow.ContentColor, foreground=tkwindow.TextColor)
    hot_keys.configure(
        justify="center",
        disabledforeground="white",
        disabledbackground=tkwindow.ContentColor,
        borderwidth=2,
    )

    # configures button
    button = tkinter.Button(
        frame, text="CONFIRM", command=lambda: _save_key_Input(main_window)
    )
    
    tkwindow.configure_button(button)

    # Records all keyboard activities
    hook(_perses)
    
    tkwindow.configure_window(main_window)


def _save_key_Input(screen):
    
    global returning_hotkeys
    global  keys_clicked_display
    
    returning_hotkeys = keys_clicked_display
    
    screen.quit()
    screen.destroy()


def return_hot_key_input():

    # this function is called by main to get the hot_key_input
    global keys_clicked
    global keys_clicked_display
    global returning_hotkeys
    
    returning_hotkeys = ""

    _Inserted_hot_key_window()
    
    unhook_all()

    _keys_clicked = keys_clicked.copy()
    keys_clicked = []
    
    keys_clicked_display = ""
    
    if returning_hotkeys:
    
        _returning_hotkeys = returning_hotkeys
        returning_hotkeys = ""
        
        return _keys_clicked, _returning_hotkeys

    return 0, 0


def _perses(input):

    global keys_clicked
    global tyr
    global keys_clicked_display

    if tyr:
        tyr = 0

        # saves current key to a list
        current_key = input

        hot_keys.config(state="normal")
        current_key = str(current_key)
        key_input = ""

        for cr in current_key:
            key_input += cr
            if key_input == "KeyboardEvent(":
                key_input = ""
            if cr == " ":
                key_input = key_input.rstrip()
                if not keys_clicked_display:
                    if len(key_input) == 1:
                        keys_clicked_display += str(key_input)
                    else:
                        keys_clicked_display += str(key_input).upper()
                    break

                if len(key_input) == 1:
                    keys_clicked_display += " + " + str(key_input)
                else:
                    keys_clicked_display += " + " + str(key_input).upper()
                break

        keys_clicked.append(key_input)
        hot_keys.delete(0, "end")
        hot_keys.insert(0, keys_clicked_display)
        hot_keys.config(state="disabled")

    else:
        tyr = 1
