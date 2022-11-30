import sample.universal.config as config
from tkinter import messagebox
import tkinter
from sample.helpers.dir import InputDialogueBox


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

    tkwindow = InputDialogueBox()

    main_window = tkwindow.initialise_window(title="Replace Action")
    loop_frame, frame = tkwindow.main_frame(main_window, heading="REPLACE ACTION")

    # sub-heading name and configurations
    ReplaceID_label = tkinter.Label(loop_frame, text="INPUT ID :- ")
    ReplaceID_spinbox = tkinter.Spinbox(loop_frame, from_=1, to="infinity")

    # input box position in grid
    ReplaceID_label.grid(row=0, column=2, pady=10, padx=75)
    ReplaceID_spinbox.grid(row=1, column=2, padx=75)

    # input box color and input position
    ReplaceID_spinbox.configure(
        background=tkwindow.ContentColor, foreground=tkwindow.TextColor
    )
    ReplaceID_label.configure(
        background=tkwindow.ContentColor, foreground=tkwindow.TextColor
    )
    ReplaceID_spinbox.configure(justify="center") 

    # Button calls 'ReplaceSave on click
    button = tkinter.Button(
        frame,
        text="REPLACE",
        command=lambda: ReplaceSave(ReplaceID_spinbox, main_window),
    )

    tkwindow.configure_button(button)

    tkwindow.configure_window(main_window)
