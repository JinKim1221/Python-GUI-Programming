from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

# button1 = Button(root, text="button1")
# button2 = Button(root, text="button2")

# button1.grid(row=1, column=0)
# button2.grid(row=1, column=1)

# The first line
button_f16 = Button(root, text="F16", width=5, height=2)
button_f17 = Button(root, text="F17", width=5, height=2)
button_f18 = Button(root, text="F18", width=5, height=2)
button_f19 = Button(root, text="F19", width=5, height=2)

button_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
button_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
button_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
button_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear line
button_clear = Button(root, text="clear", width=5, height=2)
button_equal = Button(root, text="=", width=5, height=2)
button_divide = Button(root, text="/", width=5, height=2)
button_multiply = Button(root, text="*", width=5, height=2)

button_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
button_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
button_divide.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
button_multiply.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# Button from 7
button_7 = Button(root, text="7", width=5, height=2)
button_8 = Button(root, text="8", width=5, height=2)
button_9 = Button(root, text="9", width=5, height=2)
button_sub = Button(root, text="-", width=5, height=2)

button_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
button_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
button_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
button_sub.grid(row=2, column=3, sticky=N+E+W+S,  padx=3, pady=3)

# Button from 4
button_4 = Button(root, text="4", width=5, height=2)
button_5 = Button(root, text="5", width=5, height=2)
button_6 = Button(root, text="6", width=5, height=2)
button_add = Button(root, text="+", width=5, height=2)

button_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
button_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
button_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
button_add.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)


# Button from 4
button_1 = Button(root, text="1", width=5, height=2)
button_2 = Button(root, text="2", width=5, height=2)
button_3 = Button(root, text="3", width=5, height=2)
button_enter = Button(root, text="enter", width=5, height=2)

button_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
button_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
button_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
button_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) #rowspan : it adds more rows from the current position to the bottom row


# Button from 4
button_0 = Button(root, text="0", width=5, height=2)
button_point = Button(root, text=".", width=5, height=2)

button_0.grid(row=5, column=0,columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
button_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)
root.mainloop() # not to make the window close

