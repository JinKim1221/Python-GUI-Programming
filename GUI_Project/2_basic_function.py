import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("GUI Project")

# Add file
def add_file():
    files = filedialog.askopenfilenames(title="Select images", \
        filetypes = (("PNG", "*.png"),("All files", "*.*")), \
        initialdir=r"C:\Users\Jin\Desktop\Personal Project\Python_game\pygame_project\images")
        # display the path the user set
        
    # Present files that a user selected
    for file in files:
        list_file.insert(END, file)

# Delete file
def delete_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# File Frame (add files, delete the chosen)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5) # make some space between frames

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add file", command=add_file)
btn_add_file.pack(side="left")

btn_delete_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete file", command=delete_file)
btn_delete_file.pack(side="right")

# List Frame (when you add files you see the files)
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y", padx=5, pady=5)

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# Path to Save Frame
path_frame = LabelFrame(root, text="Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

text_dest_path = Entry(path_frame)
text_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # ipad : inner pad 

button_dest_path = Button(path_frame, text="Find", width=10)
button_dest_path.pack(side="right", padx=5, pady=5)

# Option Frame
option_frame = LabelFrame(root, text="Option")
option_frame.pack(padx=5, pady=5, ipady=5)

# Option Frame - 1. Width
# Width option label
lbl_width = Label(option_frame, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# Width option combo
opt_width = ["remain", "1024", "800", "640"]
combo_width = ttk.Combobox(option_frame, state="readonly", values=opt_width, width=10)
combo_width.current(0)
combo_width.pack(side="left", padx=5, pady=5)

# Option Frame - 2. Space between pictures
# Space option label
lbl_space = Label(option_frame, text="Space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# Space option combo
opt_space = ["none", "narrow", "normal", "wide"]
combo_space = ttk.Combobox(option_frame, state="readonly", values=opt_space, width=10)
combo_space.current(0)
combo_space.pack(side="left", padx=5, pady=5)

# Option Frame - 3. File format
# File format option label
lbl_fformat = Label(option_frame, text="Format", width=8)
lbl_fformat.pack(side="left", padx=5, pady=5)

# File format option combo
opt_format = ["PNG", "JPG", "BMP"]
combo_fformat = ttk.Combobox(option_frame, state="readonly", values=opt_format, width=10)
combo_fformat.current(0)
combo_fformat.pack(side="left", padx=5, pady=5)

# Progress bar
progress_frame = LabelFrame(root, text="Progress")
progress_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# Run Frame
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

button_close = Button(run_frame, padx=5, pady=5, text="Close", width=12, command=root.quit)
button_close.pack(side="right", padx=5, pady=5)

button_run = Button(run_frame, padx=5, pady=5, text="Run", width=12)
button_run.pack(side="right", padx=5, pady=5)



root.resizable(False, False)
root.mainloop()