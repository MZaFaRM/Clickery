from tkinter import filedialog
from tkinter import *
from os import getcwd
from ctypes import windll


def clarity():
    # Increases the clarity ktinkter dialogue boxes
    windll.shcore.SetProcessDpiAwareness(1)


def folder(extension, Title="Select file"):

    location = filedialog.askopenfilename(
        initialdir=getcwd(), title=Title, filetypes=extension
    )

    return location
