from tkinter import *

root = Tk()  # create window called root

e = Entry(root, width=50)

e.pack()  # Better to seperate in order to define e variable

e.insert(0, "Enter name here")


# Label widget
def myclick():
    my_label = Label(root, text=e.get())
    my_label.pack()
    print(e.get())


myButton = Button(root, text="Enter name", command=myclick(), padx=50).pack()

root.mainloop()