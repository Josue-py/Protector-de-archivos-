from tkinter import filedialog
from PyPDF2 import PdfReader
import os

file_path = "Python Basics A Practical Introduction to Python 3.pdf"
reader = PdfReader(file_path)

meta = reader.metadata

print(meta.title)
file_size_in_bytes = os.path.getsize(file_path)
file_size_in_mb = file_size_in_bytes / (1024 * 1024)
print(f"size of the file: {file_size_in_mb:.2f} MB")

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

            def select_file():
                file_path = filedialog.askopenfilename(
                    initialdir='/',
                    title='Guardar archivo',
                    filetypes=(
                        ('Archivos de texto', '*.pdf'),
                        ('Todos los archivos', '*.*')
                    )
                )

                if file_path.endswith('.pdf'):
                    print('Este archivo es compatible')
                else:
                    print('Este archivo no es compatible,solo archivos PDF')
                    # try:
                    #     with open(file_path, "w") as archivo:
                    #         archivo.write("Contenido del archivo")
                    #     print(f"Archivo guardado en: {file_path}")
                    # except IOError:
                    #     print("Error al guardar el archivo.")

            def open_image():
                img = Image.open(LOGO_PNG)
                resized_image = img.resize((100, 100))
                image_tk = ImageTk.PhotoImage(resized_image)
                return image_tk