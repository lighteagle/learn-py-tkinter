"""
This module creates a simple Tkinter application that displays two labels in a grid.
"""
from tkinter import Tk, Label

# Create the main window
root = Tk()

# Create a labels
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My Name is John Elder')

# Arrange labels in a grid
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# Run the application
root.mainloop()
