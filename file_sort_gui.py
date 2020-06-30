from tkinter import *
from tkinter import filedialog, messagebox
from file_sort import sort_folder
root = Tk()  # create window called root
root.title("Dimas's Organizing Program")

widthx = 25
my_title = Label(root,text="Insert directory to organize")
my_title.grid(row=0,column=0)
e = Entry()
e.grid(row = 1,column = 0,padx = widthx)
e.insert(0,"Input directory here")
#Function to select the directory
def askdir():
    e.delete(0,'end')
    folder = filedialog.askdirectory()
    print("This folder has been selected to sort: ")
    print(folder)
    e.insert(0,folder)

def organize():
    response = messagebox.askokcancel("Organize Folder","Are you sure you want to organize the folder?")
    print("Input:" + str(response))
    if response is True:
        print("Ok then performing sort")
        sort_folder(e.get())
    else:
        print("Ok no sort then :(")



my_button = Button(root, text="Search folder to organize", command= askdir,padx = widthx)
my_button.grid(row = 1,column = 1)

execute_ocd= Button(root, text="Organize this folder", command= organize)
execute_ocd.grid(row = 2,column = 0)

root.mainloop()