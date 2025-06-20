import requests
import os
import tkinter as tk
from tkinter import filedialog
import zipfile


def korblox():
    url = 'https://github.com/TejasPlayzYT/korblox-and-headless-FOSS/releases/download/v1.0/korblox.mesherzipped.zip'
    response = requests.get(url, stream=True)
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    if folder_path:
        file_path = os.path.join(folder_path, 'korblox.mesherzipped.zip')
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        mesher_folder_path = os.path.join(folder_path, 'mesher')
        if not os.path.exists(mesher_folder_path):
            os.makedirs(mesher_folder_path)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(mesher_folder_path)
        os.startfile(mesher_folder_path)
