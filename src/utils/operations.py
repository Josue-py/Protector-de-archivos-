from cryptography.fernet import Fernet
from PyPDF2 import PdfReader, PdfWriter
import os
from tkinter import Tk, filedialog

class ProtectorPDF:
    """
       Clase para proteger un archivo PDF con una contraseña utilizando cifrado simétrico.

       Atributos:
           password (str): Contraseña utilizada para cifrar el PDF.
           clave_fernet (bytes): Clave generada para cifrar la contraseña.
           contrasena_cifrada (bytes): Contraseña cifrada utilizando la clave Fernet.

       Métodos:
           __init__(self, password):
               Inicializa la instancia de ProtectorPDF y cifra la contraseña.

           cifrar_contrasena(self):
               Cifra la contraseña proporcionada utilizando la clave Fernet.

           proteger_pdf(self, input_pdf_path, output_pdf_path):
               Protege el archivo PDF con la contraseña cifrada.

           leer_pdf(self, input_pdf_path):
               Lee el archivo PDF desde la ruta especificada.

           copiar_paginas_al_writer(self, reader):
               Copia las páginas del PDF original al objeto PdfWriter.

           aplicar_cifrado_y_guardar_pdf(self, writer, output_pdf_path):
               Aplica el cifrado al objeto PdfWriter y lo guarda en la ruta especificada.
       """
    def __init__(self, password):
        self.password = password
        self.clave_fernet = Fernet.generate_key()
        self.contrasena_cifrada = self.cifrar_contrasena()

    def cifrar_contrasena(self):
        cifrador = Fernet(self.clave_fernet)
        return cifrador.encrypt(self.password.encode())

    def proteger_pdf(self, input_pdf_path, output_pdf_path):
        reader = self.leer_pdf(input_pdf_path)
        writer = self.copiar_paginas_al_writer(reader)
        self.aplicar_cifrado_y_guardar_pdf(writer, output_pdf_path)

    def leer_pdf(self, input_pdf_path):
        with open(input_pdf_path, "rb") as file:
            return PdfReader(file)

    def copiar_paginas_al_writer(self, reader):
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        return writer

    def aplicar_cifrado_y_guardar_pdf(self, writer, output_pdf_path):
        writer.encrypt(self.password)
        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)
        print("El archivo PDF ha sido protegido con contraseña")

def select_file():
    """Permite al usuario seleccionar un archivo PDF a través del explorador de archivos"""
    Tk().withdraw()  # Oculta la ventana principal de Tkinter
    file_path = filedialog.askopenfilename(
        title='Seleccionar archivo PDF',
        filetypes=(('Archivos PDF', '*.pdf'), ('Todos los archivos', '*.*'))
    )
    return file_path

# Script de prueba
if __name__ == "__main__":
    ruta_pdf_original = select_file()
    if not ruta_pdf_original:
        print("No se ha seleccionado ningún archivo. Por favor, selecciona uno.")
    else:
        # Crear la ruta del archivo protegido
        ruta_pdf_protegido = ruta_pdf_original.replace(".pdf", "_protegido.pdf")

        # Definir la contraseña para el PDF protegido
        password = input("Escriba una contraseña: ")

        # Crear instancia de ProtectorPDF
        protector = ProtectorPDF(password)

        # Proteger el PDF
        protector.proteger_pdf(ruta_pdf_original, ruta_pdf_protegido)

        # Confirmar la creación del archivo protegido
        if os.path.exists(ruta_pdf_protegido):
            print(f"El archivo protegido se ha creado en {ruta_pdf_protegido}")
        else:
            print("Hubo un problema al crear el archivo protegido.")
