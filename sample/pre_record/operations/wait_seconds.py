import tkinter
from tkinter import messagebox
from sample.helpers.dir import InputDialogueBox

wait_final = "-"


def return_wait():
    # gets the global variable
    global wait_final
    # initiates the window
    _wait_window()
    # if clicked on save button creates a duplicate of it and clears it
    _wait_final = wait_final
    # cleared state
    wait_final = "-"

    return _wait_final


def _wait_save(_wait_seconds, window):

    # saves user input time
    global wait_final

    wait_seconds = _wait_seconds.get()

    try:
        wait_seconds = int(wait_seconds)

        if wait_seconds < 0:
            raise ValueError

        wait_final = wait_seconds

        window.quit()
        window.destroy()

    # exception handling
    except ValueError:
        messagebox.showwarning(
            title="Value Error",
            message="The time here is represented in seconds by positive integers",
        )


def _wait_window():

    # 'wait' window

    tkwindow = InputDialogueBox()

    main_window = tkwindow.initialise_window(title="Wait for time")
    wait_frame, frame = tkwindow.main_frame(main_window, heading=" WAIT IN SECONDS")

    Waits_label = tkinter.Label(wait_frame, text="INPUT SECONDS")
    Waits_spinbox = tkinter.Spinbox(wait_frame, from_=0, to="infinity")
    Waits_label.grid(row=0, column=2, pady=10, padx=75)
    Waits_spinbox.grid(row=1, column=2, padx=75)
    Waits_spinbox.configure(
        background=tkwindow.ContentColor, foreground=tkwindow.TextColor
    )
    Waits_label.configure(
        background=tkwindow.ContentColor, foreground=tkwindow.TextColor
    )
    Waits_spinbox.configure(justify="center")

    # Button
    button = tkinter.Button(
        frame, text="CONTINUE", command=lambda: _wait_save(Waits_spinbox, main_window)
    )

    tkwindow.configure_button(button)
    tkwindow.configure_window(main_window)
