import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window


# progress_bar = ttk.Progressbar(root, maximum=100, mode="determinate") 
# # indeterminate : you don't know when stuff is finished
# progress_bar.start(10) # the bar moves every 10 ms
# progress_bar.pack()
# def btn_command():
#     progress_bar.stop()

# button = Button(root, text="Stop", command=btn_command)
# button.pack()

p_var2 = DoubleVar()
progress_bar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progress_bar2.pack()

def btn_command2():
    for i in range(1, 101):
        time.sleep(0.01)
        
        p_var2.set(i) # set value of pprogress bar
        progress_bar2.update() # UI update
        print(p_var2.get())

button = Button(root, text="Start", command=btn_command2)
button.pack()

root.mainloop() # not to make the window close
