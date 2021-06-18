import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Meme Creator")
root.geometry("640x480") # Setting size of the window

def info():
    msgbox.showinfo("Alarm", "Works fine")

def warn():
    msgbox.showwarning("Warning", "Warning Alarm")

def error():
    msgbox.showerror("Error", "Error Alarm")
    
def cancel():
    msgbox.askokcancel("Cancel", "Optional Confirm/Cancel")

def retry_cancel():
    response = msgbox.askretrycancel("Retry", "Temporarily Error, retry?")
    #Yes : 1, No : 0
    if response == 1:
        print("Retry")
    elif response == 0:
        print("Cancel")

def yes_no():
    msgbox.askyesno("Yes/No", "Yes / No?")

def yes_no_cancel():
    response = msgbox.askyesnocancel(title=None, message="No title")
    print(response)
    #Yes : 1, No : 0, Cancel : others
    if response == 1:
        print("YES")
    elif response == 0:
        print("NO")
    else:
        print("Cancel")

Button(root, command=info, text="Alarm").pack()
Button(root, command=warn, text="Warn").pack()
Button(root, command=error, text="Error").pack()

Button(root, command=cancel, text="Cancel").pack()
Button(root, command=retry_cancel, text="Retry").pack()
Button(root, command=yes_no, text="Yes No").pack()
Button(root, command=yes_no_cancel, text="Yes No Cancel").pack()

root.mainloop() # not to make the window close
