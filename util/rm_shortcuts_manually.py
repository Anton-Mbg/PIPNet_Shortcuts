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
    df = pd.read_csv(dirShortcutIds, sep=",", names="ID", skiprows=0, na_values=["n.a."])
    listOfPrototypeIDs = df["ID"].tolist()
    for p in listOfPrototypeIDs:
        net.module._classification.weight[p] = 0


