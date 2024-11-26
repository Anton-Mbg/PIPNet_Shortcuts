import os
import shutil





def move_files_to_parent(parent_dir):
    """
    Verschiebt alle Dateien aus Unterordnern eines Überordners in den Überordner.

    Args:
        parent_dir (str): Pfad zum Überordner
    """
    if not os.path.isdir(parent_dir):
        print(f"{parent_dir} ist kein gültiges Verzeichnis.")
        return

    for root, dirs, files in os.walk(parent_dir):
        # root ist der aktuelle Ordner in der Iteration
        # dirs sind die Unterordner von root
        # files sind die Dateien in root
        if root == parent_dir:
            continue  # Überspringt den Überordner selbst

        for file in files:
            source_path = os.path.join(root, file)  # Aktueller Pfad zur Datei
            destination_path = os.path.join(parent_dir, file)  # Zielpfad im Überordner

            # Umbenennen, wenn Datei bereits im Ziel existiert
            if os.path.exists(destination_path):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_path):
                    destination_path = os.path.join(parent_dir, f"{base}_{counter}{ext}")
                    counter += 1

            # Datei verschieben
            shutil.move(source_path, destination_path)
            print(f"Verschoben: {source_path} -> {destination_path}")

    # Leere Unterordner löschen
    for root, dirs, files in os.walk(parent_dir, topdown=False):
        for dir_ in dirs:
            dir_path = os.path.join(root, dir_)
            if not os.listdir(dir_path):  # Prüft, ob Ordner leer ist
                os.rmdir(dir_path)
                print(f"Gelöscht: {dir_path}")


# Beispielaufruf
parent_directory = "/Users/anton/CodingProjects/PIPNet_Shortcuts/data/waterbird/test/waterbird"
move_files_to_parent(parent_directory)
