from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

# button1 = Button(root, text="button1")
# button2 = Button(root, text="button2")

# button1.grid(row=1, column=0)
# button2.grid(row=1, column=1)

# The first line
button_f16 = Button(root, text="F16")
button_f17 = Button(root, text="F17")
button_f18 = Button(root, text="F18")
button_f19 = Button(root, text="F19")

button_f16.grid(row=0, column=0)
button_f17.grid(row=0, column=1)
button_f18.grid(row=0, column=2)
button_f19.grid(row=0, column=3)

# clear line
button_clear = Button(root, text="clear")
button_equal = Button(root, text="=")
button_divide = Button(root, text="/")
button_multiply = Button(root, text="*")

button_clear.grid(row=1, column=0)
button_equal.grid(row=1, column=1)
button_divide.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

# Button from 7
button_7 = Button(root, text="7")
button_8 = Button(root, text="8")
button_9 = Button(root, text="9")
button_sub = Button(root, text="-")

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

# Button from 4
button_4 = Button(root, text="4")
button_5 = Button(root, text="5")
button_6 = Button(root, text="6")
button_add = Button(root, text="+")

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_add.grid(row=3, column=3)


# Button from 4
button_1 = Button(root, text="1")
button_2 = Button(root, text="2")
button_3 = Button(root, text="3")
button_enter = Button(root, text="enter")

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_enter.grid(row=4, column=3, rowspan=2) #rowspan : it adds more rows from the current position to the bottom row


# Button from 4
button_0 = Button(root, text="0")
button_point = Button(root, text=".")

button_0.grid(row=5, column=0,columnspan=2)
button_point.grid(row=5, column=2)
root.mainloop() # not to make the window close

