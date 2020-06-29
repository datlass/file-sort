from tkinter import *

root = Tk()  # create window

# Label widget
myLabel = Label(root, text="Hello World")
myButton = Button(root, text="Click me").pack()

myLabel.grid(row=0,column=0)

root.mainloop()