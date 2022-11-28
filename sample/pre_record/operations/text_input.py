import tkinter
from sample.helpers.dir import InputDialogueBox

write_text = ""


def return_write():

    global write_text

    _write_window()
    
    _Return_Text = write_text
    write_text = ""
    
    return _Return_Text


def _write_save(window, _write_text):

    global write_text

    write_text = _write_text.get(1.0, "end-1c")

    window.quit()
    window.destroy()


def _write_window():
    
    tkwindow = InputDialogueBox()

    main_window = tkwindow.initialise_window(title="Input text")
    write_frame, frame = tkwindow.main_frame(main_window, heading="     INPUT TEXT TO WRITE")


    writetxt_label = tkinter.Label(write_frame, text="INPUT TEXT :- ")
    writetxt = tkinter.Text(write_frame, height=10, width=30)
    writetxt_label.grid(row=0, column=2, pady=10, padx=75)
    writetxt.grid(row=1, column=2, padx=75)
    writetxt.configure(background=tkwindow.ContentColor, foreground=tkwindow.TextColor)
    writetxt_label.configure(background=tkwindow.ContentColor, foreground=tkwindow.TextColor)

    # Button
    button = tkinter.Button(
        frame, text="CONTINUE", command=lambda: _write_save(main_window, writetxt)
    )
    
    tkwindow.configure_button(button)
    tkwindow.configure_window(main_window)
