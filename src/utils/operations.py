from tkinter import filedialog
from PIL import Image, ImageTk
from .config import LOGO_PNG

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
        print('Correcto')
    else:
        print('Incorrecto')
        # try:
        #     with open(file_path, "w") as archivo:
        #         archivo.write("Contenido del archivo")
        #     print(f"Archivo guardado en: {file_path}")
        # except IOError:
        #     print("Error al guardar el archivo.")


def open_image():
    img = Image.open(LOGO_PNG)
    resized_image = img.resize((100,100))
    image_tk = ImageTk.PhotoImage(resized_image)
    return image_tk