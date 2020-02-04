# Tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import *
from tkinter import constants

# PIL
from PIL import *
from PIL import Image

#cv2
import cv2

# Autres
import os
from pathlib import Path

# Creation fenetre TK
root = tk.Tk()
maintext = Label(root, text="")
maintext.grid(row=0,column=0)
root.update()


