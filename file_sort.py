from os import listdir
from os.path import isfile, join
import os
from shutil import move
from tkinter import messagebox


# This script seperates files and puts them in their respective file type folder

# Project inspiration and assistance:
# https://medium.com/better-programming/how-i-organise-my-downloads-folder-with-python-6c76358968ea

# Example code for list directory:
# entries = listdir('sort_folder')
# print(type(entries[0]))
# print(entries) # Example code for listdir which creates a list
# print(os.path.abspath('sort_folder')) Example to show absolute file directory path

def sort_folder(mypath):
    # Confirm if mypath is an existing directory
    if os.path.isdir(mypath):
        #Extracts only files and discludes system files that start with .
        onlyfiles = [f for f in listdir(mypath) if f.startswith('.') is False and isfile(join(mypath, f))]
        print("Files contained in the organizing folder:")
        print(onlyfiles)
        # Finds the all the unique file type within the organizing folder
        filetype = []  # Empty list for storage
        for f in onlyfiles:
            # print(f.split('.', f.rfind('.'))[1])
            temp = f.split('.', f.rfind('.'))
            if len(temp) != 1 and temp[1] not in filetype:
                filetype.append(f.split('.', f.rfind('.'))[1])
        print("Type of file in the organizing folder:")
        print(filetype)
        # Create a folder for each of the file type
        os.chdir(mypath)  # Sets the working directory
        # Example of creating a folder:
        # if "folder" not in listdir(mypath):
        #     os.mkdir("folder")
        for f in filetype:
            file_name = f + "_folder"
            if file_name not in listdir(mypath):
                os.mkdir(file_name)
        # Now moves the file type in the respective file type folder
        for f in onlyfiles:
            temp_location = mypath + "/" + f
            temp = f.split('.', f.rfind('.'))
            if len(temp) != 1 and f.find('.') != -1:  # Obtains the file type
                folder_type: str = f.split('.', f.rfind('.'))[-1]
            else:
                folder_type = 'null'
            respective_folder = mypath + "/" + folder_type + "_folder"
            # print(temp_location)
            # print(respective_folder)
            # print("")
            if f.find('.') != -1:
                print(temp_location)
                print("Has been placed in :")
                print(respective_folder)
                print("")
                try:
                    move(temp_location, respective_folder)
                except:
                    messagebox.showerror("Error", "Files are overlapping or something else idk")

        print("Finished the sort! hopefully")
    else:
        print("Directory does not exist")
        messagebox.showerror("Error", "Directory does not exist")

def unpack_all(mypath):
    if os.path.isdir(mypath):
        onlyfiles = [f for f in listdir(mypath)]
    else:
        print("Directory does not exist")
        messagebox.showerror("Error", "Directory does not exist")
# print(listdir("/Users/HomeFolder/Desktop/Python Organize test"))

# unpack_all("/Users/HomeFolder/Desktop/Python Organize test")
print(listdir("/Users/HomeFolder/Desktop/"))