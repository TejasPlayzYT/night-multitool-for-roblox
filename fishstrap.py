import requests
import os
import tkinter as tk
from tkinter import filedialog

def fishstrap():
    url = 'https://github.com/fishstrap/fishstrap/releases/download/v2.9.1.2/Fishstrap-v2.9.1.2.exe'
    response = requests.get(url, stream=True)
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        file_path = os.path.join(folder_path, 'Fishstraplatest.exe')
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        os.startfile(file_path)

def bloxstrap():
    url = 'https://github.com/bloxstraplabs/bloxstrap/releases/download/v2.9.0/Bloxstrap-v2.9.0.exe'
    response = requests.get(url, stream=True)
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        file_path = os.path.join(folder_path, 'Bloxstraplatest.exe')
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        os.startfile(file_path)
