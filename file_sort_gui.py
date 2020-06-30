from tkinter import *

root = Tk()  # create window

# Label widget
def myClick():
    myLabel = Label(root, text="Button Clicked")
    myLabel.pack()


myButton = Button(root, text="Click me", command = myClick, padx=50).pack()


root.mainloop()