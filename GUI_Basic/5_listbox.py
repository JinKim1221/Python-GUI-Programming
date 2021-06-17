from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

listbox = Listbox(root, selectmode="extended", height=3) 
# selectmode ='extended' : multiple choices, single : only one
# height = 0 : all the options of list is shown if height=3 only 3 options are displayed
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Water Mellon")
listbox.insert(END, "Grape")
listbox.pack()

def btn_command():
    # Delete
    # listbox.delete(0)

    # check the number of options
    # print("In the list there are ", listbox.size(), "options")

    # Check what options in the list(start index, end index)
    # print("from the first to the third : ", listbox.get(0,2))

    # Check the choseon options in the list
    print("Chosen one(s) : ", listbox.curselection()) #current selection

button = Button(root, text="click", command=btn_command)
button.pack()

root.mainloop() # not to make the window close
