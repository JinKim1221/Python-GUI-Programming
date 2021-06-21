import os
import tkinter.ttk as ttk
import tkinter.messagebox as msg_box
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("GUI Project")

# Add file
def add_file():

    files = filedialog.askopenfilenames(title="Select images", \
        filetypes = (("PNG", "*.png"),("All files", "*.*")), \
        initialdir=r"C:\Users\Jin\Desktop/Python_GUI/")
        # display the path the user set
        
    # Present files that a user selected
    for file in files:
        list_file.insert(END, file)

# Delete file
def delete_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# Path to save
def browse_dest_path():
    folder_selected = filedialog.askdirectory()# select a folder
    if folder_selected == "" :
        return
    # print(folder_selected)
    text_dest_path.delete(0, END)
    text_dest_path.insert(0, folder_selected)

# Merge_image
def merge_image():
    # print(list_file.get(0,END)) # get the list of all files
    images = [Image.open(x) for x in list_file.get(0, END)]

    #size => size[0] : width, size[1] : height
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]

    widths, heights = zip(*(x.size for x in images))


    # Maximum width, Total height
    max_width, total_height = max(widths), sum(heights)
    
    # Create a sketchbook to put images all together
    result_iamge = Image.new("RGB", (max_width, total_height), (255, 255,255)) # white background
    y_offset = 0 # y info

    # for img in images:
    #     result_iamge.paste(img, (0, y_offset))
    #     y_offset += img.size[1] # add the value of height to continuously put images 

    for idx, img in enumerate(images):
        result_iamge.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1)/len(images) * 100 # calcuate the percentage info
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(text_dest_path.get(), "test.jpg")
    result_iamge.save(dest_path)
    msg_box.showinfo("Alarm", "Merging finished")

# Run
def run():
    # check each option(width, space, format)
    # print("width : ", combo_width.get())
    # print("space : ", combo_space.get())
    # print("format : ", combo_fformat.get())

    # check file list
    if list_file.size() == 0:
        msg_box.showwarning("Warning", "Please add images")
        return
    
    # check path to save
    if text_dest_path.get() == "" :
        msg_box.showwarning("Warning", "Pleas select a folder")
        return

    merge_image()

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

button_dest_path = Button(path_frame, text="Browse", width=10, command=browse_dest_path)
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

button_run = Button(run_frame, padx=5, pady=5, text="Run", width=12, command=run)
button_run.pack(side="right", padx=5, pady=5)



root.resizable(False, False)
root.mainloop()

