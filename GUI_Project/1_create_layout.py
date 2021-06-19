from tkinter import *

root = Tk()
root.title("GUI Project")

# File Frame (add files, delete the chosen)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add file")
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete file")
btn_delete_file.pack(side="right")

# List Frame (when you add files you see the files)
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Path to Save Frame
path_frame = LabelFrame(root, text="Path")
path_frame.pack()

text_dest_path = Entry(path_frame)
text_dest_path.pack(side="left", fill="x", expand=True, ipady=4) # ipad : inner pad 

button_dest_path = Button(path_frame, text="Find", width=10)
button_dest_path.pack(side="right")

root.resizable(False, False)
root.mainloop()