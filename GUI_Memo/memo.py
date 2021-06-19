import os
from tkinter import *

root = Tk()
root.title("Untitled - Window Notepad")
root.geometry("640x480") # Setting size of the window


menu = Menu(root)

file_name="memo.txt"

def open_file():
    if os.path.isfile(file_name) : # if exists True, if not False
        with open(file_name, 'r', encoding="utf8") as file:
            txt.delete("1.0", END) # Text widget context is deleted
            txt.insert(END, file.read()) # File context is inserted

def save_file():
    with open(file_name, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # (1.0, END) : from the first line, 0 index to the end

# FILE
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_command(label="Quit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)
menu.add_cascade(label="Edit")
menu.add_cascade(label="Form")
menu.add_cascade(label="Help")


scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview) 

root.config(menu=menu)
root.mainloop() # not to make the window close
