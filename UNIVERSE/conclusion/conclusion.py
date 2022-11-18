import tkinter
from tkinter import messagebox
import tkinter.font as font
from helpers.menu import add_id, PrintRecorded
from keyboard import read_key
from tabulate import tabulate
import universal.config as config
from rich import print
from initialise.manual.operations import *

window = ""


def clear():
    global window
    config.loop_final = []
    window.quit()
    window.destroy()


def looper():
    LoopWindow()
    try:
        loops = loop_final["LoopCount"]
        start = loop_final["LoopStart"]
        end = loop_final["LoopEnd"]
        InsertAfter = loop_final["InsertAfter"]
    except KeyError:
        return

    # Gets the loop to multiply
    looper_list = config.record[start - 1 : end]

    # Multiplies the loop
    looper_list = looper_list * loops

    # Adds the elements back to list
    for action in reversed(looper_list):
        config.record.insert(InsertAfter, action)

    add_id()
    # Lists
    PrintRecorded()


loop_final = config.loop_final


def LoopWindow():

    global window

    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"

    window = tkinter.Tk()
    window.title("Insert loops")

    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(background=ContentColor)

    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")

    loop_frame = tkinter.LabelFrame(frame, text="LOOP MODIFICATIONS")
    loop_frame.grid(row=2, column=0, columnspan=3)
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

    NumberOfLoops_label = tkinter.Label(loop_frame, text="NUMBER OF LOOPS")
    NumberOfLoops_spinbox = tkinter.Spinbox(loop_frame, from_=0, to="infinity")
    NumberOfLoops_label.grid(row=0, column=0)
    NumberOfLoops_spinbox.grid(row=0, column=1)
    NumberOfLoops_spinbox.configure(background=ContentColor, foreground=TextColor)
    NumberOfLoops_label.configure(background=ContentColor, foreground=TextColor)
    NumberOfLoops_spinbox.configure(justify="center")

    LoopStart_label = tkinter.Label(loop_frame, text="LOOP STARTS FROM")
    LoopStart_spinbox = tkinter.Spinbox(loop_frame, from_=1, to=len(config.record))
    LoopStart_label.grid(row=1, column=0)
    LoopStart_spinbox.grid(row=1, column=1)
    LoopStart_spinbox.configure(background=ContentColor, foreground=TextColor)
    LoopStart_label.configure(background=ContentColor, foreground=TextColor)
    LoopStart_spinbox.configure(justify="center")

    LoopEnd_label = tkinter.Label(loop_frame, text="LOOP ENDS AT")
    LoopEnd_spinbox = tkinter.Spinbox(loop_frame, from_=0, to=len(config.record))
    LoopEnd_label.grid(row=2, column=0)
    LoopEnd_spinbox.grid(row=2, column=1)
    LoopEnd_spinbox.configure(background=ContentColor, foreground=TextColor)
    LoopEnd_label.configure(background=ContentColor, foreground=TextColor)
    LoopEnd_spinbox.configure(justify="center")

    InsertAfter_label = tkinter.Label(loop_frame, text="INSERT LOOP AFTER")
    InsertAfter_spinbox = tkinter.Spinbox(loop_frame, from_=0, to=len(config.record))
    InsertAfter_label.grid(row=3, column=0)
    InsertAfter_spinbox.grid(row=3, column=1)
    InsertAfter_spinbox.configure(background=ContentColor, foreground=TextColor)
    InsertAfter_label.configure(background=ContentColor, foreground=TextColor)
    InsertAfter_spinbox.configure(justify="center")

    for widget in loop_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Button
    parameters = [
        NumberOfLoops_spinbox,
        LoopStart_spinbox,
        LoopEnd_spinbox,
        InsertAfter_spinbox,
    ]
    button = tkinter.Button(
        frame, text="CREATE LOOP", command=lambda: LoopSave(parameters, window)
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

    window.protocol("WM_DELETE_WINDOW", clear)
    window.mainloop()


def LoopSave(parameters, window):

    global loop_final

    NumberOfLoops = parameters[0]
    LoopStart = parameters[1]
    LoopEnd = parameters[2]
    InsertAfter = parameters[3]

    LoopCount = NumberOfLoops.get()
    LoopStart = LoopStart.get()
    LoopEnd = LoopEnd.get()
    InsertAfter = InsertAfter.get()

    if LoopCount and LoopStart and LoopEnd:
        try:
            LoopCount = int(LoopCount)
            LoopStart = int(LoopStart)
            LoopEnd = int(LoopEnd)
            InsertAfter = int(InsertAfter)
            if LoopStart > LoopEnd:
                raise RuntimeError
            loop_final = {
                "LoopCount": LoopCount,
                "LoopStart": LoopStart,
                "LoopEnd": LoopEnd,
                "InsertAfter": InsertAfter,
            }
            if LoopStart <= 0:
                raise OSError
            if (
                LoopEnd > len(config.record)
                or LoopStart > len(config.record)
                or InsertAfter > len(config.record)
            ):
                raise AttributeError
            if InsertAfter < 0:
                raise IndentationError
            config.loop_final = loop_final
            window.quit()
            window.destroy()
        except IndentationError:
            messagebox.showwarning(
                title="Value Error", message="Insert loop after value must be atleast 0"
            )
        except ValueError:
            messagebox.showwarning(
                title="Value Error", message="All inputs must be integers."
            )
        except RuntimeError:
            messagebox.showwarning(
                title="value Error",
                message="Loop's starting point must be before Loop's ending point",
            )
        except OSError:
            messagebox.showwarning(
                title="Value Error", message="Loop's starting point must be atleast 1"
            )
        except AttributeError:
            messagebox.showwarning(
                title="Value Error",
                message="Loop must start and end between the length of action",
            )
    else:
        messagebox.showwarning(title="Input Error", message="All inputs are required.")


def ReplaceSave(ReplaceID, window):

    ReplaceID = ReplaceID.get()

    if ReplaceID:
        try:
            ReplaceID = int(ReplaceID)

            Replace_final = {"ReplaceID": ReplaceID}

            if ReplaceID > len(config.record):
                raise AttributeError
            if ReplaceID < 1:
                raise IndentationError
            config.replace_final = Replace_final
            window.quit()
            window.destroy()
        except IndentationError:
            messagebox.showwarning(
                title="Value Error", message="Inserted ID must be atleast 1"
            )
        except AttributeError:
            messagebox.showwarning(
                title="Value Error", message="Inserted ID must be part of actions list"
            )
        except ValueError:
            messagebox.showwarning(
                title="Value Error", message="All inputs must be integers."
            )
    else:
        messagebox.showwarning(title="Input Error", message="All inputs are required.")


def replace_window():
    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"
    window = tkinter.Tk()
    window.title("Replace Action")
    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(background=ContentColor)
    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")
    loop_frame = tkinter.LabelFrame(frame, text="REPLACE ACTION")
    loop_frame.grid(row=2, column=0, columnspan=3)
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

    ReplaceID_label = tkinter.Label(loop_frame, text="INPUT ID :- ")
    ReplaceID_spinbox = tkinter.Spinbox(loop_frame, from_=1, to="infinity")
    ReplaceID_label.grid(row=0, column=2, pady=10, padx=75)
    ReplaceID_spinbox.grid(row=1, column=2, padx=75)
    ReplaceID_spinbox.configure(background=ContentColor, foreground=TextColor)
    ReplaceID_label.configure(background=ContentColor, foreground=TextColor)
    ReplaceID_spinbox.configure(justify="center")

    # Button
    button = tkinter.Button(
        frame, text="REPLACE", command=lambda: ReplaceSave(ReplaceID_spinbox, window)
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

    window.mainloop()


def print_menu_replace():
    # Menu for manual input
    menu_items = []
    single_item = {}
    for item in config.replace_list:
        single_item["ID"] = item["id"]
        single_item["DESCRIPTION"] = item["description"]
        single_item["CALL"] = '"' + item["call"] + '"'
        menu_items.append(single_item)
        single_item = {}

    print(tabulate(menu_items, "keys", "rounded_grid"), end="\n\n")


def replacer():
    replace_window()
    try:
        ReplaceID = config.replace_final["ReplaceID"]
    except KeyError:
        return

    # Stores keyboard input
    print_menu_replace()
    config.keyboardinput = read_key()

    # Stop recording
    if config.keyboardinput == "esc":
        pass


    # Checks user input and saves action
    for item in config.replace_list:

        Hephaestus = False
        Hades = True

        if item["call"] == config.keyboardinput:

            Hades = False

            print(f"{ReplaceID}   :point_right:  ", end="")
            action = eval(item["function"])

            for i, element in enumerate(config.record):
                if element["id"] == ReplaceID:
                    Hephaestus = True
                    config.record[i] = action
                    break

        if Hephaestus:
            break
    if Hades:
        print(":Cross_Mark: [#DC3535] Invalid Input")

    add_id()
    # Lists
    PrintRecorded()