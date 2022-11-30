from keyboard import hook, unhook_all
import tkinter
from tkinter import font

key_clicked = ""
phanes = True
tyr = 1

def _Inserted_Key_window():

    global InsertedKey

    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"
    window = tkinter.Tk()
    window.attributes("-topmost", True)
    window.title("INSERT KEY")
    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(background=ContentColor)
    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")
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

    # Button
    button = tkinter.Button(frame, text="CONFIRM", command=lambda: _save_key_Input(window))
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
    window.attributes('-topmost',True)
    window.after_idle(window.attributes,'-topmost',False)
    
    window.mainloop()


def _save_key_Input(screen):
    
    global key_clicked

    key_clicked = InsertedKey.get()
    # Stops recording all keyboard activities
    unhook_all()
    screen.quit()
    screen.destroy()
    
def return_key_input():
    _Inserted_Key_window()
    return key_clicked

def _perses(input):

    global key_clicked
    global tyr

    if tyr:
        tyr = 0

        key_clicked = input

        InsertedKey.config(state="normal")
        InsertedKey.delete(0, "end")
        key_clicked = str(key_clicked)
        key_input = ""

        for cr in key_clicked:
            key_input += cr
            if key_input == "KeyboardEvent(":
                key_input = ""
            if cr == " ":
                if len(key_input) == 2:
                    key_clicked = key_input
                else:
                    key_clicked = key_input.upper()
                break

        InsertedKey.insert(0, key_clicked)
        InsertedKey.config(state="disabled")

        global phanes
        phanes = False

    else:
        tyr = 1