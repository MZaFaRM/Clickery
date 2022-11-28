from keyboard import hook, unhook_all
import tkinter
from tkinter import font, messagebox

keys_clicked = []
keys_clicked_display = ""
tyr = 1


def display_hotkeys():
    global keys_clicked_display

    _keys_clicked_display = keys_clicked_display

    keys_clicked_display = ""

    return _keys_clicked_display


def quit():
    # quits if user manually decides to quit by reseting everything and unhooking keys

    global keys_clicked_display
    global keys_clicked
    global window

    unhook_all()

    keys_clicked = []
    keys_clicked_display = ""

    window.quit()
    window.destroy()


def _Inserted_hot_key_window():

    # window of 'key insert'
    global hot_keys
    global window

    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"
    window = tkinter.Tk()
    window.attributes("-topmost", True)

    # sets window title and attributes
    window.title("Insert Hotkey")
    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(background=ContentColor)
    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")

    # sets window heading and attributes
    loop_frame = tkinter.LabelFrame(frame, text="  ENTER HOTKEY")
    loop_frame.grid(row=2, column=0, columnspan=3, pady=30)
    loop_frame["font"] = headf
    for widget in loop_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    loop_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10, columnspan=3)
    loop_frame.configure(
        background=ContentColor,
        foreground="#FEDB39",
        highlightbackground="yellow",
        highlightcolor="red",
        borderwidth=0,
    )

    # label for text box
    hot_keys_label = tkinter.Label(loop_frame, text="ENTER KEYS :- ")
    hot_keys_label.configure(justify="center")
    hot_keys = tkinter.Entry(loop_frame)

    hot_keys_label.grid(row=1, column=2, pady=10, padx=75, columnspan=3)
    hot_keys.grid(row=2, column=2, padx=75)
    hot_keys.configure(background=ContentColor, foreground=TextColor)
    hot_keys_label.configure(background=ContentColor, foreground=TextColor)
    hot_keys.configure(
        justify="center",
        disabledforeground="white",
        disabledbackground=ContentColor,
        borderwidth=2,
    )

    # configures button
    button = tkinter.Button(
        frame, text="CONFIRM", command=lambda: _save_key_Input(window)
    )
    button.grid(row=5, column=1, sticky="news", padx=20, pady=20)
    button.configure(
        background=ButtonColor,
        foreground=TextColor,
        activebackground=TextColor,
        activeforeground=ButtonColor,
        borderwidth=0,
    )
    button["font"] = buttonf

    # Records all keyboard activities
    hook(_perses)

    # To bring the window to front
    # https://stackoverflow.com/a/36191443/19916937
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)

    # disables resizing
    window.resizable(False, False)

    # called when user closes window 'quit' function defined elsewhere
    window.protocol("WM_DELETE_WINDOW", quit)

    window.mainloop()


def _save_key_Input(screen):

    # Stops recording all keyboard activities
    unhook_all()
    
    screen.quit()
    screen.destroy()


def return_hot_key_input():

    # this function is called by main to get the hot_key_input
    global keys_clicked

    _Inserted_hot_key_window()

    _keys_clicked = keys_clicked.copy()

    keys_clicked = []

    if _keys_clicked:
        return _keys_clicked

    return 0


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
