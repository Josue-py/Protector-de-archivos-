from utils.config import ANCHO, ALTO, LOGO_ICO, NOMBRE_VENTANA

def windows_options(window):
    # Opción para indicar el título de la ventana
    window.title(NOMBRE_VENTANA)

    # Ícono de la ventana
    window.iconbitmap(LOGO_ICO)

    # Opción para indicar el tamaño de la ventana (ancho x alto)
    window.resizable(False, False)

    # Opciones de geometría de la ventana
    ancho_pantalla = window.winfo_screenwidth()
    alto_pantalla = window.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla // 2) - (ANCHO // 2)
    y = (alto_pantalla // 2) - (ALTO // 2)

    # Establecer la geometría de la ventana
    window.geometry(f'{ANCHO}x{ALTO}+{x}+{y}')