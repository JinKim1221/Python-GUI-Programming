from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

label1 = Label(root, text="Choose menu").pack()

burger_var = IntVar()  #save the value as integer
btn_burger1 = Radiobutton(root, text="Burger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="Cheese Burger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Bacon Burger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label1 = Label(root, text="Choose drinks").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Sprite", value="Sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btn_command():
    print(burger_var.get()) # get the value of the chosen menu 
    print(drink_var.get()) # get the value of the chosen drink 

button = Button(root, text="Order", command=btn_command)
button.pack()

root.mainloop() # not to make the window close
