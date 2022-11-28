from tkinter import filedialog
from tkinter import *
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
