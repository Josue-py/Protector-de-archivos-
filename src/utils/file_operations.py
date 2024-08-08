from tkinter import filedialog

def select_file():
    file_path = filedialog.askopenfilename(
        initialdir='/',
        title='Guardar archivo',
        filetypes=(
            ('Archivos de texto', '*.txt'),
            ('Todos los archivos', '*.*')
        )
    )

    if file_path:
        try:
            with open(file_path, "w") as archivo:
                archivo.write("Contenido del archivo")
            print(f"Archivo guardado en: {file_path}")
        except IOError:
            print("Error al guardar el archivo.")