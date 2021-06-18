from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window
# root.geometry("640x480+300+100") # horizon, vertical, position of the window(+x, +y)

Label(root, text = "Choose your menu").pack(side="top")

Button(root, text = "Order").pack(side="bottom")
# Burger Frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Burger").pack()
Button(frame_burger, text="Cheese Burger").pack()
Button(frame_burger, text="Chicken Burger").pack()


# Drink Frame
frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()
root.mainloop() # not to make the window close

