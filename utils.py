import os, sys

# ruta absoluta a la raíz del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_resource_path(relativa: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relativa)
    return os.path.join(BASE_DIR, relativa)