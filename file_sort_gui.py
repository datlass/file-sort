from tkinter import *
from tkinter import filedialog

root = Tk()  # create window called root

def askdir():
    folder = filedialog.askdirectory()
    print("This folder has been selected: ")
    print(folder)

my_button = Button(root, text="Search organizing folder", command= askdir, padx=50)
my_button.pack()

root.mainloop()