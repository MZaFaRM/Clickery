import tkinter
from tkinter import messagebox
from tkinter import font

write_text = ""
window = ""


def return_write():

    global write_text

    _write_window()
    _Return_Text = write_text
    write_text = ""
    return _Return_Text


def quit():
    global window

    global write_text
    write_text = ""

    window.quit()
    window.destroy()


def _write_save(_write_text):

    global window

    global write_text

    write_text = _write_text.get(1.0, "end-1c")

    window.quit()
    window.destroy()


def _write_window():

    global window

    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"
    window = tkinter.Tk()
    window.title("Input text")
    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(background=ContentColor)
    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")
    loop_frame = tkinter.LabelFrame(frame, text="     INPUT TEXT TO WRITE")
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

    writetxt_label = tkinter.Label(loop_frame, text="INPUT TEXT :- ")
    writetxt = tkinter.Text(loop_frame, height=10, width=30)
    writetxt_label.grid(row=0, column=2, pady=10, padx=75)
    writetxt.grid(row=1, column=2, padx=75)
    writetxt.configure(background=ContentColor, foreground=TextColor)
    writetxt_label.configure(background=ContentColor, foreground=TextColor)

    # Button
    button = tkinter.Button(
        frame, text="CONTINUE", command=lambda: _write_save(writetxt)
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

    # To bring the window to front
    # https://stackoverflow.com/a/36191443/19916937
    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)
    window.resizable(False, False)

    window.protocol("WM_DELETE_WINDOW", quit)

    window.mainloop()
