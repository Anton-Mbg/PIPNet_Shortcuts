import csv
import os
import shutil
import pandas as pd
import numpy as np

def organize_images_by_place(csv_path, image_dir, output_dir):
    """
    Organisiert Bilder in Ordner 'land' und 'water' basierend auf dem 'place'-Wert in der CSV.

    Args:
        csv_path (str): Pfad zur CSV-Datei.
        image_dir (str): Verzeichnis, in dem sich die Bilder befinden.
        output_dir (str): Basis-Ausgabeverzeichnis für 'land' und 'water'.
    """
    bird_cat_dict = {}
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
        bird_cat_dict[img_filename]=place
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

    return bird_cat_dict

# Beispielaufruf
#csv_path = "/Users/anton/CodingProjects/PIPNet_Shortcuts/util/metadata.csv"  # Ersetze mit dem tatsächlichen Pfad zur CSV
#image_dir = "/Users/anton/CodingProjects/PIPNet_Shortcuts/data/waterbird/test/waterbird"      # Ersetze mit dem Verzeichnis der Bilder
#output_dir = "/Users/anton/CodingProjects/PIPNet_Shortcuts/data/waterbird/test/waterbird/test"     # Ersetze mit dem gewünschten Ausgabeverzeichnis

#print(organize_images_by_place(csv_path, image_dir, output_dir))


def get_acc_per_group(img_pred_dir):
    dict = {}
    file_path = "/home/thielant/PIPNet/util/metadata.csv"

    """
    Liest eine CSV-Datei Zeile für Zeile ein und speichert die Zeilen in einer Liste.

    Args:
        file_path (str): Pfad zur CSV-Datei.

    Returns:
        list: Liste mit Zeilen (jede Zeile ist eine Liste von Spalten).
    """
    rows_df = pd.read_csv(file_path,delimiter=',', index_col=0, header=0)
    anz_per_group = np.array([[[0],[0]],
                     [[0],[0]]])
    score_per_group = np.array([[[0],[0]],
                     [[0],[0]]])
    for row in rows_df.itertuples():
        img_filename = row.img_filename.split("/", 1)[1]
        img_label = row.y #0 for ?? 1 for ??
        img_background = row.place #0 for ?? 1 for ??

        anz_per_group[img_label][img_background] += 1
        if (img_label == img_pred_dir[img_filename]):
            score_per_group[img_label][img_background] += 1
        dict[img_filename] = {"label" :row.y, "place": row.place }

    result = score_per_group /anz_per_group

    return result[0][0],result[0][1],result[1][0],result[1][1]
# erster index ist das label also 1=wb oder 0=lb und zweiter index ist background 1 = water und 0 = land
