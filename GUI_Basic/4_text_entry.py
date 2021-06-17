from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Enter text")

e = Entry(root, width=30) # not able to enter
e.pack()
e.insert(0, "insert one line")

def btn_command():
    # Print contents
    print(txt.get("1.0", END)) 
    #(1.0), END : get the text from the beginning to the end
    # 1 : First Line, 2 : 0 collumn, END : to the end
    print(e.get())
    
    # Delete contents
    txt.delete("1.0", END)
    e.delete(0, END)
button = Button(root, text="click", command=btn_command)
button.pack()
root.mainloop() # not to make the window close
