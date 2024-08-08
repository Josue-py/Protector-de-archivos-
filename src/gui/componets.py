import tkinter as tk

def create_header(container):
    header = tk.Label(
        container,
        text='Proteger tus archivos',
        font='Arial 16 bold',
        pady=10
    )
    header.pack()

def create_button(container, command):
    button = tk.Button(
        container,
        text='Seleccionar archivo',
        command=command
    )
    button.pack(pady=10)