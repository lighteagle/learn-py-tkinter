"""
A simple Tkinter application that displays a window with the text 'Hello World!'.
"""

from tkinter import Tk, Label

# Create the root window
root = Tk()

# Create a Label widget
myLabel = Label(root, text='Hello World!')

# Show it onto the screen
myLabel.pack()

# Run the application
root.mainloop()