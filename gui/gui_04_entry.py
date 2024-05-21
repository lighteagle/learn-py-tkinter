"""
Create a simple Tkinter application that allows the user to enter their name
and displays a personalized greeting when a button is clicked.
"""

from tkinter import Tk, Button, Label, Entry

def show_message():
    """
    Create and display a label with a personalized greeting message.
    The message includes the name entered by the user in the Entry widget.
    """
    message = f"Hello, {e.get()}!"
    message_label = Label(root, text=message)
    message_label.pack()

# Create the main window
root = Tk()

# Create an Entry widget for user to input their name
e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name")

# Create a button that, when clicked, calls the show_message function
button = Button(root, text="Submit", command=show_message)
button.pack()

# Run the Tkinter event loop
root.mainloop()
