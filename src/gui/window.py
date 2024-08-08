import tkinter as tk
from .componets import create_header, create_button
from utils.file_operations import select_file


def create_main_window():
    window = tk.Tk(className=' SecurityFILE')
    window.geometry('1000x600')

    create_header(window)
    create_button(window, select_file)

    window.mainloop()