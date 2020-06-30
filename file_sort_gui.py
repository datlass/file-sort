from tkinter import *
from tkinter import filedialog, messagebox
from file_sort import sort_folder
root = Tk()  # create window called root
root.title("Dimas's Organizing Program")


e = Entry()
e.grid(row = 0,column = 0)

#Function to select the directory
def askdir():
    folder = filedialog.askdirectory()
    print("This folder has been selected to sort: ")
    print(folder)
    e.insert(0,folder)

def organize():
    print("test")
    response = messagebox.askokcancel("Organize Folder","Are you sure you want to organize the folder?")
    print(response)
    if response is True:
        print("is true lol")
        #sort_folder(e.get()) #Needs an error message in case mypath is wrong


my_button = Button(root, text="Search folder to organize", command= askdir)
my_button.grid(row = 0,column = 1)

execute_ocd= Button(root, text="Organize this folder", command= organize)
execute_ocd.grid(row = 1,column = 0)

root.mainloop()