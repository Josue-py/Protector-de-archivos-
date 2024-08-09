import tkinter as tk
from .frames import main_frame
from .options import windows_options


def create_main_window():
    window = tk.Tk()
    windows_options(window)
    main_frame(window)
    window.mainloop()