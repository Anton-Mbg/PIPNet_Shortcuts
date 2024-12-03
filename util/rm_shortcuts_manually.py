from tqdm import tqdm
import argparse
import torch
import torch.nn.functional as F
import torch.utils.data
import os
from PIL import Image, ImageDraw as D
import torchvision.transforms as transforms
import torchvision
from util.func import get_patch_size
import random
import pandas as pd


@torch.no_grad()
def removeShortcutsManually(net, dirShortcutIds):
    try:
        with open(dirShortcutIds, 'r') as file:
            # Jede Zeile lesen, Leerzeichen entfernen und in eine Ganzzahl umwandeln
            listOfPrototypeIDs = [int(line.strip()) for line in file if line.strip()]
            for p in listOfPrototypeIDs:
                net.module._classification.weight[:,p] = 0
    except FileNotFoundError:
        print(f"Die Datei '{dirShortcutIds}' wurde nicht gefunden.")
        return []
    except ValueError:
        print("Die Datei enthält ungültige Daten (keine Ganzzahlen).")
        return []




