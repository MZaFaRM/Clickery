import tkinter
from tkinter import messagebox
from tkinter import font

wait_final = "-"

def quit(window):
    
    global wait_final
    
    wait_final = "-"
    
    window.quit()
    window.destroy()

def return_wait():
    global wait_final
    _Wait_window()
    
    _wait_final = wait_final
    
    wait_final = "-"
    
    return _wait_final

def _wait_save(_wait_seconds, window):
    
    global wait_final

    wait_seconds = _wait_seconds.get()

    try:
        wait_seconds = int(wait_seconds)
    
        if wait_seconds < 0:
            raise ValueError
        
        wait_final = wait_seconds
        
        window.quit()
        window.destroy()
    
    except ValueError:
        messagebox.showwarning(
            title="Value Error", message="The time here is represented in seconds by positive integers"
        )


def _Wait_window():
    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"
    window = tkinter.Tk()
    window.title("Wait for time")
    frame = tkinter.Frame(window)
    frame.pack()
    frame.configure(background=ContentColor)
    buttonf = font.Font(weight="bold", size=10)
    headf = font.Font(size=20, weight="bold")
    loop_frame = tkinter.LabelFrame(frame, text="  WAIT IN SECONDS")
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

    Waits_label = tkinter.Label(loop_frame, text="INPUT SECONDS :- ")
    Waits_spinbox = tkinter.Spinbox(loop_frame, from_=0, to="infinity")
    Waits_label.grid(row=0, column=2, pady=10, padx=75)
    Waits_spinbox.grid(row=1, column=2, padx=75)
    Waits_spinbox.configure(background=ContentColor, foreground=TextColor)
    Waits_label.configure(background=ContentColor, foreground=TextColor)
    Waits_spinbox.configure(justify="center")

    # Button
    button = tkinter.Button(
        frame, text="CONTINUE", command=lambda: _wait_save(Waits_spinbox, window)
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
    window.attributes('-topmost',True)
    window.after_idle(window.attributes,'-topmost',False)
    window.resizable(False, False)
    
    window.protocol('WM_DELETE_WINDOW', lambda: quit(window))

    window.mainloop()