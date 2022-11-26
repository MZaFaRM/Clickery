import sample.universal.config as config
from tkinter import messagebox, font
import tkinter

replace_id = 0


def ReplaceSave(ReplaceID, window):

    global replace_id

    ReplaceID = ReplaceID.get()

    if ReplaceID:
        try:
            ReplaceID = int(ReplaceID)

            if ReplaceID > len(config.record):
                raise AttributeError
            if ReplaceID < 1:
                raise IndentationError

            replace_id = ReplaceID

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

    return 1


def replace_window():

    global window

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

    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)
    window.resizable(False, False)

    window.mainloop()
