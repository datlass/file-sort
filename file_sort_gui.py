from tkinter import *
from tkinter import filedialog, messagebox
from file_sort import sort_folder, filesearch

root = Tk()  # create window called root
root.title("Dimas's Organizing Program")
#Adds color to the root
mac_grey = '#ededed'
root.configure(background=mac_grey)

# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 3 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

# Constant x padding var
widthx = 25

# Adds title to the python window
my_title = Label(root, text="Insert directory to organize",borderwidth=2, relief="groove")

e = Entry()
e.insert(0, "Input directory here")

# Function to select the directory for the search button
frame = Frame(root)
list_label = Label(frame, text="Files within selected directory:")
file_list = Listbox(frame)

def askdir():
    e.delete(0, 'end')
    folder = filedialog.askdirectory()
    print("This folder has been selected to sort: ")
    print(folder)
    e.insert(0, folder)
    file_list.delete(0, END)
    if len(filesearch(folder)) != 0:
        for file in filesearch(folder):
            file_list.insert(END, file)
    else:
        file_list.insert(END, "No files in this folder")


my_button = Button(root, text="Search folder to organize", command=askdir, padx=10)


# Function to select the directory for the organize button

def organize():
    response = messagebox.askokcancel("Organize Folder", "Are you sure you want to organize the folder?")
    print("Input:" + str(response))
    if response is True:
        print("Ok then performing sort")
        sort_folder(e.get())
    else:
        print("Ok no sort then :(")


execute_ocd = Button(root, text="Organize this folder", command=organize)

#Adds a scrollbar to the frame and tell it to follow the listbox
file_scroll_y = Scrollbar(frame)
file_scroll_x = Scrollbar(frame, orient = HORIZONTAL)
#scrollbar.grid( row=4, column=2 , columnspan=3,)

#Attaches scrollbar to file list
file_scroll_y.config(command = file_list.yview)
file_list.config(yscrollcommand = file_scroll_y.set)

file_scroll_x.config(command = file_list.xview)
file_list.config(xscrollcommand = file_scroll_x.set)

#Organizes the listbox components within the frame using grid system
list_label.grid(row=0, column=0)
file_scroll_y.grid(row=1, column=0,sticky='NSE')
file_scroll_x.grid(row=1, column=0,sticky='SEW')
file_list.grid(row=1, column=0)

# All the Elements
my_title.grid(row=0, column=0, columnspan=3,pady=(10,5))
e.grid(row=1, column=0)
my_button.grid(row=1, column=1)
execute_ocd.grid(row=1, column=2)
file_list.config(width=35)
#list_label.grid(row=3, column=0,pady=5)
frame.grid(row=4, column=0, columnspan=3,pady=25)
#file_list.grid(row=4, column=0, columnspan=3)

root.mainloop()
