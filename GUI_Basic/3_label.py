from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

label1 = Label(root, text="Hello world")
label1.pack()

photo = PhotoImage(file="GUI_Basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See you again")
    
    global photo2 # declare photo2 as global variable to tell the garbage collection that this is needed.
    photo2 = PhotoImage(file="GUI_Basic/image2.png")
    label2.config(image=photo2)

button = Button(root, text="Click", command=change)
button.pack()

root.mainloop() # not to make the window close

