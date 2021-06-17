from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

button1 = Button(root, text="btn1")
button1.pack()

button2 = Button(root, padx=5, pady=10, text="btn2")
button2.pack()

button3 = Button(root, padx=10, pady=5, text="btn3")
button3.pack()

button4 = Button(root, width=10, height=3, text="btn4") # button size is fixed
button4.pack()

button5 = Button(root, fg="blue", bg="yellow", text="btn5")
button5.pack()

photo = PhotoImage(file="C:/Users/Jin/Desktop/Python_GUI/GUI_Basic/image.png")
button6 = Button(root, image=photo)
button6.pack()

def btn_command():
    print("Button is clicked")

button7 = Button(root, text="active button", command=btn_command)
button7.pack()

root.mainloop() # not to make the window close

