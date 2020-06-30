from tkinter import *
from tkinter import filedialog
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


my_button = Button(root, text="Search folder to organize", command= askdir)
my_button.grid(row = 0,column = 1)

root.mainloop()