from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# if you don't set the scrollbar then the bar will go up again
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32) : # 1 ~ 31
    listbox.insert(END, "day "+ str(i))
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # should do mapping between scrollbar and listbox 

root.mainloop() # not to make the window close

