from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

chkvar = IntVar() # save the value as integer
chkbox = Checkbutton(root, text="No more pop up for today", variable=chkvar)
chkbox.select() # check automatically
chkbox.deselect() 
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="No more pop up for a week", variable=chkvar2)
chkbox2.pack()

def btn_command():
    print(chkvar.get()) # 0 : deselect, 1 : select
    print(chkvar2.get())
button = Button(root, text="click", command=btn_command)
button.pack()

root.mainloop() # not to make the window close
