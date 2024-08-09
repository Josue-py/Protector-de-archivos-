import tkinter as tk
from utils.config import COLOR_FONDO
from .componets import create_header, create_button, create_logo
from utils.operations import select_file, open_image


def main_frame(window):
    frame_parent = tk.Frame(window)
    frame_parent.config(
        bg=COLOR_FONDO
    )
    frame_parent.pack(
        fill='both',
        expand=True
    )
    frame_header(frame_parent)
    frame_logo(frame_parent)
    frame_button(frame_parent)


def frame_header(frame_parent):
    header = tk.Frame(frame_parent)
    create_header(header)
    header.pack(
        pady=(40, 10)
    )


def frame_logo(frame_parent):
    logo = tk.Frame(frame_parent)
    create_logo(logo, open_image)
    logo.pack(
        pady=(20,20)
    )


def frame_button(frame_parent):
    button = tk.Frame(frame_parent)
    button.config(
        background=COLOR_FONDO
    )
    create_button(button, select_file)
    button.pack(
        fill='y',
        expand=True,
        pady=(0, 10)
    )