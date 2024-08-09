import tkinter as tk
from utils.config import COLOR_FONDO

def create_header(container):
    header = tk.Label(container)
    header.config(
        text='Protege tus archivos',
        font=('Arial', 20, 'bold'),
        background=COLOR_FONDO
    )
    header.pack()

def create_logo(container, img):
    logo = tk.Label(container)
    logo.configure(
        image=img
    )
    logo.pack(
        pady=(10,10)
    )

def create_button(container, command):
    button = tk.Button(container)
    button.config(
        text='Seleccionar archivo',
        font=('Arial', 12, 'bold'),
        command=command
    )
    button.pack(
        anchor='center',
        expand=True
    )