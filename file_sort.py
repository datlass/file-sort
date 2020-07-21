from os import listdir
from os.path import isfile, join
import os
from shutil import move
from tkinter import messagebox
#Going to add wxpython later

# This script seperates files and puts them in their respective file type folder

# Project inspiration and assistance:
# https://medium.com/better-programming/how-i-organise-my-downloads-folder-with-python-6c76358968ea

# Example code for list directory:

# Mypath input is supposed to be an absolute directory to a folder
# File search returns name of files in a directory:
def filesearch(mypath):
    if os.path.isdir(mypath):
        onlyfiles = [f for f in listdir(mypath) if f.startswith('.') is False and isfile(join(mypath, f))]
        return onlyfiles
    else:
        print("Error path is not valid")


# Searches for the directory of the files within a directory
def filedirsearch(mypath):
    if os.path.isdir(mypath):
        onlyfiles = [mypath + "/" + f for f in listdir(mypath) if
                     f.startswith('.') is False and isfile(join(mypath, f))]
        return onlyfiles
    else:
        print("Error path is not valid")


def sort_folder(mypath):
    # Confirm if mypath is an existing directory
    if os.path.isdir(mypath):
        # Extracts only files and discludes system files that start with .
        onlyfiles = filesearch(mypath)
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


# returns directory to folders only within the current directory
def folderdirsearch(mypath):
    if os.path.isdir(mypath):
        onlyfolders = [mypath + "/" + f for f in listdir(mypath) if
                       isfile(join(mypath, f)) is False and f.find(".app") == -1]
        # print(onlyfolders)
        # print("length of directory: "+str(len(onlyfolders)))
        return onlyfolders
    else:
        print("Directory does not exist")
        messagebox.showerror("Error", "Directory does not exist")


# print(len(folderdirsearch("/Users/HomeFolder/Desktop/Python Organize test")))

# Finds all folders within given directory
def findallfolders(mypath):
    folders = folderdirsearch(mypath)
    for folder in folders:
        folders = folders + folderdirsearch(folder)
        # If there is a folder in a folder in the directory
        if len(folderdirsearch(folder)) != 0:
            additionalfolder = findallfolders(folder)
            additionalfolder.pop(0)
            folders = folders + additionalfolder

    return folders


def findallfiles(mypath):
    allfiles = filedirsearch(mypath)
    allfolders = findallfolders(mypath)
    for folder in allfolders:
        allfiles = allfiles + filedirsearch(folder)
    return allfiles


# Note the unpack doesn't delete the folders just empties them
def unpack_all(mypath):
    if os.path.isdir(mypath):
        allfilestomove = findallfiles(mypath)
        for file in allfilestomove:
            try:
                move(file, mypath)
            except:
                print("Error moving: " + file)
                print("to: " + mypath)
                # messagebox.showerror("Error", "Error moving files? perhaps overlapping")
        print("Done moving")
    else:
        print("Error path inputted not valid")

# testpath ="/Users/HomeFolder/Desktop/Python Organize test"
# print(findallfolders(testpath))
# print(findallfiles(testpath))
# unpack_all(testpath)
