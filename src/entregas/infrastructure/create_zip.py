import zipfile
import os

def create_zip(zip_name, folder):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                # Agregar el archivo al ZIP manteniendo la estructura de directorios
                zipf.write(file_path, os.path.relpath(file_path, os.path.join(folder, '..')))


# Crear el ZIP para entregas
create_zip('entregas.zip', 'entregas')
