from tkinter import filedialog
import tkinter
import tkinter.font as font
from os import getcwd
from ctypes import windll


def clarity():
    # Increases the clarity ktinkter dialogue boxes
    windll.shcore.SetProcessDpiAwareness(1)


def folder(extension, Title="Select file"):
    # Used by file input, image search to get the file name to import actions from
    location = filedialog.askopenfilename(
        # getcwd ensures the initial directory is the directory of the program
        initialdir=getcwd(),
        title=Title,
        filetypes=extension,
    )

    return location

class InputDialogueBox:

    ContentColor = "#2C3639"
    ButtonColor = "#3F4E4F"
    TextColor = "#F9F2ED"

    def initialise_window(self, title=""):

        window = tkinter.Tk()
        window.title(title)
        return window

    def main_frame(self, window, heading=""):

        frame = tkinter.Frame(window)
        frame.pack()
        frame.configure(background=self.ContentColor)

        sub_frame = tkinter.LabelFrame(frame, text=heading)
        sub_frame.grid(row=2, column=0, columnspan=3)

        # button and heading style
        headf = font.Font(size=20, weight="bold")

        sub_frame["font"] = headf

        for widget in sub_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        sub_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10, columnspan=3)
        sub_frame.configure(
            background=self.ContentColor,
            foreground="#FEDB39",
            highlightbackground="yellow",
            highlightcolor="red",
            borderwidth=0,
        )

        return sub_frame, frame

    def configure_button(self, button):

        # configures postion of button on grid
        button.grid(row=5, column=1, sticky="news", padx=20, pady=20)

        # configures color of button
        button.configure(
            background=self.ButtonColor,
            foreground=self.TextColor,
            activebackground=self.TextColor,
            activeforeground=self.ButtonColor,
            borderwidth=0,
        )

        buttonf = font.Font(weight="bold", size=10)

        # configures button font
        button["font"] = buttonf

    def configure_window(self, window):

        # lifts the window above all other windows once
        window.lift()
        window.attributes("-topmost", True)
        window.after_idle(window.attributes, "-topmost", False)

        # doesn't allow window resizing
        window.resizable(False, False)

        window.mainloop()

