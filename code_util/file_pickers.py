import tkinter as tk
from tkinter import filedialog

def pick_folder(title="Select a folder", print_title=True):
    if print_title:
        print(title)
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=title)
    return folder if folder else None

def pick_file(title="Select a file", print_title=True, filetypes=(("All Files", "*.*"),)):
    if print_title:
        print(title)
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(title=title, filetypes=filetypes)
    return filename if filename else None