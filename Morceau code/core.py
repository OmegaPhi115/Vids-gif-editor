# Everyone is here !
from __future__ import print_function, unicode_literals
print("    >>> Loading JSaH... | Loading dependencies", end="\r")
import cv2
import os
from pathlib import Path
from PIL import *
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pprint import *
from PyInquirer import *
import threading
from tkinter.ttk import *
from tkinter import constants
from multiprocessing.dummy import Pool as ThreadPool
from distutils.dir_util import copy_tree
import ast

print("    >>> Loading JSaH... | Creating TKinter window", end="\r")

root = tk.Tk()
maintext = Label(root, text="")
maintext.grid(row=0,column=0)
root.update()

print("    >>> Loading JSaH... | Loading PyInquirer", end="\r")

def colorHEXrgba(HEX):
    """
    Convert color in HEX into RGB
    :param HEX: str (#RRGGBB)
    :return: tuple (RRR, GGG, BBB)
    """
    HEX = HEX.lstrip('#')
    return tuple(int(HEX[i:i + 2], 16) for i in (0, 2, 4))

def colorrgbaHEX(input):
    out = "#"
    for ele in input:
        out += str(int(ele, 10))


colors = {
    "pink jsab": "uhm",
    "pink": colorHEXrgba("#ff1474")
}

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#ff1474 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#ff1474 bold',
    Token.Question: '',
})

print("    >>> Loading JSaH... | Checking folders", end="\r")
data_folder = Path(os.path.dirname(__file__), "Data")

overidespliting = False
test_data_folder = ""
#test_data_folder = Path(data_folder, 'testdata')


def colorinterval(x, y, z):
    """
    test for y < x < z with tupples
    :param x:
    :param y:
    :param z:
    :return:
    """
    a = y[0] <= x[0] <= z[0]
    b = y[1] <= x[1] <= z[1]
    c = y[1] <= x[1] <= z[1]
    return a and b and c
