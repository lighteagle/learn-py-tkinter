"""
Create a simple Tkinter application that displays a button which, when clicked, shows a new label.
"""

from tkinter import Tk, Button, Label

def show_message():
    """
    Create and display a label with the text 'Look! I clicked a button!'.
    """
    message_label = Label(root, text="Look! I clicked a button!")
    message_label.pack()

# Create the main window
root = Tk()

# Create a button with the text 'Click me!' and set its command to the show_message function
button = Button(root, text="Click me!", command=show_message)
button.pack()

# Run the Tkinter event loop
root.mainloop()
