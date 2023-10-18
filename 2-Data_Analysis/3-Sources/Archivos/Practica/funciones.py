import os
import shutil
from variables import folders, doc_types, img_types, software_types

def crear_directorios():
    for i in folders:
        if i not in os.listdir():
            os.mkdir(i)

def mover_archivos():
    for i in os.listdir():
        try:
            if i.endswith(doc_types):
                shutil.move(i, 'documentos')
            elif i.endswith(img_types):
                shutil.move(i, 'imagenes')
            elif i.endswith(software_types):
                shutil.move(i, 'software')
            else:
                if not os.path.isdir(i) and not i.endswith('.py'):
                    shutil.move(i, 'otros')
        except:
            pass