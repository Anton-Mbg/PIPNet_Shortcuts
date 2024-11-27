import os
import shutil
import pandas as pd

def organize_images_by_place(csv_path, image_dir, output_dir):
    """
    Organisiert Bilder in Ordner 'land' und 'water' basierend auf dem 'place'-Wert in der CSV.

    Args:
        csv_path (str): Pfad zur CSV-Datei.
        image_dir (str): Verzeichnis, in dem sich die Bilder befinden.
        output_dir (str): Basis-Ausgabeverzeichnis für 'land' und 'water'.
    """
    # CSV einlesen
    df = pd.read_csv(csv_path)

    # Erstellen der Ausgabeverzeichnisse
    land_dir = os.path.join(output_dir, "land")
    water_dir = os.path.join(output_dir, "water")
    os.makedirs(land_dir, exist_ok=True)
    os.makedirs(water_dir, exist_ok=True)

    # Iteration über die Datenzeilen
    for _, row in df.iterrows():

        # Teil ab dem ersten Slash
        img_filename = row['img_filename'].split("/", 1)[1]
        place = row['place']

        # Vollständiger Pfad des Quellbildes
        source_path = os.path.join(image_dir, img_filename)

        # Zielverzeichnis basierend auf `place`
        if place == 0:
            dest_dir = land_dir
        elif place == 1:
            dest_dir = water_dir
        else:
            print(f"Ungültiger 'place'-Wert für Bild: {img_filename}")
            continue

        # Datei verschieben
        dest_path = os.path.join(dest_dir, os.path.basename(img_filename))
        if os.path.exists(source_path):
            shutil.move(source_path, dest_path)
            print(f"Verschoben: {source_path} -> {dest_path}")
        else:
            print(f"Datei nicht gefunden: {source_path}")

# Beispielaufruf
csv_path = "/Users/anton/CodingProjects/PIPNet_Shortcuts/util/metadata.csv"  # Ersetze mit dem tatsächlichen Pfad zur CSV
image_dir = "/Users/anton/CodingProjects/PIPNet_Shortcuts/data/waterbird/test/waterbird"      # Ersetze mit dem Verzeichnis der Bilder
output_dir = "/Users/anton/CodingProjects/PIPNet_Shortcuts/data/waterbird/test/waterbird/test"     # Ersetze mit dem gewünschten Ausgabeverzeichnis

organize_images_by_place(csv_path, image_dir, output_dir)