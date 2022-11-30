from keyboard import hook, unhook_all
from tkinter import font
import tkinter


key_clicked = ""
tyr = 1
window = ""


def quit():
    # quits if user manually decides to quit by reseting everything and unhooking keys
    global window
    global key_clicked

    unhook_all()
    
    window.destroy()
    key_clicked = ""


def _save_key_Input():
    # saves key input
    global key_clicked
    global window

    # Stops recording all keyboard activities
    unhook_all()

    window.destroy()


def return_key_input():
    # this function is called by main to get the key_input
    global key_clicked

    _Inserted_Key_window()
    _key_clicked = key_clicked
    key_clicked = ""

    return _key_clicked


def _perses(input):
    # input is given by the hook function
    global key_clicked
    global tyr

    if tyr:
        tyr = 0
        # filters 'key up' and 'key down'

        key_clicked = input

        # formats the 'input' to onlly have the key name
        InsertedKey.config(state="normal")
        InsertedKey.delete(0, "end")
        key_clicked = str(key_clicked)

        key_input = ""

        for cr in key_clicked:

            key_input += cr

            if key_input == "KeyboardEvent(":
                key_input = ""
            if cr == " ":
                key_input = key_input.rstrip()
                key_clicked = key_input
                break

        if len(key_input) == 2:
            InsertedKey.insert(0, key_input)
        else:
            key_input = key_input.upper()
            InsertedKey.insert(0, key_input)

        InsertedKey.config(state="disabled")

    else:
        tyr = 1


def _Inserted_Key_window():

    # window of 'key insert'

    global InsertedKey
    global window
    # sets colors for the window
    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"

    # initiates window
    window = tkinter.Tk()
    window.attributes("-topmost", True)

    # sets window title and attributes
    window.title("Insert key")
    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(background=ContentColor)
    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")

    # sets window heading and attributes
    loop_frame = tkinter.LabelFrame(frame, text="      ENTER KEY")
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
    InsertedKey_label = tkinter.Label(loop_frame, text="INSERT KEY :- ")
    InsertedKey_label.configure(justify="center")
    InsertedKey = tkinter.Entry(loop_frame)

    InsertedKey_label.grid(row=1, column=2, pady=10, padx=75, columnspan=3)
    InsertedKey.grid(row=2, column=2, padx=75)
    InsertedKey.configure(background=ContentColor, foreground=TextColor)
    InsertedKey_label.configure(background=ContentColor, foreground=TextColor)
    InsertedKey.configure(
        justify="center",
        disabledforeground="white",
        disabledbackground=ContentColor,
        borderwidth=2,
    )

    # configures button
    button = tkinter.Button(frame, text="CONFIRM", command=_save_key_Input)
    button.grid(row=5, column=1, sticky="news", padx=20, pady=20)
    button.configure(
        background=ButtonColor,
        foreground=TextColor,
        activebackground=TextColor,
        activeforeground=ButtonColor,
        borderwidth=0,
    )
    button["font"] = buttonf

    # Records all keyboard activites
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
