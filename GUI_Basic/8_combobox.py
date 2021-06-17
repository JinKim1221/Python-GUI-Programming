import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

values = ["Day " + str(i) for i in range(1, 32)] # 1~31
comboBox = ttk.Combobox(root, height=5, values= values, state="readonly")

comboBox.pack()
comboBox.set("Payment") # inital title of combo box

def btn_command():
    print(comboBox.get()) # display the chosen one

button = Button(root, text="Order", command=btn_command)
button.pack()

root.mainloop() # not to make the window close
