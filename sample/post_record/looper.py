import tkinter
from tkinter import messagebox
import tkinter.font as font
import sample.universal.config as config


loop_final = []


def LoopWindow():
    
    # loop action's window
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

    window.lift()
    window.attributes("-topmost", True)
    window.after_idle(window.attributes, "-topmost", False)
    window.resizable(False, False)

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

            # quits window if all goes well
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