import sample.universal.config as config
from tkinter import messagebox, font
import tkinter


replace_id = 0


def ReplaceSave(ReplaceID, window):
    # saves replace_id to global variable

    # gets the global variable
    global replace_id

    # gets input from the spinbox
    ReplaceID = ReplaceID.get()

    # if replaceID not equal to 0, since index starts at 1, and 0 means no input
    if ReplaceID:
        try:
            # tries to convert to int
            ReplaceID = int(ReplaceID)
            # checks if inserted value is a possible id for an element
            if ReplaceID > len(config.record):
                raise AttributeError
            if ReplaceID < 1:
                raise IndentationError
            # if all true assigns it to global variable
            replace_id = ReplaceID

            # quits window
            window.quit()
            window.destroy()

        except IndentationError:
            messagebox.showwarning(
                # if less that 1
                title="Value Error",
                message="Inserted ID must be atleast 1",
            )
        except AttributeError:
            messagebox.showwarning(
                # if not a possible id
                title="Value Error",
                message="Inserted ID must be part of actions list",
            )
        except ValueError:
            messagebox.showwarning(
                # if all not int
                title="Value Error",
                message="All inputs must be integers.",
            )
    else:
        # if submitted without entering anything
        messagebox.showwarning(title="Input Error", message="All inputs are required.")
    # return 1 if all goes well
    return 1


def replace_window():

    global window
    # sets the colours for the windwo
    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"

    # initiates the window
    window = tkinter.Tk()
    # window title, frame configurations
    window.title("Replace Action")
    frame = tkinter.Frame(window)
    frame.pack()

    # window color
    frame.configure(background=ContentColor)

    # button and heading style
    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")

    # heading position and configurations
    loop_frame = tkinter.LabelFrame(frame, text="REPLACE ACTION")
    loop_frame.grid(row=2, column=0, columnspan=3)
    loop_frame["font"] = headf

    # Configures all child elements
    for widget in loop_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # configures main frame position and color
    loop_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10, columnspan=3)
    loop_frame.configure(
        background=ContentColor,
        foreground="#FEDB39",
        highlightbackground="yellow",
        highlightcolor="red",
        borderwidth=0,
    )

    # sub-heading name and configurations
    ReplaceID_label = tkinter.Label(loop_frame, text="INPUT ID :- ")
    ReplaceID_spinbox = tkinter.Spinbox(loop_frame, from_=1, to="infinity")

    # input box position in grid
    ReplaceID_label.grid(row=0, column=2, pady=10, padx=75)
    ReplaceID_spinbox.grid(row=1, column=2, padx=75)

    # input box color and input position
    ReplaceID_spinbox.configure(background=ContentColor, foreground=TextColor)
    ReplaceID_label.configure(background=ContentColor, foreground=TextColor)
    ReplaceID_spinbox.configure(justify="center")

    # Button calls 'ReplaceSave on click
    button = tkinter.Button(
        frame, text="REPLACE", command=lambda: ReplaceSave(ReplaceID_spinbox, window)
    )

    # configures postion of button on grid
    button.grid(row=5, column=1, sticky="news", padx=20, pady=20)

    # configures color of button
    button.configure(
        background=ButtonColor,
        foreground=TextColor,
        activebackground=TextColor,
        activeforeground=ButtonColor,
        borderwidth=0,
    )

    # configures button font
    button["font"] = buttonf

    # lifts the window above all other windows once
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)

    # doesn't allow window resizing
    window.resizable(False, False)

    window.mainloop()
